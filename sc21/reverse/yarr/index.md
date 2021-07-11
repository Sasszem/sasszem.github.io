---
title: "Celestial Yarr Harr Harr"
layout: page
---

[B] Josh, I also found an old cartridge in the treatment facility. Apparently, WaterWorks LLC was not just about cleansing, they were developing games on the side.

[J] What kind of cartridge?

[B] I don't know what kind, it looks ancient! Never seen anything like it. According to their market analysis, people love retro games but it's really hard to sell due to emulators and roms being widely available.. Rampant Piracy.

[J] What a bunch of bollocks. People pay for the games they like regardless of DRM!

[B] Whatever. The booklet mentions they made a new DRM scheme to allow retro games to rise again. I didn't see any development units of the console but at least the cartridge is intact.

[J] Can you.. connect to it somehow?

[B] Yeah, I'll try to pull a rom dump and send it over.

[J] Alright, it's my time to shine then, good work Bill.

_author: Sun G_

Attached file:
- [yarr](yarr)

## Writeup

This challenge was not too hard, maybe _Sun G_ was sick when he made it...

It turns out that the file is a GBA rom image. It boots up to a screen with ear-piercing music and a text telling us that we are pirates.

For tooling, I've tried different emulators, `Virtualboy Advance`, `Bizhawk`, `VBA-SDL`... None of them is perfect when it gets to debugging sadly...

The game itself is a modded version of Celeste, [and the source code is also alaviable](https://github.com/JeffRuLz/Celeste-Classic-GBA) (but I did not use it on the first day of my work)

I've installed [GBA loader for Ghidra](https://github.com/SiD3W4y/GhidraGBA).

Searching for the strings in Ghidra led me to a single-byte flag witch determines if I'm a pirate or not. Setting it in Bizhawk got me through, and the game is actually quite good. With some RAM-searching cheats (Bizhawk got a built-in Cheat-engine) I've given myself infinite air-dashes and got to a point where the whole game just crashes.

VBA-SDL revealed that there was an unsopported syscall - 0xd. It turns out to be a BIOS hash check, and it is used to set the piracy flag. I've reversed that part and determined witch hash should it be - `0x13371337` (not even close to the standard ones...)

It's easy to fake that after the syscalls with Bizhawk's LUA api:
```lua
local function set_bios_hash() 
	print("Bios hash quaried!")
	emu.setregister("R0",0x13371337)
end

event.onmemoryexecute(set_bios_hash, 0x08004870) -- piracy flag
```
But still, it crashes when trying to draw the message on room (3, 1).

Using the source, it is mostly trivial to identify the functions, and we can actually find some of the differences:
- in `_draw`, when drawing title, we print the piracy text if the flag is set
- the setting of the piracy flag
- `message_draw` is changed a lot - it checks for room (3,1) (memorial site) and level 30 (summit)

I've tried hard to debug the crash, but I could not. I've just decided to try to skip it.

I've focused on `message_draw`. It turns out it prints 2 different messages depending on the level, decrypting it with two values derived from the hash - so I've used the same bypass on them:
```lua
event.onmemoryexecute(set_bios_hash, 0x08004262) -- message_draw
event.onmemoryexecute(set_bios_hash, 0x08004060) -- message_draw
```

And after overwriting the LEVEL variable with Bizhawk's tools, I could just go to the hilltop and the flag was given as a text...


