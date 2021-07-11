---
title: "Guidance to Salvation"
layout: page
---
- medium

You have to go through several labyrinths to find salvation. Or there might be a shortcut?

`nc challenges.crysys.hu 5007`

Hint: look for the `unsafe` keyword.

_author: nemarci_

Attached file: 
- [guidance_to_salvation.tar.zst](guidance_to_salvation.tar.zst)

## Writeup

Uncompressing the archive, we can see the full Rust source code of the challenge.

It seems it generates a few random 64 bit numbers, expects us to XOR them 2 bits at a time to make them zero, then if all are zero, we get the flag.

Of course, that is unlikely to happen. If we follow the hint, and look for the `unsafe` keyword, we can only see one use:
```rust
fn challenge() {
    let mut labyrinths: [u64; LABYRINTH_COUNT] = [0; LABYRINTH_COUNT];
    labyrinths.iter_mut().for_each(|lab| *lab = rand::random());
    // println!("{:#x?}", labyrinths);
    loop {
        println!("Please make a choice: ");
        println!("1: Solve a labyrinth");
        println!("2: Check solution");
        let line = prompt_and_read("Choice: ");
        match line.trim().parse::<u8>() {
            Ok(1) => {
                let lab_index = get_labyrinth_index();
                // We already checked that the index is inbounds in `get_labyrinth_index`
                // We gain some performance if we omit the bounds check here
                let labyrinth = unsafe { labyrinths.get_unchecked_mut(lab_index) };
                solve_labyrinth(labyrinth);
            }
            Ok(2) => break,
            _ => println!("Invalid choice"),
        }
    }
    if check_solution(&labyrinths) {
        salvation()
    } else {
        println!("WRONG");
    }
} 
```
So if we can make `get_labyrinth_index()` return a wrong index, we can write (well, XOR) any value on the stack, ignoring the check.

`get_labyrinth_index()` looks very safe:
```rust
fn get_labyrinth_index() -> usize {
    let mut i = None;
    loop {
        let line = prompt_and_read("Give me an index: ");
        if let Ok(index) = line.trim_end().parse::<usize>() {
            i = Some(index);
            if index >= LABYRINTH_COUNT {
                println!("Please give me a number less than {}", LABYRINTH_COUNT);
                continue;
            }
        } else {
            println!("Please give me a number");
        }

        if let Some(i) = i {
            break i;
        }
    }
}
```
It took me a bit of time, but found a bug: if we enter an out-of-bounds number, `i` will be set, and next time we enter an invalid number (like some text), it will just return it.

What to XOR? I've tried many things, most of them failed. The goal is to redirect code execution to `salvation()`. 

If we just override a return pointer to it, we get a nice crash since the stack won't be aligned, and some operations just segfault in that case.

I've tried to be clever and jump to the second instruction of salvation, skipping the stack frame setup. This way it will crash badly, but only AFTER printing me the flag, so I thought I don't have to care.

Well that was not the case, if the program segfaults I won't get any result from the server, so it only works locally.

Overriding more than one value sounds impossible, so fixing the stack this way is NOT trivial. The working method was super-simple: just jump to the `call salvation` instruction, and that will do it, and at the end, `main()` will just return fine.

I've overridden the return pointer of `solve_labyrinth()` this way.

Offset in the array is `-14`, or `18446744073709551602` in unsigned.

`call salvation` is at `0x...98AB`, and `solve_labyrinth()` returns to `0x...9827` (ASLR kinda keeps things aligned, so those digits should be sort of fixed).

`0x9827 ^ 0x98ab = 0x8c = 0b10001100 -> 10 00 11 00 -> H L K L -> LKLH` needs to be entered.
