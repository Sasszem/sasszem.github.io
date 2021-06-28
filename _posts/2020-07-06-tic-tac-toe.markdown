---
title: Online tic-tac-toe
layout: page
category: prog
---

Online multiplayer tic-tac-toe Svelte-ben, websocket kommunikációval és Python backenddel    
(na ez már projekt név!)

Készítés ideje: 2020.06.23 22:45
- első működő teljes verzió: 2020.06.24 11:17
- azóta refaktorálás, javítgatások

[Github repó](https://github.com/sasszem/tic-tac-toe)   
[szerver github repó](https://github.com/Sasszem/heroku-ttt-server)

[Online kipróbálás](https://sasszem.github.io/tic-tac-toe/)

# Történet

## Én és a web

### HTML

Már fogalmam sincs hogy honnan tanultam meg a HTML alapjait. Talán a [Farkas Csaba](https://www.libri.hu/konyv/farkas_csaba.programozasi-ismeretek-halado-felhasznaloknak.html) könyv volt az? Időben nagyjából akkor volt, még általános alsós koromban...

Ez a könyv elég elavult volt már akkor is, pedig még annyira nem is volt régi kiadás. Persze akkoriban még nem volt éppen HTML5 vagy ennyi szép JS framework, de azért a Microsoft SharePoint-os statikus oldalakkal vetekedő notepad-os gányolások már akkor is elavultak voltak...

Mindenesetre megtanultam a nagyon alapokat, úgymint `<html></html>`, `<p>` és egyebek. A JS-ről még szó sem volt akkor, de a CSS-ről sem. Az abszolút maximum a `Kompozer` használata volt...

### JS

A legelső programozási nyelvem a JS volt. Még a közelítő dátumra sem emlékszem amikor először kértem bátyámat hogy tanítson meg "programozni", de úgy rémlik hogy még a HTML ELŐTT volt, tehát még bőven alsós koromban...

A legelső alkalommal emlékszem hogy elkezdte a kulcsszavakat sorolni, kezdve a `var`-al (ami akkor még friss és meleg volt), majd ilyen bonyolult szavakkal ijesztett el hogy

> és ezzel lehet változókat *deklarálni*

Nagyjából 5 perc után lett elegem és léptem le, igazán okos módon rázott le... 

Valamivel (hónapok? évek?) később újra megkértem hogy tanítson, és ekkor már leült velem rendesen dolgozni. A nyelv amit tanított, a JS volt. A HTML már ment eléggé, így volt mire építeni. 

A legelső programom egy csodálatos weblap volt rajta egy gombbal, amit ha megnyomtál, a rajta levő szám eggyel megnőtt...

A második programom egy saját készítésű számológép volt, ami tudott összeadni, kivonni, szorozni és osztani is. Persze semmi fogalma sem volt a műveleti sorrendről, de elég jól modellezte az olcsóbb számológépek működését.

A JS-el végül írtam egyszer egy csodálatos generátorprogramot, ami "interaktív" teszteket generált - ilyen mondatból kihagyott szó jellegűeket. Beírtam hogy mi legyen a mondat eleje, mi a helyes válasz, és mi legyen a mondat vége. Csakis fix számú kérdést lehetett megadni, de több sablon volt (talán 5-10-15 kérdéses?). A program több lépésben kérdezte meg a beírandó adatokat, majd a legvégső lépésben kaptuk meg a generált HTML-t beágyazott JS-el. Ekkor még talán nem is volt lehetséges JS-ből file-t menteni, főleg nem az általam használt ősrégi IE-ben, így a kimenetet ki kellett másolni és kézzel beírni egy file-ba...

A JS-el sokkal többet akkor nem foglalkoztam, elkezdtem egy (ha lehet még elavultabb) könyvből `Turbo Pascal`-t tanulni, míg végül bátyám szerzett nekem egy Python-könyvet. 

A webbel azóta nem sokat foglalkoztam, főként hogy akárhányszor megpróbáltam, mindig rövid úton agygörcsöt kaptam a CSS-től, de láttam hogy igen gyorsan fejlődik és valószínűleg érdemes foglalkoznom vele.

## Én és az Angular

A sulink honlapjának újratervezésébe fogtunk bele páran 10. osztály környékén. Kicsit kevesebben lettünk mint eredetileg terveztük, és ennek megfelelően nem is annyira haladt a dolog.

A két fő technológia a `Laravel` (PHP, backend) és `Angular`(TS, frontend) volt. Rögtön lecsaptam a backendre, a szükséges `Laravel` tudást egy hét alatt felszedtem, majd elkezdtem JSON API-kat írni. 

A backend sokkal gyorsabban elkészült használható állapotra mint a frontend, így kis idő múlva elkezdtem tanulni azt is, kezdve a `freecodecamp.com`-os anyagokkal, majd folytatva a TS-t és az Angular-t. 

Nem tudom hogy magában az Angular-tól vagy az általunk használt többi dologtól (a "főni" szeret mindent túlbonyolítani ha cserébe beleviheti a legújabb / google által is használt technológiát), de igencsak hamar tettem egy 180°-os fordulatot és azóta sem vagyok hajlandó egy betűt is hozzáírni ahhoz a frontendhez.

Az angular ahogy látom ténylegesen "enterprise ready", azaz bonyolultságban vetekszik az NCC-1701-el. Ha enterprise FizzBuzz-t akarnék írni akkor biztosan #1 lenne az Angular, de a saját hobbiprojektjeimhez biztosan nem használnám.

## Én és a Svelte

A Svelte-ről először egy YouTube-os videóból hallottam: [Rethinking Reactivity](https://www.youtube.com/watch?v=AdNJ3fydeao). Alapvetően Rich Harris egy fél órán át promózza a saját framework-jét, és azt állítja hogy mindenki más rosszul csinálja a sajátját. Baromi meggyőző, annyit tudok csak mondani.

A prezentáció baromi jó reklám lett, amióta csak láttam megint le akartam ülni "webezni" - de még mindig egy kicsit visszatartott a CSS, illetve nem akartam újabb projektbe kezdeni, hanem a változatosság kedvéért be is akartam fejezni valamit...

# Alapötlet

Az alapötletet az adta, hogy valahol olvastam egy másik szintén csodálatos (bár nem ennyire új) webes technológiáról - a websocketekről. Gondoltam csinálhatnék vele valamilyen játékot - de valami egyszerűvel kéne kezdeni. A legegyszerűbb multiplayer játék (a kő-papír-olló után) pedig a tic-tac-toe...

Ha már játék, akkor csináljuk rendesen - legyen lobby, győzelem / vereség és persze legyen biztonságos, azaz ne lehessen csalni, akár a JS kód módosításával se lehessen a szervert átverni.

A websocket-nek egy hátránya van: amíg a svelte-s oldalt bármilyen statikus hostingon el lehet helyezni (pl. github.io), addig a websocketeknek kell egy szerver és egy szerverprogram. Úgy döntöttem viszont hogy kipróbálom a Banana Pi-met mint szervert. 

# Működés

## Frontend

Baromi egyszerű.

A játék állapotától függően váltogatok többféle svelte komponenst, pl. a név beírós képernyőt, a lobby-t vagy a játékot.

A gombokra való kattintás a store-on keresztül üzenetet küld a websocketen, míg bejövő üzenet esetén frissítjük a lokális állapotot.

A legtöbb időm a CSS-el ment el, főleg a lobby-nál a vízszintesen oldalra és függőlegesen középre igazított elemekkel. Ezúton is köszönöm a tippet a W3Schools-nak hogy használjak `float`-ot, de még inkább haveromnak hogy használjak `flexbox`-ot és hagyjam a W3S-t a fenébe.

## Backend

Python alapon kezdtem neki a szervernek, a [websockets könyvtárral](https://websockets.readthedocs.io/en/stable/intro.html).

A könyvtár `asyncio`-s (`async`/`await`-os) async módon működik, amely gyakorlatilag coroutine-okat használ és könnyen kezelhetően fut "több szálon". Eddig még nem nagyon írtam ilyen python programot, de nem volt túl nehéz a példákat kissé átalakítani és arra építeni.

A szerver üzeneteket vár a klienstől, állapottól függően reagál a különböző típusúakra, módosítja a helyi állapotot majd elküldi a kliensnek, adott esetben akár minden kliensnek. Nem egy nagyon összetett program, bár az első működő verzió elég csúnyán nézett ki, így az egyik első dolgom volt refaktorálni.

### Banana Pi

A szerver gyönyörűen futott a saját gépemen, de sajnos a Banana Pi-men el sem indult, mivel azon még csak Python 3.4 volt. 

A kód egy részét át tudtam írni hogy kompatibilis legyen vele, de sajnos a `websockets` könyvtárnak csak egy régi verziója elérhető itt, és nekem újabb kellett.

Raspbian-ra nem elérhető újabb verzió, de a banana pi-ra még a legújabb `raspbian`  sem elérhető sajnos. Nem maradt más választásom mint forráskódból fordítani a Python-t. Nem volt igazándiból nehéz, csak sokat kellett várni, de nyugodtan lehetett közben mást csinálni.

Amint a szerver működött, a routeremen beállítottam egy port-továbbítást rá, és frissítettem a DDNS-em is. Feldobtam egy `nginx`-et a frontend hostolására is.

#### Frissítés - 2021.01.19.

A szervert áthelyeztem Heroku-ra, leginkább azért hogy kipróbáljam hogy azt hogyan kell.
[Új repó a szerverprogramnak](https://github.com/Sasszem/heroku-ttt-server)

# Konklúzió

A mikroprojekt során megtanultam a Svelte és a WebSocket-ek alapjait, de persze még sokkal jobban el lehet mélyedni mindkettőben.

Az egész leginkább egy "csináljunk valamit ezzel a technológiával" projekt volt. Általában én fordítva indulok el, a célhoz választom a technológiát, és utána kezdek ismerkedésből hasonlókat csinálni, de itt nem volt hosszútávú célom.

Sikerült egy kicsit CSS-ben is dolgoznom és csak közepes méretű agybajt kaptam az igazításoktól, de látom hogy a flexbox és a grid sok mindent megold amivel korábban bajom volt.

De az is biztos hogy ha a jelenlegi egyszerű honlapot le akarom cserélni, akkor Svelte alapon kezdek neki az újnak.

(frissítés: inkább kihagyom, ez a `Jekyll` egészen jó, és végre elolvastam a dokumentációt is, nem kell sajátot fejlesztenem - 2021.06.28)