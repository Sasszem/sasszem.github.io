---
title: "Right to disappear"
layout: page
---

# Description and resources

- Authorization
- Web security
- Easy

Writeup by `Sasszem`

## Mission brief
Your task is to delete your profile from the app somehow. Note: only an admin has the necessary permission.

## Instructions
You can log in with username `john@doe.com` and password `CSa42q2#5@#$Sd`.

**IMPORTANT: DO NOT FORGET TO CLICK ON DELETE PROFILE BUTTON AFTER IT APPEARS!**

---

# Writeup

I am still not sure if we solved this or not. Only one team solved it officially, but we did manage to get to a point where we deleted the profile but the system did not take it as solved. There were also problems with the CTF platform, so it is suspected now that it did not register successful solves after the first one, but the organizers believed it was working since one team managed to do it. Nevertheless, they asked us to send out solutions to them via email and they'll see if it works.

The page we had to delete out profile from was very similar to the one at the `node rce` chall, and had the same base vulneribility, namely unsave deserialization. The goal was different now. After some looking at the code provided at that chall, I figured that the site uses `MongoDB` with the `mongoose` library.

First, our experimentation was limited, as all we have managed to do was to stop the server via `process.exit()`. After some `if-else` toying we figured that we don't have access to the `User` variable holding the ORM modell for users, nor the `mongoose` module, but we managed to get them via re-requireing `mongoose` and asking for the modell by name. After some unsuccessful quarying we found that we can write to our user (there were no other users in the database), and used that to leak some info via writing to the name. 

It turned out that there's no `isAdmin` flag, but a set of permissions. I added the `DELETE_PROFILE` permission to my user, then triggered the explit and I could in fact delete my user accout.

My RCE:
```
{"rce":"_$$ND_FUNC$$_async function() {let user = require('mongoose').model('User'); let me = await user.findOne({age: 28}); me.permissions = me.permissions+',DELETE_PROFILE';me.save();}()"}
```

After that it was mainly us banging out heads agains the wall and trying to figure out what else to do besides what they have asked for to get our points, and strongly suspecting that something is broken. In the last minutes the organizers came to the same conclusion, so we do not know yet if we solved this or not.