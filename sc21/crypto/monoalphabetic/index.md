---
title: "Monoalphabetic MadMax"
layout: page
---

- easy

You love it, you hate it, it doesn't matter this is monoalphabetic.

_author: Suma_

Attached file:
- [enc.txt](enc.txt)

# Writeup

It was clear that it's just a [monoalphabetic cipher or fixed substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution) - so every letter is replaced by another one based on a fix alphabet.

I've never broken one of those before, but they are not hard if the ciphertext is long enough - and this one is.

I've worked in a way that every decoded letter is uppercase, it was easier for me to distinguish them from unknown ones.

One mistake I've nearly made was search-replacing - but that might have replaced already-replaced letters, so I've wrote a python script that goes letter by letter.

I've ran a few statistics on it and calculated letter frequencies. Based on the english letter frequencies I've found that `G` codes `E`. Based on that and the 3-letter groups I've also identified `X` as `T` and `W` as `H`.

I've also found `T` is `S` from `'s`. 

Next I've guessed `C` as `A` from frequency, and found `sAST` and guessed it as `LAST`, so `S` is `L` - also `O` is `I` from `is`.

I've found `SHApES HIS HEAa` - clearly meant to be `shakes his head`.

I've continued to guess letters based on words, until I've had a full decoded sentence and could google that - and found that I'm decoding `Mad Max 2: The Road Warrior`'s script ([link](http://www.scifiscripts.com/scripts/madmax2.txt)).

Based on that, I was able to decode ALL letters and get the flag inserted in the document.