# :)

- medium

(╯°□°）╯︵ ┻━┻

_author: tk_

Attached file:
- [smiley](smiley)

## Writeup

`smiley` is a `stripped ELF64 binary`, so I've just dropped it into `IDA`

There was an easy-to-patch check of the current date, after that, it asks for a password and checks it.

A few checks were simple, so I knew that `key[3]=key[21]=key[35]=" "`, `key[0]="o"`, `key[1]="_"` and `key[2]="O"`.

After that, I've found a loop that generated indexes with a crazy function with lots of bit math (but actually just generated 5,6,7,...20), and XORed the 4,5,...19th bytes of the key with those and compared the result with a stored one.

I've put this one aside when I've seen that one of the stored values was bigger than 128, thus one of the bytes was not in ascii range...

I've come back later, and found another check I've missed the first time: `key[20]=")"` - and from that and the XORs we can just calculate most of the characters! I've realized when I saw it that it's not ASCII, but UTF-8...

After that, it takes the next unchecked byte, uses it as a single-byte XOR decrypt key for some data, and executes it as code, passing it the remaining key as a parameter. Then it does it again with another piece of data and another byte of the key.

I've written a python script that tries every byte and checks if the resulting code causes a segfault to narrow down the possibilities:
```python
# patched XOR checks bc I did not know that it's UTF-8

key_pat = list("o_O Apxxxxxxxxxxxxxxx xxxxxxxxxxxxx xxxxxxxx".encode())

from pwn import *

def test_key(k):
    p = process("smiley")
    p.clean()
    p.sendline(k)
    x = p.clean()
    if x:
        return True
    return False
    #print(p.clean())


for i in range(256):
    k = key_pat[:]
    k[0x16] = i
    k[0x14] = ord(")")
    key = bytes(k)
    if test_key(key):
        print(f"Possible: {i}")
        print(key.decode())
```

(and also for the other byte)

After that, I've tried all of them and used GDB to disassemble the decoded instructions, and this way I've found the only real bytes.

The decrypted programs just perform some checks on the key:
```assembly
   0x5555555580a0:      push   rbp
   0x5555555580a1:      mov    rbp,rsp
   0x5555555580a4:      mov    QWORD PTR [rbp-key_part],rdi ; -0x18
   0x5555555580a8:      movabs rax,0x298483e3285f5caf
   0x5555555580b2:      mov    QWORD PTR [rbp-DATA],rax ; -0x10
   0x5555555580b6:      mov    DWORD PTR [rbp-0x8],0xafc22f5f ; -0x8
   0x5555555580bd:      mov    DWORD PTR [rbp-COUNTER],0x0
   0x5555555580c4:      jmp    0x5555555580ef ; FOR_CHECK
   FOR_BODY
   0x5555555580c6:      mov    eax,DWORD PTR [rbp-COUNTER]
   0x5555555580c9:      movsxd rdx,eax
   0x5555555580cc:      mov    rax,QWORD PTR [rbp-key_part]
   0x5555555580d0:      add    rax,rdx 
   0x5555555580d3:      movzx  edx,BYTE PTR [rax] ; KEY_PART[COUNTER]
   0x5555555580d6:      mov    eax,DWORD PTR [rbp-COUNTER]
   0x5555555580d9:      cdqe
   0x5555555580db:      movzx  eax,BYTE PTR [rbp+rax*1-DATA] ; DATA[COUNTER]
   0x5555555580e0:      cmp    dl,al
   0x5555555580e2:      je     0x5555555580eb $ FOR_CHECK
   NOT_EQ
   0x5555555580e4:      mov    eax,0x0
   0x5555555580e9:      jmp    0x5555555580fa ; RET
   FOR_INCREMENT
   0x5555555580eb:      add    DWORD PTR [rbp-COUNTER],0x1
   FOR_CHECK
   0x5555555580ef:      cmp    DWORD PTR [rbp-COUNTER],0xb
   0x5555555580f3:      jle    0x5555555580c6 ; FOR_BODY
   FOR_END
   0x5555555580f5:      mov    eax,0x1
   RET
   0x5555555580fa:      pop    rbp
   0x5555555580fb:      ret
```

```assembly
0x555555558100:      push   rbp
0x555555558101:      mov    rbp,rsp
0x555555558104:      mov    QWORD PTR [rbp-KEY_PART],rdi ; -0x18
0x555555558108:      mov    DWORD PTR [rbp-0x7],0xb0835528
0x55555555810f:      mov    WORD PTR [rbp-0x3],0x4bd7
0x555555558115:      mov    BYTE PTR [rbp-0x1],0x74
0x555555558119:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555811d:      movzx  edx,BYTE PTR [rax]
0x555555558120:      movzx  eax,BYTE PTR [rbp-0x7]
0x555555558124:      cmp    dl,al ; KEY_PART [0] == DATA[0] = 0x28
0x555555558126:      je     0x555555558132

0x555555558128:      mov    eax,0x0
0x55555555812d:      jmp    0x5555555582eb ; RET 0

0x555555558132:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558136:      movzx  eax,BYTE PTR [rax]
0x555555558139:      movsx  edx,al ; KEY_PART[0]
0x55555555813c:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558140:      add    rax,0x1
0x555555558144:      movzx  eax,BYTE PTR [rax]
0x555555558147:      movsx  eax,al
0x55555555814a:      add    edx,eax ; KEY_PART[0] + KEY_PART[1]
0x55555555814c:      movzx  eax,BYTE PTR [rbp-0x6] ; DATA[1] = 0x55
0x555555558150:      movsx  eax,al
0x555555558153:      cmp    edx,eax ; 0x55-0x28 -> 0x2d
0x555555558155:      je     0x555555558161

0x555555558157:      mov    eax,0x0
0x55555555815c:      jmp    0x5555555582eb ; RET 0

0x555555558161:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558165:      movzx  eax,BYTE PTR [rax]
0x555555558168:      mov    edx,eax ; KEY_PART[0]
0x55555555816a:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555816e:      add    rax,0x1
0x555555558172:      movzx  eax,BYTE PTR [rax]
0x555555558175:      add    edx,eax ; KEY_PART[0] + KEY_PART[1]
0x555555558177:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555817b:      add    rax,0x2
0x55555555817f:      movzx  eax,BYTE PTR [rax]
0x555555558182:      add    eax,edx ; KEY_PART[0] + KEY_PART[1] + KEY_PART[2]
0x555555558184:      movzx  edx,BYTE PTR [rbp-0x5] ; DATA[3] = 0x83
0x555555558188:      cmp    al,dl ; 0x83 - 0x55 = 0x2e
0x55555555818a:      je     0x555555558196

0x55555555818c:      mov    eax,0x0
0x555555558191:      jmp    0x5555555582eb ; RET 0

0x555555558196:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555819a:      movzx  eax,BYTE PTR [rax]
0x55555555819d:      mov    edx,eax
0x55555555819f:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581a3:      add    rax,0x1
0x5555555581a7:      movzx  eax,BYTE PTR [rax]
0x5555555581aa:      add    edx,eax
0x5555555581ac:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581b0:      add    rax,0x2
0x5555555581b4:      movzx  eax,BYTE PTR [rax]
0x5555555581b7:      add    edx,eax
0x5555555581b9:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581bd:      add    rax,0x3
0x5555555581c1:      movzx  eax,BYTE PTR [rax]
0x5555555581c4:      add    eax,edx
0x5555555581c6:      movzx  edx,BYTE PTR [rbp-0x4]
0x5555555581ca:      cmp    al,dl
0x5555555581cc:      je     0x5555555581d8

0x5555555581ce:      mov    eax,0x0
0x5555555581d3:      jmp    0x5555555582eb ; RET 0

0x5555555581d8:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581dc:      movzx  eax,BYTE PTR [rax]
0x5555555581df:      mov    edx,eax
0x5555555581e1:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581e5:      add    rax,0x1
0x5555555581e9:      movzx  eax,BYTE PTR [rax]
0x5555555581ec:      add    edx,eax
0x5555555581ee:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581f2:      add    rax,0x2
0x5555555581f6:      movzx  eax,BYTE PTR [rax]
0x5555555581f9:      add    edx,eax
0x5555555581fb:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555581ff:      add    rax,0x3
0x555555558203:      movzx  eax,BYTE PTR [rax]
0x555555558206:      add    edx,eax
0x555555558208:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555820c:      add    rax,0x4
0x555555558210:      movzx  eax,BYTE PTR [rax]
0x555555558213:      add    eax,edx
0x555555558215:      movzx  edx,BYTE PTR [rbp-0x3]
0x555555558219:      cmp    al,dl
0x55555555821b:      je     0x555555558227

0x55555555821d:      mov    eax,0x0
0x555555558222:      jmp    0x5555555582eb ; RET 0

0x555555558227:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555822b:      movzx  eax,BYTE PTR [rax]
0x55555555822e:      mov    edx,eax
0x555555558230:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558234:      add    rax,0x1
0x555555558238:      movzx  eax,BYTE PTR [rax]
0x55555555823b:      add    edx,eax
0x55555555823d:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558241:      add    rax,0x2
0x555555558245:      movzx  eax,BYTE PTR [rax]
0x555555558248:      add    edx,eax
0x55555555824a:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555824e:      add    rax,0x3
0x555555558252:      movzx  eax,BYTE PTR [rax]
0x555555558255:      add    edx,eax
0x555555558257:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555825b:      add    rax,0x4
0x55555555825f:      movzx  eax,BYTE PTR [rax]
0x555555558262:      add    edx,eax
0x555555558264:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558268:      add    rax,0x5
0x55555555826c:      movzx  eax,BYTE PTR [rax]
0x55555555826f:      add    eax,edx
0x555555558271:      movzx  edx,BYTE PTR [rbp-0x2]
0x555555558275:      cmp    al,dl
0x555555558277:      je     0x555555558280

0x555555558279:      mov    eax,0x0
0x55555555827e:      jmp    0x5555555582eb ; RET 0

0x555555558280:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x555555558284:      movzx  eax,BYTE PTR [rax]
0x555555558287:      mov    edx,eax
0x555555558289:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555828d:      add    rax,0x1
0x555555558291:      movzx  eax,BYTE PTR [rax]
0x555555558294:      add    edx,eax
0x555555558296:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x55555555829a:      add    rax,0x2
0x55555555829e:      movzx  eax,BYTE PTR [rax]
0x5555555582a1:      add    edx,eax
0x5555555582a3:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555582a7:      add    rax,0x3
0x5555555582ab:      movzx  eax,BYTE PTR [rax]
0x5555555582ae:      add    edx,eax
0x5555555582b0:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555582b4:      add    rax,0x4
0x5555555582b8:      movzx  eax,BYTE PTR [rax]
0x5555555582bb:      add    edx,eax
0x5555555582bd:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555582c1:      add    rax,0x5
0x5555555582c5:      movzx  eax,BYTE PTR [rax]
0x5555555582c8:      add    edx,eax
0x5555555582ca:      mov    rax,QWORD PTR [rbp-KEY_PART]
0x5555555582ce:      add    rax,0x6
0x5555555582d2:      movzx  eax,BYTE PTR [rax]
0x5555555582d5:      add    eax,edx
0x5555555582d7:      movzx  edx,BYTE PTR [rbp-0x1]
0x5555555582db:      cmp    al,dl
0x5555555582dd:      je     0x5555555582e6 ; RET_OK

0x5555555582df:      mov    eax,0x0
0x5555555582e4:      jmp    0x5555555582eb ; RET 0
RET_OK
0x5555555582e6:      mov    eax,0x1
RET
0x5555555582eb:      pop    rbp
0x5555555582ec:      ret
```

(commented and formatted it a bit)

I've decided to just use `z3` to make the key. Totally unnecessary, but did some thinking for me and I've wanted to try it before:

```python
from z3 import *


s = Solver()
key = [BitVec(f"key[{i}]",8) for i in range(44)]

for i in key:
    s.add(i!=0)
    s.add(i!=10)


s.add(key[3]==key[16+5])
s.add(key[16+5]==key[32+3])
s.add(key[32+3]==ord(" "))

s.add(key[0]==ord("o"))
s.add(key[1]==ord("_"))
s.add(key[2]==ord("O"))

XORDATA = (0x51ED9072636CED08).to_bytes(8,"little") + (0x9972636CEDB65C56).to_bytes(8,"little")

for i in range(0x10):
    s.add(key[i+4]^key[i+5]==XORDATA[i])

# checked bytes:
s.add(key[0x14]==ord(")"))
#s.add(key[0x16]==84)
#s.add(key[0x16]==85)
s.add(key[0x16]==194)


SECOND_XOR = [29,82,116,136,226,227]
s.add(key[0x24]==SECOND_XOR[2])

CHECK1 = (0x298483e3285f5caf).to_bytes(8,"little") + (0xafc22f5f).to_bytes(4,"little")

for i, b in enumerate(CHECK1):
    s.add(key[0x17+i]==b)

CHECK2 = (0).to_bytes(1,"little") + (0xb0835528).to_bytes(4,"little") + (0x4bd7).to_bytes(2,"little") + (0x74).to_bytes(1,"little")

for i, b in enumerate(CHECK2[:-1]):
    s.add(key[0x25+i]==CHECK2[i+1]-CHECK2[i])

assert s.check()==sat

d = [0]*44
m = s.model()
for k in m:
    i = int(str(k)[4:-1])
    d[i] = m[k].as_long()
print(bytes(d))
with open("payload","wb") as f:
    f.write(bytes(d)) 
```