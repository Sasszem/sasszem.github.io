# RTTT - Rust tic-tac-toe

Egyszerű egyjátékos tic-tac-toe Rust-ban

2020-07-11 - 2020-07-16

[github repó](https://github.com/sasszem/rttt)

[Vissza](prog.md)


## Rust

A Rust manapság elég népszerű programozási nyelv. Fő erőssége hogy memóriabiztos - megakadályozza a memóriaszivárgásokat és a gyakoribb többszálúsági hibákat. Elég új nyelv, erős fejlődésben van, és sokban eltér a megszokottabb nyelvektől. Nagyon ígéretes nyelv.

A Rust [dokumentációja](https://doc.rust-lang.org/book/title-page.html) igen jó. Egy nyaralás során olvastam végig, és kezdtem el írni ezt a projektet.

## RTTT

Az egyik legegyszerűbb interaktív projekt ami az eszembe jutott egy tic-tac-toe játék volt. Nem túl összetett, de ahhoz pont eléggé hogy kipróbálhassam vele a fontosabb feature-öket.

### Kód

A programkódot pár nap alatt írtam esténként, fokozatosan fejlesztgetve. Az első működő verzió után elkezdtem refaktorálni, a projektet modulokra bontva. A végén írtam egy kis dokumentációt is, bár ebben az esetben ennek annyira sok értelme nincs...

### Konklúzió

A Rust egy jól használható nyelv, amely nagyon ígéretes. A memory safety-t nem használtam ki túlzottan, de ezek nem is álltak az utamba a fejlesztés során, ami egy kicsit meglepő volt.

A Rust-ot még nem igazán tudom hogy mire fogom használni. Lehet vele könyvtárakat készíteni, sebessége kb. a C/C++-al esik egy kategóriába (bár elég friss, így még erősen ráfér az optimalizáció), natív alkalmazások készíthetők vele, és biztonságos szálkezelést biztosít. Ha nagyteljesítményű alkalmazást akarok írni, vagy olyasmit aminek nincsen külső függősége (pl. Python), akkor jó választás lehet. Grafikai alkalmazásban viszont nem túl hordozható (Android-ra *valószínűleg* nehezen fordítható), így cross-platform játékok írására mást kell választani. 

Pár projektem amiben érdemes lehet használnom:
- Raytracer
- Prog. nyelvek (kérdés hogy milyen PEG vagy LL modult találok hozzá)
- Fiz. szimulációk (SDL megjelenítés megoldható PC-re)
- Emulátorok
- 3D
(gyak. minden kivéve a játékokat, amelyeknél szeretném hogy androidon is fussanak)

A Rust egyik félig-meddig egyedi felhasználása a WASM-re való fordítással a nagyobbteljesítményű webes alkalmazások készítése. Még ezt nem próbáltam ki, de használható lehetne pl. a Sudoku-megoldó program háttereként.

Összesítve: tanultam valami talán hasznosat is a nyaraláson (hogy az elektronikai témákról amiket olvastam ne is beszéljek). 

Miért, TE mit csinálsz mikor nyaralsz, programozási nyelvek és/vagy tranzisztoros áramkörök tanulása helyett?

[Vissza](prog.md)