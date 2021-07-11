---
title: "Escape the chains"
layout: page
---

- Stopping the apocalypse part 1 
- easy

As you wake up, the first thing you notice is a headache. The second one is that you are in the back of a vehicle you do not remember entering. You hear unfamiliar voices outside. Something about an "important device" and "the apocalypse". While it sounds fairly interesting, you can't make out the details.

Sitting up, you notice something on your legs. No one seems to be around, so You are free to take a closer look. It looks like a fancy cuff. On the device, You notice what appears to be a connector, labeled UART...

[https://escape-the-chains.secchallenge.crysys.hu](https://escape-the-chains.secchallenge.crysys.hu)

Note: If you believe to have successfully connected, but receive no feedback from the device, you might want to ask it to help you.

author: Wintermute, Csf3r3ncz1

## Writeup

Simply the most annoying HW challenge, at least for me. We were given a fake linux shell `user@banana-tau` (obvious Raspberry Pi reference), and had to "connect" to a serial device using UART.

You know what I did not notice the first 5 or so times when I've attempted this? A button on the upper-right corner where I can "connect" the wires. Who might have guessed that this works best when plugged in?

Anyways, connecting UART is easy: `RX` to `TX` and vica versa (as you want to receive what the other transmits, and also the other way around). Also `GND` goes to `GND`.

A few commands actually worked on the terminal, namely `ls /bin/` told us we have `id` (useless), `ls` (mostly useless), `lsusb` and `ttycon`.

`lsusb` tells us there's an USB-UART converter connected and it's available at `/dev/ttyUSB0` (could have guessed that as I've used those things before).

`ttycon` asks for a device and also some parameters, namely `baudrate`, `databits`, `parity bit` and `stopbits`.

Guessing them is a bit boring, but fortunately it was mostly the normal stuff (8 data bits, 1 stop bit, no parity) and the baud rate was 115200, witch is a common one. 

Command: `ttycon -baud-rate 115200 -data-bits 8 -parity-bit none -stop-bits 1 /dev/ttyUSB0`

After that, typing `help` told me that:
```
available commands: check-updates, factory-reset, help, system-info
```

Trying all of them resulted in `factory-reset` printing the flag, and also unlocking the chains on my leg...