---
title: Crossfire - Lövésgomb-nélküli lövöldözős játék
layout: post
---
(eredetileg 2019-2020-ban készült)

# Linkek

- [Github repó](https://github.com/sasszem/crossfire)

# A sztori

Régóta nézője vagyok a [Game Maker's toolkit](https://www.youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw) csatornának, amely különböző játékok elemzésével mutat be játéktervezési problémákat, trükköket és megoldásokat. Nagyon hasznos tippeket ismertem meg, amiket *nyilvánvalóan* használni is fogok amint saját játékot tervezek, de addig is érdekes hallani ahogy a kedvenc játékaimat dicséri, illetve egyben tippet is ad hogy mivel játsszak legközelebb.

Egy ideje évente megrendezik a "GMTK Game Jam"-et - egy verseny, ahol egy általa megadott téma köré kell játékot tervezni és készíteni 48 óra alatt. A 2018-as Jam egyik kiemelt játéka a [Crossfire nevű játék lett](https://seet.itch.io/crossfire), ami nekem annyira megtetszett hogy úgy döntöttem hogy lemásolom, főleg hogy egy ideje már szemeztem a `Löve2D` keretrendszerrel, és ez egy elég összetett projekt volt hogy alaposabban megismerjem. Végül nem igazán másolat lett az eredmény, az én játékom *nagyon* hasonló, de vannak benne új ötletek is, és persze egy sornyi kód vagy grafika sem lett átemelve.

A játék különlegessége hogy bár egy lövöldözős jellegű játék, de a játékos nem tud lőni. Az ellenfelek lőnek a játékosra, aki a lövedékeket kerülgeti, és ha jól taktikázik, az őt körbevevő ellenfelek egymást találják el.

Míg az eredeti játék 48 óra alatt készült el (azt hiszem valami GameMaker-ben), addig az enyém kb. egy év alatt. Ennek számos oka van amit még részletesebben kifejtek...

# Tervezés

A projekt átment pár újratervezési fázison. Ami végig megmaradt:

- [Löve2D](https://love2d.org) keretrendszer
- [nata](https://github.com/tesselode/nata) `ECS-keretrendszer`

Volt még a rendszerben `Moonscript` is, a végén pedig bekerült a `flux` és a `yalg` is.

## Moonscript

Az elején [Moonscript](https://moonscript.org)-ben kezdtem dolgozni (egy olyan nyelv ami Lua-ra fordul), amit a segédeszközök majdnem teljes hiánya miatt végül feladtam, főleg hogy átírni mindent Lua-ra nem is volt olyan nagy munka, tehát sokat nem is spórolt nekem.

A Moonscript tud segíteni ha Lua-ban OOP kódot akarunk írni (a Lua-ban ez nem is olyan könnyű!), meg segít javítani pár furcsaságot - mint például a ternary operátor hiánya, a `~=` az `==` helyett, vagy az in-place `+` vagy `-` hiánya.

## ECS-lib

Az `ECS` az `Entity-Component-System` rövidítése. A lényege, hogy a játékot 3 dologból építjük fel: `szereplők`ből (entity), `komponensekből` és `rendszerek`ből (system)

A `szereplők` (nagyrészt) `komponensek`ből épülnek fel, amelyek egy-egy tulajdonságot hordoznak. Például az én játékomban van egy `CollisionComponent`, amely egy szereplő "ütközési dobozának" (amely egy kör) a sugarát tárolja.

A `rendszer`ek általában nem `szereplő`-típusonként működnek, hanem `komponensek`en - például nálam a `CollisionSystem` minden olyan szereplőn dolgozik akinek van `CollisionComponent`-je. 

A `rendszer`ek `esemény`ek-re reagálnak, néha új `esemény`ek küldésével. Az `esemény`ek tartalmazhatnak plusz adatot is. Nálam például van `update(dt)`, `collision(ki, kivel)`, vagy `enemyHit(enemy)` esemény.

A `nata` az ilyen `rendszer`ek és `szereplő`k összerendezésében segít, és az egész projekt gerincét adja így.

## Paradigma

Manapság úgy tűnik dúl az `OOP` vs `functional` háború - meg úgy általában az arról való vita hogy mi a legjobb programtervezési módszertan. A mostani divat az `agilis` fejlesztés, de a cél a `TDD` és persze a `DOD (Data Oriented Design)` (amihez amúgy közelít az `ECS`).

A projektet először full-`OOP`-ban kezdtem amit a Moonscript támogatott. Egy idő után elkezdtem `funkcionális`ra átírni mindent (amit lehetett és még egy-két dolgot), majd rájöttem hogy ez miért is hülyeség (sokkal rondább lett pár dolog), és végül visszatértem az `OOP`-hez.

Megjegyzem hogy a `nata` a rendszereket teljesen OOP módon kezeli, akárcsak a `szereplő`ket. Persze a Lua-s `OOP` modell baromi képlékeny, egy `tábla` (`szótár`, `hashmap`, `kulcs->érték gyűjtemény`, vagy hívd ahogy akarod) is nyugodtan lehet osztálypéldány ha belerakunk adatok és/vagy függvényeket, így elég elmosódott a határ...

Mindazonáltal jóval több időm ment el oda-vissza refaktorálásra mint kellett volna...

## Feladatkezelés

Nagyobb programokat általában kisebb feladatok(`issue`, `task`, stb. ) formájában valósítják meg. Ezek típus szerint általában lehetnek `feature`-ök vagy `bug`-ok.

Az egyes `issue`-kat szokás csoportokba rendezni. Ennek hogyanja változó, a logikailag összetartozó `feature`-ök azonban logikus hogy együtt készüljenek el, de szokás még hetente kiválasztani hogy az adott héten mit csinál meg a csapat (sprint).

Az `issue`-kat általában címkékkel is ellátják, illetve kijelölnek egy felelőst aki azt megcsinálja.

Git alapú verziókezelésnél szokás minden `issue`-t külön `branch`-en fejleszteni, majd minden `issue`-hez egy `PR`-t (`pull request`) készíteni. Ez segít elkülöníteni a dolgokat egymástól, bár kisebb `issue`-k esetében több munka tud lenni mint megcsinálni a feladatot.

Bár az én projektem nem túl nagy, de igyekeztem hasonlóan eljárni, elég sok (bár nem minden) részét kihasználva a Github eszköztárának. Voltak `issue`-im, majdnem minden `issue`-ra külön `PR`-jeim, mérföldköveim (`milestone`), kanban táblám...

Mindemellett próbálkoztam írni unit testeket (mondjuk a véletlenszerű tesztgenerálás azt jelentette hogy gyakran a teszt és a tesztelt kód megegyezett, illetve kiderült hogy a floating-point műveleteknél elég viccesen lehet csak tesztelni...), ez alapján megpróbáltam bevezetni egy automata tesztelést `PR` előtt (`CI` - continuous integration), ami nem engedi `mergelni` a `PR`-t amíg minden teszt hibátlan nem lesz.

A `CI`-be próbáltam még beilleszteni egy `code coverage` tesztet is, ami a tesztek alapján ellenőrzi hogy minden sor kódom lefutott-e legalább egyszer, tehát minden elágazás minden esete le van-e fedve valamely teszt által. Ezt még a `Moonscript`-el próbáltam, és elég szépen felsült, mivel semmilyen coverage tool nem viselte el ezt a nyelvet, még a nyelvbe épített sem!

Összefoglalva: jó volt játszani a hű-de-professzionális fejlesztőt, de többször állt az utamba mint segített, illetve megfelelő eszközök nélkül van amit konkrétan nem lehet megoldani...
Más projektnél még valószínűleg fogok ilyet csinálni, de itt nem sok értelme volt - az egész nagyon erősen összetett interakciókra épül, és nem olyan sok minden tesztelhető automatikusan.

## Projekt felbontás

Az egész projektet a leginkább az lassította le hogy próbáltam mindent a lehető legszebben és legelegánsabban megoldani.

Rájöttem közben a tökéletes és teljesen hibamentes program megírásának egyetlen módjára:

> Annyit kell azon filozofálni hogy hogy lenne a program tökéletes, hogy egy fél sor kódot sem írunk...

Ráadásképpen hozzátenném hogy ha 8 órát gondolkodunk azon hogy hogy lehetne szépen megírni valamit, majd leülünk megírni, 5 perc alatt olyan problémákat és szépséghibákat találunk amik további 8 óra gondolkodás alatt sem jutottak volna az eszünkbe. **Jobb leülni, megírni csúnyán, és utána keresni hogy hogyan lehetne javítani / átalakítani / szépíteni mint fordítva.** Még ha félúton abbahagyjuk is van egy működő de esetleg ronda programunk...

Mindemellett megállapítottam hogy a framework-ök és az engine-k egyik legfontosabb, de kevésbé hangoztatott előnye az, hogy a projekt struktúrájával és paradigmájával kapcsolatos döntések egy részét már meghozták helyettünk, így egyáltalán nem szükséges ezeken gondolkodnunk.

# Egyebek

## flux

Felhasználtam a nagyszerű [flux](https://github.com/rxi/flux) könyvtárat, amely sokat segít a változó állapotok közötti interpolációban (tweening).

## YALG

Amikor egy GUI-libet kerestem a projekthez, de nem találtam nekem tetszőt, úgy döntöttem írok egy sajátot - ez lett a [YALG]({% link _posts/2020-07-03-yalg.markdown %})

A YALG-ot használtam a [13]({% link _posts/2020-07-03-13.markdown %})-ban is.

# Konklúzió

Sikerült befejeznem egy projektet, a termék játszható, és valamennyire élvezetes is. Az elsőre vagyok a legbüszkébb, ahogy ez az egész haladt.

Mindemellett tanultam pár dolgot a nagyobb projektek menedzseléséről, meg úgy általában a fejlesztésről.

Mellékprojektként írtam egy GUI-libet ami akár még másoknak is hasznos lehet, de én is használtam már máshol.

**Köszönet bátyámnak a tesztelésért és a kiváló ötletekért!**