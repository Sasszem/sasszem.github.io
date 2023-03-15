---
title: "Hello Kitty"
layout: page
---

Just a rootkit

- Firmware
- Forensics
- Malware analysis
- Medium

Writeup by `KosmX`

# Description and resources

## Mission brief

In this challenge, you have to find which function the malware modified to hide your files

## Instructions

You've just realized that your brand new smart TV cannot locate your favorite movies anymore since you browsed a pirate site last week. It's getting more and more embarrassing as many recorded family events seem to be lost also.

Fortunately, you are hands-on enough and figured out how to create a memory snapshot from your device that you need to analyze now. Your instincts drives you forward and suspect that a malicious operation lies in the background.

**Your task is to submit the name of the function the malware modified to hide your files. Please pick the one which comes without numbers.**

Good luck!

---

# Writeup

**This challenge happens in an SSH server**

On the server there were 2 directories. One with a 4GB memory snapshot, the other with [Volatility tool](https://www.volatilityfoundation.org/)
Every file was too large, and the connection was limited. It has to be done on the server.

Figuring out, what the heck is volatility and how to use it was not trivial.
It is designed against Windows, it could not recognize the image.
After some searching, I've found out, if I want to use it against linux, I have to use different commands...
 `linux_pslist` instead of `pslist`.

After that, we found the bash history in the memory snapshot.
Apparently, they installed [m0nad/Diamorphine](https://github.com/m0nad/Diamorphine), an open-source rootkit.
We all had to read it's README multiple times, to find out, it **can** hide files.

Then *wat* function. Linux uses syscalls. (what are technically C functions)
[Here is the line](https://github.com/m0nad/Diamorphine/blob/898810523aa2033f582a4a5903ffe453334044f9/diamorphine.c#L413), where it redirects the original function: `__NR_getdents`

The solution was `getdents`   
(most likely stands for "get directory entries")