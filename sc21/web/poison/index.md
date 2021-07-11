---
title: "Poison for tomorrow"
layout: page
---

- Stopping the apocalypse part 5
- medium

You did it! Everything blew up. Joe is dead, the remaining Warboys ran off. Luckily the anti-apocalypse machine is unharmed. As you walk closer to the machine you see it is counting down from 999 years. Joe programmed it to delay the end of the apocalypse as much as possible. Find a way to reprogram the machine, otherwise, the apocalypse will stay for a long time.

[https://poison-for-tomorrow.secchallenge.crysys.hu](https://poison-for-tomorrow.secchallenge.crysys.hu)

_author: Pepe_

## Writeup

The page actually redirects to `https://poison-for-tomorrow.secchallenge.crysys.hu/index.php?page=countdown.html`. 

That `page` parameter just screams for attacks, so I've tried a few. I could include `/etc/passwd`, `index.php` or many other files, but could not read the contents of the later because it's parsed PHP.

I've tried a few automated `local file inclusion (LFI)` tools, and one of them found that we can include `/var/log/apache2/access.log`. It turns out that this file has our IP, time of access and useragent. Faking an useragent with chrome witch is a PHP snipped I've executed `phpinfo()`. 

Turns out most functions were disabled, but I could still do a directory listing:
```php
<? foreach(scandir(".") as $x => $x_value) {   echo "Key=" . $x . ", FILE=" . $x_value;   echo "<br>"; } ?>
```
This way I've found a secret folder named `very_secret_hidden_folder_[removed_that_so_you_wont_get_the_flag_for_free]` and could just navigate to `https://poison-for-tomorrow.secchallenge.crysys.hu/very_secret_hidden_folder_[removed_that_so_you_wont_get_the_flag_for_free]/` and see the flag.
