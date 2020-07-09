# Sweep-r 

Egyszerű svelte-s aknakereső

Linkek:
- [github repó](https://github.com/sasszem/sweep-r/)
- [kipróbálás](https://sasszem.github.io/sweep-r/)

[Vissza](prog.md)

## Rövid történet

Az aknakereső egyike azon baromi addiktív játékoknak amivel órákat tudok játszani akárhányszor leülök programozni. Néha viszont a hajamat tépem, mivel gyakran előfordulnak olyan helyzetek amikor konkrétan nem lehetséges eldönteni hogy két négyzet közül melyik akna... Elgondolkoztam hogy lehetséges lenne-e egy olyan aknakeresőt írni amelyben nem fordul elő ilyen helyzet, de először úgy döntöttem hogy írok egy hagyományost, aztán próbálkozom tovább.

## Tech

Megjelenítésre webes technológiát akartam, és az előző projekt után itt is a svelte-t választottam. Az egyetlen további extra a typescript beemelése amely feltehetőleg segít majd kiszűrni a primitív hibákat, de ugye azokat *úgyse fogom elkövetni*...

AZ egyik utolsó módosítás egy `CD workflow` beállítása lett, azaz a `master`-ra pusholt commit-ok alapján automatikusan legyártja a honlapot és commit-olja a `gh-pages`-re.

## Állás

Nagyrészt készen van - semmi extrát nem tartalmaz, csak egy automata segítő algoritmust, amely az egyszerűbb egyértelmű helyzetek alapján sok esetben az egész játékot meg tudja oldani nekünk. 

A megoldó működése két egyszerű lépésből áll: 

- ha egy négyzet körül pontosan annyi felderítettelen négyzet van ahány akna hiányzik, megjelöli őket
- ha egy négyzet körül pontosan annyi zászló van mint amennyi rá van írva, a maradékot felderíti

Ezt a két lépést addig ismétli amíg elér bármilyen változást velük. Összetettebb esetekre nem nagyon használ, de az egyszerűbbeken segít, és a gondolkodást hagyja meg nekünk - meg persze az elkerülhetetlen tippelgetést...

[Vissza](prog.md)