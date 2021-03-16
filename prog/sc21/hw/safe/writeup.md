# A safe place

- Stopping the apocalypse part 3 
- medium

V8? What did they mean by leaving V8 behind on the ACME servers? Perhaps the war boys deleted the manual? They must have a copy of it! Wait a minute... I remember that Joe has a little home made safe in his room. Maybe its in there?

You examine the safe, and there is a display on the front, a dial and two buttons. It feels like that the whole thing is made out of scrap electronics. The dial rotates like a rotary encoder, and the thing beeps as you press the buttons. You managed to take the cover off the dial and the next button. Bingo! You can see the rotary encoder and the button's connectors. You hook up your trusty logic analyzer, and wait for Joe to unlock it. After a few hours, you managed to log the signals while the safe has been opened, but it looks like the encoder is not the best quality.

Your task is to figure out the code and open the safe. The counter starts from 0. After you figure out the code, you can use the webpage to enter it on the safe, and receive the flag.

https://a-safe-place.secchallenge.crysys.hu

The webpage shall be only used for code verification and flag retrieval. Please do not try to brute force the code via the webpage, you'll not succeed

author: Csf3r3ncz1

Attached file:
- [safe_challenge.sal](safe_challenge.sal)

## Writeup

The linked page simulates a "safe" with a turn knob and 2 buttons. You have to enter 6 numbers in the range 1-100. The first button moves to the next number and the second "opens" the safe if all of them are correct.

The attached file can be opened with `Saleae Logic 2`, a logic analyzer software. Two immidiate observations:
- it's a rotary encoder with a button
- it's noisy af

I've dealt with rotary encoders before when building my own reflow soldering heat gun controller, so I knew how it works.

Basically, it's sending 2 signals every "click". If you turn it clockwise, the first will fall before the second, and the other way around counterclockwise. Just by looking at them you can't be sure witch way is witch, but it's only 2 tried in the worst case.

I've tried exporting the data into CSV and filtering that with Python but I could not get that working reliably, so I've just decided to do it by hand: I've counted the impulses in each direction, wrote them down and entered it.