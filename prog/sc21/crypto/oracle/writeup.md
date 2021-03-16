# Oracle

- hard
- fixed
- fixed^2

I don't know crypto so I use this open source service to encrypt and decrypt my secrets (oracle.py). Unfortunatelly, I cannot decrypt some of my secrets, because I don't have a valid API key for the service. Luckily, I've created a network capture of my communication with this Oracle service (capture.pcapng). Can you decrypt some of them? You might be able to leak some secrets from the server too.

Your task is to find 7 secrets hidden within the communication and in the running Oracle service. Please submit all of them on my website, so I can give you a reward. Good luck!

Oracle service: nc challenges.crysys.hu 5003

My website: https://oracle.secchallenge.crysys.hu

P.S.: The secrets are in the following format: flag{.*}

Fix: It was not possible to extract one secret using the original version, the server is updated, check oracle-fixed.py!

_author: tk_

Attached files:
- [oracle.py](oracle.py)
- [capture.pcapng](capture.pcapng)
- [oracle-fixed.py](oracle-fixed.py)

## Writeup

Well this challenge was problematic! First the flag portal broke, then it turned out it was impossible to solve! Good thing one can't go crazy TWICE, because I spent so much time trying to solve the unsolvable part!

![tk.png](tk.png)

The conversation with this "service" starts by exchanging `2048 bit RSA` keys, then using those to exchange `ChaCha20` keys, then it's a simple menu of encrypting or decrypting text.

Since I did not have either RSA private keys, I had no idea of the sent or received data, so I've put it aside. After some time I've thought that maybe the RSA keys are crackable - and yes, `RsaCtfTool` could crack the key of the client in a few minutes.

With that, I could decode the `ChaCha20` key the client used for sending messages and thus see every message it sent - one of the secrets was in there.

The service offers encryption and decryption with 9 different schemes. Decryption, however requires an API key, and without it we can't see the decrypted data.

The client
- sent data to encrypt with all 9 modes
- sent data to decrypt with all 9 modes
- did NEVER send a valid API key

So it's clear that we have to crack some of the encrypted data the server refuses to decrypt for us.

The service offers these encryptions:
```
- Symmetric crypto
    - Stream ciphers
        - ARC4 (0)
        - Salsa20 (1)
    - Block ciphers
        - AES in CBC-mode (2)
        - AES in CTR-mode (3)
        - Blowfish in ECB-mode (4)
        - Blowfish in EAX-mode (5)
- Asymmetric crypto
    - PKCS OAEP with RSA 2048 (6)
    - El Gamal (7)
- Other
    - XOR (8)
```

First, `XOR` is trivial to crack: we just send a known payload, get the encrypted version, XOR it with the known plaintext and we have the key. XOR it with the unknown ciphertext and we have it's plaintext. Also, the XOR key was also a secret to find.

`ARC4` is a stream cipher, witch means it works on a similar way - it generates a bytestream from a key and XORs it with our plaintext. Since it's always the same key, the bytestream will also be the same, so we can just do the same as with the XOR.

`Salsa20` was protected against this trick, but the second fix broke that. `Salsa20` uses a random-generated nonce for each message, so the bytetreams will be different (and it also prepends the nonce to the message so we can decode it). After the fix it reused the nonce, so it could be decoded the same way.

`AES-CBC` is famous for an attack called `padding oracle`. We can tamper with the ciphertext, send it for decode, and it might or might not have valid padding. If we can leak this info then we can use it to decode the full message. Fortunately, the decryption on the server happens BEFORE the API key check, and it fails with an exception witch get caught and we know if failed. I've already had the code of such an attack from [Cryptopals challenge 17](https://cryptopals.com/sets/3/challenges/17) witch I could just reuse.

`AES-CTR` used a random nonce, and thus was unbreakable.

`Blowfish ECB` was also unbreakable.

`Blowfish EAX` was too, but also that was used to encrypt the first secret (witch we did not have to decrypt).

`PKCS OAEP with RSA 2048` I found a possible attack on it while searching for the 7th secret, but that would have needed a bazillion of messages with the server AND the publickey used, so it was unbreakable in this scenario.

`El Gamal` was an interesting one. It's another crypto based on finite field arithmetic and primes. After reading about it on [Wikipedia](https://en.wikipedia.org/wiki/ElGamal_encryption) and checking the code, I noticed that the random `y` was actually fixed! 

Searching a bit more lead me to [this crypto stackexchange post](https://crypto.stackexchange.com/questions/44021/elgamal-why-is-reusing-the-same-k-not-secure) witch explained that this causes it to be easily breakable. The equations there work in the finite field of `base-q`, but I did not know this `q` for my encryption.

The encryption with this fixed-y was done like this:
- generate `s` based on `y` (always the same)
- return `m*s % q`

We also know that `s<q` and `q` is a prime.

I've sent 1 as message so I could get `s` directly. I've then sent 2-3-... until the result was smaller that `s` times my number, so I knew it rolled over mod `q`. That meant I had a lower and upper limit for `q`, but still pretty huge. I've tried to give those and the remainder from `s*m%q` with my small known `m` to `z3` and it solved for `q` in less than a second - I have no idea how, possibly black magic.

With that, I could compute the modular inverse of `s` in `q` (python's `pow` function can do that too!) and multiply that with the unknown ciphertext in mod-`q` and get the flag.

That's 7 secrets:
- "plaintext" in the encrypted communication
- XOR
- XOR key
- Salsa20
- ARC4
- El Gamal
- AES-CBC

So I submitted them and got my flag.

I also spent a day searching for the last one (Salsa20) before they fixed it, and almost went crazy AGAIN...