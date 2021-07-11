---
title: "Prerecorded"
layout: page
---

- hard

Your friend Ben has become obsessed with a new horoscope software. Saying its trial version was super accurate. Looking at his texts and some research later you found an open source random horoscope software that has all the daily horoscopes Ben has received. They might be the same program. Show him that his software is fraud before he purchases the full version!

`nc challenges.crysys.hu 5005`

_author: Suma_

Attached files:
- [chall.js](chall.js)
- [horoscopes.txt](horoscopes.txt)

## Writeup

It took me some time to realize that there were downloads, but after that it was not too hard.

`chall.js` randomly picks 14 lines from the other file, sends it to us, and expect us to send back the 7 lines it'll pick next - so it's clear that we have to clone it's RNG.

Turns out RNG in JS is not even trying to be secure, it's some XOR based function with only a small state.

The fact that our indexes come from `Math.floor(Math.random() * SIZE)` puzzled me for some time, until I found [this writeup of a suspiciously similar challenge](https://www.josephsurin.me/posts/2020-11-30-hitcon-ctf-2020-100-pins-writeup). Basically this schema is already broken, see [this video](https://www.youtube.com/watch?v=_Iv6fBrcbAM) and also [this code](https://github.com/d0nutptr/v8_rand_buster).

So I've had the tool that is needed to clone the RNG, and also got the code for stepping it in either directions from the first linked ctf writeup. With that, it was just a matter of putting it all together and use it on the server.

Btw, it did not _always_ work, but I got the flag in a few tries.

```python
from pwn import *
import os
import xs128p
import struct
from math import floor

# https://www.josephsurin.me/posts/2020-11-30-hitcon-ctf-2020-100-pins-writeup
# https://github.com/TACIXAT/XorShift128Plus
# https://www.youtube.com/watch?v=_Iv6fBrcbAM

def to_double(value):
    double_bits = (value >> 12) | 0x3FF0000000000000
    return struct.unpack('d', struct.pack('<Q', double_bits))[0] - 1

# Calculates xs128p (XorShift128Plus)
def xs128p(state0, state1):
    s1 = state0 & 0xFFFFFFFFFFFFFFFF
    s0 = state1 & 0xFFFFFFFFFFFFFFFF
    s1 ^= (s1 << 23) & 0xFFFFFFFFFFFFFFFF
    s1 ^= (s1 >> 17) & 0xFFFFFFFFFFFFFFFF
    s1 ^= s0 & 0xFFFFFFFFFFFFFFFF
    s1 ^= (s0 >> 26) & 0xFFFFFFFFFFFFFFFF
    state0 = state1 & 0xFFFFFFFFFFFFFFFF
    state1 = s1 & 0xFFFFFFFFFFFFFFFF
    generated = state0 & 0xFFFFFFFFFFFFFFFF

    return state0, state1, generated


def reverse17(val):
    return val ^ (val >> 17) ^ (val >> 34) ^ (val >> 51)

def reverse23(val):
    MASK = 0xFFFFFFFFFFFFFFFF
    return (val ^ (val << 23) ^ (val << 46)) & MASK

def xs128p_backward(state0, state1):
    prev_state1 = state0
    prev_state0 = state1 ^ (state0 >> 26)
    prev_state0 = prev_state0 ^ state0
    prev_state0 = reverse17(prev_state0)
    prev_state0 = reverse23(prev_state0)
    generated = prev_state0
    return prev_state0, prev_state1, generated


with open("horoscopes.txt") as f:
    horoscopes = f.read().split("\n")

#conn = process(["node", "chall.js"],env={'FLAG':"IDK"})
conn = remote("challenges.crysys.hu", 5005)
conn.readline()
conn.readline()

indexes = []


for i in range(14):
    hor = conn.readline().decode().strip()
    indexes.append(horoscopes.index(hor))
MULT = 4501

with open("numbers","w") as f:
    for d in reversed(indexes):
        f.write(f"{d}\n")


os.system(f"cat numbers | python3 xs128p_solver.py --multiple {MULT} > out")
with open("out") as f:
    state0, state1 = map(int, f.read().strip().split(","))

s0, s1 = state0, state1

state0, state1, gen = xs128p(s0, s1)
for i in range(64-14):
    state0, state1, gen = xs128p_backward(state0, state1)
    idx = floor(to_double(gen) * MULT)
    #print(f"Sending: {idx}")
    conn.sendline(horoscopes[idx])
    print(f"Got: '{conn.clean().decode()}'")
    


print(conn.clean())
conn.interactive()
```