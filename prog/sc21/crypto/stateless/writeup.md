# Stateless

- easy

Crypto, crypto everywhere!

https://stateless.secchallenge.crysys.hu

_author: tk_

## Writeup

The webpage says 
```
A stateless webpage.
This is a crypto challenge, not a web challenge. Mind the padding.
```

The webpage has a profile where we can enter our first and last name, nickname, age, university and job. It also has a read-only `admin` checkbox.

There is also a `flag` page, but we can't access it because we are not admin.

Checking the page it actually remembers our data. I've checked the cookies and found a base64 one with gibberish inside.

My first thought was that it's encrypted with some cipher, and it actually stores our data.

I've played it a bit, and found:
- if I set my "name" to a few hundred `A`s it will get longer, and contain repeating blocks of 16 bytes
- if I enter more data incrementally, it'll be at 3 bytes when the length of the data jumps by 16 bytes

From those facts, I've concluded that it's AES-ECB encrypted with an unknown key, and there were 3 padding bytes inside.

AES-ECB is a block cipher, meaning it's processing 16 byte blocks of data at once, independently of each other - basically it's like a lookup in a pre-generated table (but no one pre-generates a 256^16 sized table).

That has one important implication: if we cut-paste or rearrange our ciphertext blocks, exactly the same will happen with the decoded message - except for the padding.

Padding is required since it's unlikely that the message we want to encrypt has an even multiple of 16 for length, so we need to pad that. The padding (`PKCS7`) for AES-ECB is simple. It appends 1-16 bytes (notice that there's no option for `no padding`) to the message to make it's length correct, and all the bytes are just the number of appended bytes, so it can be `1` or `2,2` or `3,3,3` or so on.

At this point I knew all of the above (mainly because I was doing the [the cryptopals crypto challenges
](https://cryptopals.com/) before), but still did not know what message was encoded. It sure had my data, but in what format?

I've launched a `byte-at-a-time ECB decryption` attack (Had the code for that from [Cryptopals Challenge 14](https://cryptopals.com/sets/2/challenges/14)), and found that after a key it's an `&` and the name of the next key - so it's URL-encoded!

Knowing that I've had all the info I needed for a cut-and-paste attack.
- created a 16 byte padding block (the last block of the ciphertext when it's size just jumped by 16)
- a message with the second-last block ending with `&admin=` and the next being `0` and padding
- a message with a block ending with `&age=` and the next starting with `1&university=`

Spliced the `1&university` after `&admin=` and terminated it with a padding block - and the resulting cookie gave me access to the flag.