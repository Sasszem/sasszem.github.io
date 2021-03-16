# Variable length mtp

- medium

Adding some randomness to a weak cipher like mtp makes it harder to crack, right?

_author: Suma_

Attached file:
- [variable_length_mtp.zip](variable_length_mtp.zip)

## Writeup

This one is one of my favorite challenges. Not because it's very interesting or hard, but because I've literally dreamt up it's solution.

We get a few files:

`description.txt`:
```
Who needs one time pad when you can do multiple times pad? With extra randomness!
```

`chall.py`:
```python
from random import randint
import os

flag = b"cd21{placeholder}"
from flag import flag
print(flag)
data = os.urandom(23456-len(flag))

ind = randint(0, len(data))
data = data[:ind] + flag + data[ind:]

def xor(b1, b2):
    return bytes([d ^ k for d, k in zip(b1, b2)])

def encode(data, key):
    enc = bytearray()
    ind = 0
    i = 0
    while ind < len(data):
        i += 1
        k = min([len(data)-ind, randint(1, len(key))])
        enc.append(k)
        enc.extend(xor(data[ind:ind+k], key))
        ind += k
    return enc

key1 = os.urandom(128)
key2 = os.urandom(128)

with open("enc1", "wb") as f:
    f.write(encode(data, key1))

with open("enc2", "wb") as f:
    f.write(encode(data, key2)) 
```
And 2 binary files (`enc1`, `enc2`), clearly made with the above script.

So the script:
- generates a big amount of random bytes (basically garbage)
- sticks the flag randomly inside it
- generates 2 128 byte keys
- encodes the random text with the flag with both of them

Encryption is a bit odd:
- pick a random number between 1 and key length (but at most the number of remaining bytes)
- write that number
- write these many bytes XOR-encoded with the key

If we want to bruteforce both of the keys, we would have 256 unknown variables.

The idea I had was simple: what if the same byte of the message got encoded with different index bytes of the keys? So we have `KEY1[i]^M` and `KEY2[j]^M` with the same `M`? With all that randomness it will sure happen a lot! If we XOR them together, we'll get `KEY1[i]^M^KEY2[j]^M`, the `M`'s cancel and we have `KEY1[i]^KEY2[j]`.

Since all the randomness and the length we don't just have one of those info, but a lot of them. With these connections if we guess one byte of one of the keys, we "know" many bytes of the other, and based on them more from the first.

I've built a graph from the connections and ran a simple graph traversal on it to count how many components (and thus unknowns) we have - it turned out to be just 1!

So based on the same graph I could generate 256 different keys, and decode the text with them. Since I know that the flag starts with `cd21{`, I just filtered for it and found the flag.

```python
# diff attack
# if we just XOR the two messages w/ a different length key
# we can get k1[i]^k2[j]=xx type info
# the messages are LONG
# so we get MANY
# this means we can just write an optimized BF for it
# maybe use z3 idk


def parse_msg(enc):
    MSG = []
    while enc:
        l = enc[0]
        enc = enc[1:]
        MSG += [(d,i) for i,d in enumerate(enc[:l])]
        enc = enc[l:]
    return MSG


def test_parse():
    from chall import encode
    from random import randrange
    data = bytes(randrange(256) for _ in range(128))
    key  = bytes(randrange(256) for _ in range(128))
    enc = encode(data, key)
    parsed = parse_msg(enc)
    print(enc[:10])
    print(parsed[:10])
    dec = bytes(b[0]^key[b[1]] for a,b in zip(data, parsed))
    assert dec==data

def read_and_parse(fname):
    with open(fname, "rb") as f:
        return parse_msg(f.read())

# we have an even graph w/ 2*128 nodes
# and the edges are XOR connections
# we build it and then run a BFS on it
# we can get the number of the components this way
# and that's how many unknowns we REALLY have

class Graph:
    def __init__(self):
        self.nodes = {k:{} for k in range(256)}

    def add_edge(self, fr, to, xor):
        assert self.nodes[fr].get(to, xor) == xor
        self.nodes[fr][to] = xor

    def count_components(self):
        components = 0
        seen = set()
        while len(seen)<256:
            components += 1
            todo = []
            for c in range(256):
                if c not in seen:
                    todo.append(c)
                    seen.add(c)
                    break
            while todo:
                c = todo.pop()
                #print(c)
                seen.add(c)
                n = self.nodes[c]
                for k in n:
                    if not k in seen:
                        todo.append(k)

        return components

    def synth_from(self, base):
        keys = [None for _ in range(256)]
        keys[0] = base
        seen = set()
        while len(seen)<256:
            todo = []
            for c in range(256):
                if c not in seen:
                    todo.append(c)
                    seen.add(c)
                    break
            while todo:
                c = todo.pop()
                #print(c)
                seen.add(c)
                n = self.nodes[c]
                for k in n:
                    if not k in seen:
                        todo.append(k)
                        keys[k] = keys[c]^n[k]
        return keys[:128], keys[128:]


def build_graph(parsed1, parsed2):
    g = Graph()
    for p1, p2 in zip(parsed1, parsed2):
        g.add_edge(p1[1],128+p2[1],p1[0]^p2[0])
        g.add_edge(p2[1]+128,p1[1],p1[0]^p2[0])
    return g

def graph_from_data(f1="enc1", f2="enc2"):
    p1 = read_and_parse(f1)
    p2 = read_and_parse(f2)

    G = build_graph(p1, p2)
    print(f"Components: {G.count_components()}")
    return G,p1,p2

def decode(parsed, key):
    return bytes(p^key[i] for p, i in parsed)

if __name__=="__main__":
    g,p1,p2 = graph_from_data()
    for i in range(256):
        k1, k2 = g.synth_from(i)
        assert not None in k1
        assert not None in k2
        d = decode(p1, k1)
        if b"cd21{" in d:
            i = d.index(b"cd21")
            print(d[i:i+75])
```