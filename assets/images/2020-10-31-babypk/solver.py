#/bin/env python3
import ctypes
import string
import base64


l = ctypes.CDLL("./elso.so")

def intToBytes(i: int):
    bytestring: list[int] = []
    while i != 0:
        bytestring.append(i%256)
        i //= 256
    return bytestring    



targets = [0xb0b0e14a693968d2, 0x757556d2c4be69d2, 0xebeb177dc2e22454, 0x5f5f28da051e5c6d, 0x606b8ba228f1fbe, 0x38389ab2489a5064]


targetSeqS = [intToBytes(i) for i in targets]

funcs = [l.elso, l.masodik, l.harmadik, l.negyedik, l.otodik, l.hatodik]

# this might be unnecessary but i'm unsure and it's damn late now so I'll leave it in (for now)
for f in funcs:
    f.argtypes = [ctypes.c_int]
    f.rettype = ctypes.c_int

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "/+="

flag_elements = []

for t, f in zip(targetSeqS, funcs):
    lookup = {f(ord(x)): x for x in chars}
    assert(len(lookup)==len(chars))
    b64 = "".join(lookup[b] for b in t)
    decoded = base64.b64decode(b64).decode("ascii")
    print(f"{b64} -> {decoded}")
    flag_elements.append(decoded)

print("=>")
print("-".join(flag_elements))
