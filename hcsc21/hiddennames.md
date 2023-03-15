---
title: "Hidden names"
layout: page
---

- Forensics
- Network security
- wireshark

Writeup by `KosmX`

**a leaked message from a private network**

# Mission brief

Sensitive data was leaked out of a well-firewalled network. Can you find out what got stolen?

## Instructions

A machine inside your company's network got compromised by attackers. The network had strict firewall rules around outgoing traffic, still, the attackers were able to leak some sensitive data. The network traffic of the office building is available in a PCAP file from the time of the incident. Can you figure out what exactly was stolen?

The solution is a string in a format like this:  `FLAG{XYZ123}`.

### downloadable resources:  
- a wireshark `cap` file

---

# What is going on here?

I had a little exercise in networking before.

I've downloaded wireshark (from [winget.run](https://winget.run))
Opened the file, and started looking after something weird.  
Eventually I've found the weird thing. 

There were strangely many **DNS** requests. 
Those DNS requests did TXT requests (not actively used protocol or IDK)
and asked an *external* DNS server for *internal* sites.
(Why would Google ask Cloudflare, what is google's IP?)

`X60ImfxH07o1pDHp0JUDIQc4rX6KRVHSf+QdF/uCrx6GuWW59F.avatao-challenge.com`  
something like this.  

In networking, bigger messages are often split into small (~1KB) parts.  
Those has to be re-assembled on the receiver computer.

On further inspection, these sub-domains contained invalid URL characters, like `/` but only valid Base64 characters. And there was a `=` on the last message.  

I've exported the whole history into a `csv` file, I wrote a Java code to extract and re-assemble the string, and I've got a valid Base64 string.  
(Why Java instead of Python? Because I'm way better in Java)  

But it did not contain any meaningful text.

After little thinking, I saved the binary data into a file and used `file <file>` command. It is a `JPEG` image.

![/hcsc21/hidden.jpg](/hcsc21/hidden.jpg)

Those plushie [*foxes*/*cats*] are adorable, I hope, I can win one.  

Just scan the **QR** code, and there is the flag🏁.