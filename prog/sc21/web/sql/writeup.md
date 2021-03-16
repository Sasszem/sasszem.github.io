# SQpLosIon

- Stopping the apocalypse part 4 
- easy

A manual? Coordinates?

Damn. Joe maybe already possess an anti-apocalypse machine. What is he up to? You have to get there before him.

You head out, but as you get close to the marked location, you see Joe his Warboys, and multiple war rigs. You need to access the controller of the war rigs remotely and blow them up. Hurry up the fate of the wastes is in your hands.

https://sqlplosion.secchallenge.crysys.hu

author: Pepe

## Investigation

The webpage is a simple login page with a field for username and password. The name is a direct hint on SQL injections, so I've tried a few common ones, and `' or 1=1#` got me in as `NUX`, but still unprivileged to see the flag.

Tried `UNION` injections with different number of results, and `' UNION SELECT 1,2,3,4 #` got me as user "2" - so there are 4 results. Just tried `' UNION SELECT true, 2, true, true #` and `"admin", 2,"admin","admin"`, and the later one got me in with access to the flag.