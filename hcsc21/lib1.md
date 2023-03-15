---
title: "Liberate your Library - the Warm-up"
layout: page
---

- Exploitation
- Buffer Overflow
- C
- X86_64

Writeup by `Sasszem`

# Description and resources
## Mission brief
This time you have to find an offset in `LibC`.

## Instructions
Here is a little challenge to hone your exploitation skills. Don't worry, we take only baby steps in the first place. As you know it is getting more and more difficult to exploit even the simplest executables today due to the well-designed hardening solutions such as the NX bit, ASLR or RELRO. There is always a way to go so ROP/JOP was invented a couple of years ago.

We prepared a fully armored environment to succeed with this challenge, so we installed your favorite tools:
- GDB with PEDA
- Checksec
- Pwntools for python3
- vim/nano

You find a simple binary called `main` under `src` in your home directory. Your task is to determine the offset between the `LibC` base address and the `printf` function.
Please submit this offset in a hexadecimal number (e.g., `0x1234`) as your flag. Good luck!

---

# Writeup
## Short & smart solution

First, we have to find out where is libc. For example, use  `ldd` on `src/main`, and that reported a file path of `/lib/x86_64-linux-gnu/libc-2.28.so`. Now we need to get the offset in that. For that, a convenient way is to use `pwntools`.

- Open up a python shell
- `from pwn import *`
- `print(hex(ELF('/lib/x86_64-linux-gnu/libc-2.28.so').symbols['printf']))`

Ofc I did not do it with this simple method, but did use this one later.

## What I did

Okay, so we had a lot of tools, but I only used `gdb`.

Start it w/ `gdb src/main`. It will write half a screen of garbage, then we can run the program with `r`, then terminate it with `Ctrl+C`. Now it spat out another few screenful of garbage and also some colored info, but that does not interest me at all. `info proc mapping` and `x printf` do instead, as they tell me:

```
Mapped address spaces:

          Start Addr           End Addr       Size     Offset objfile
      0x563170602000     0x563170603000     0x1000        0x0 /home/user/src/main
      0x563170603000     0x563170604000     0x1000     0x1000 /home/user/src/main
      0x563170604000     0x563170605000     0x1000     0x2000 /home/user/src/main
      0x563170605000     0x563170606000     0x1000     0x2000 /home/user/src/main
      0x563170606000     0x563170607000     0x1000     0x3000 /home/user/src/main
      0x563171649000     0x56317166a000    0x21000        0x0 [heap]
      0x7f32378f8000     0x7f323791a000    0x22000        0x0 /lib/x86_64-linux-gnu/libc-2.28.so
      0x7f323791a000     0x7f3237a62000   0x148000    0x22000 /lib/x86_64-linux-gnu/libc-2.28.so
      0x7f3237a62000     0x7f3237aae000    0x4c000   0x16a000 /lib/x86_64-linux-gnu/libc-2.28.so
      0x7f3237aae000     0x7f3237aaf000     0x1000   0x1b6000 /lib/x86_64-linux-gnu/libc-2.28.so
      0x7f3237aaf000     0x7f3237ab3000     0x4000   0x1b6000 /lib/x86_64-linux-gnu/libc-2.28.so
      0x7f3237ab3000     0x7f3237ab5000     0x2000   0x1ba000 /lib/x86_64-linux-gnu/libc-2.28.so
      0x7f3237ab5000     0x7f3237abb000     0x6000        0x0
      0x7f3237ac2000     0x7f3237ac3000     0x1000        0x0 /lib/x86_64-linux-gnu/ld-2.28.so
      0x7f3237ac3000     0x7f3237ae1000    0x1e000     0x1000 /lib/x86_64-linux-gnu/ld-2.28.so
      0x7f3237ae1000     0x7f3237ae9000     0x8000    0x1f000 /lib/x86_64-linux-gnu/ld-2.28.so
      0x7f3237ae9000     0x7f3237aea000     0x1000    0x26000 /lib/x86_64-linux-gnu/ld-2.28.so
      0x7f3237aea000     0x7f3237aeb000     0x1000    0x27000 /lib/x86_64-linux-gnu/ld-2.28.so
      0x7f3237aeb000     0x7f3237aec000     0x1000        0x0
      0x7ffedf3fc000     0x7ffedf41d000    0x21000        0x0 [stack]
      0x7ffedf49f000     0x7ffedf4a2000     0x3000        0x0 [vvar]
      0x7ffedf4a2000     0x7ffedf4a3000     0x1000        0x0 [vdso]
  0xffffffffff600000 0xffffffffff601000     0x1000        0x0 [vsyscall]
```

and 
```
0x7f3237950560 <__printf>:      0x48000000d8ec8148
```

So `printf` is at `0x7f3237950560`, but that's mapped to `libc`. The corresponding line in the mapping info is `0x7f323791a000     0x7f3237a62000   0x148000    0x22000 /lib/x86_64-linux-gnu/libc-2.28.so` since `printf` is between this one's start and end address. This means the offset of `printf` in `libc` is `0x7f3237950560 - 0x7f323791a000 + 0x22000`.

The command `p/x 0x7f3237950560 - 0x7f323791a000 + 0x22000` tells me it's `0x58560`.