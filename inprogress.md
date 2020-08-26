# Folyamatban levő és ötletszinten létező projektek

Elég sok projektem van ami félrerakásra került, illetve igen sok ötletem vagy amibe nem is kezdtem még bele

Az itt található gyűjtemény valószínűleg csak bővülni fog az idő múltával, és van egy olyan érzésem hogy némelyik soha nem is fog elkészülni. Ha bárkinek kedve van, nyugodtan lenyúlhatja bármelyik ötletemet, esetleg dobjon egy e-mailt és akár dolgozhatunk együtt is rajta...

[Vissza](README.md)

## Elektró

### El sem kezdett

#### VLF rádióvevő - DCF77

A DCF77 egy nagyon alacsony frekvenciás rádióadás amelyet órák szinkronizálására használnak. 77kHz-s, egyszerű protokollra épülő adás Németországból, ami nálunk is fogható. 

A kihívás egy saját vevő építése lenne. A frekvencia itt nem túl magas, sőt kifejezetten alacsony, így a nagyfrekvenciás tervezés nehézségei helyett itt az antenna miniatürizálása és egy NAGYON jó szelektivitású sávszűrő tervezésre lenne a fő fókusz.

#### Akkumulátor kapacitás mérő

Elég sok lítiumos és nikkelakkumlátort gyűjtött össze apám az évek során, de van pár kétségem a rájuk írt kapacitással kapcsolatban, főleg a régebbeiknél. Lehetne építeni egy teszert ami feltölti őket, majd konstans árammal merítve kiméri a kapacitásukat. 

#### (E)EPROM programozó

A Z80-as projekthez gondoltam használni, mivel egy bolti készülék árának töredékéért tudnék építeni egy sajátot a megfelelő tudásszinttel. Mivel még a használt ROM típusa sincs eldöntve, ezért lehetetlen tervezni.

#### VGA megjelenítő FPGA-val

Eléggé megtetszett a programozható logika világa, és egy érdekes ötletnek tűnik egy VGA megjelenítő készítése. Az alapok viszonylag egyszerűek, de egy kevés extra munkával sok szép feature-t lehetne összehozni:

- tile based megjelenítés
- sprite-ok átlátszósággal

Viszonylag kevés memória kéne ezekhez, viszont látványos grafikát lehet velük összehozni. Persze kell valami vezérlőprocesszor is, ami lehet szintén az FPGA-n vagy valamilyen külső CPU vagy MCU

#### 3D megjelenítés

A VGA megjelenítés elvetemült továbbiterációja lenne. Egyszínű árnyékolásmentes háromszögek térbeli megjelenítése bőven sok lenne egy egyszemélyes projektnek. Itt már semmiképpen nem úszható meg egy framebuffer használata, és valószínűleg a lebegőpontos aritmetika sem.

Bazi nagy projekt lenne, viszont mindennél látványosabb...

#### LF SDR

A szoftveres rádiók működése ránézésre nem is olyan bonyolult: szuperheterodin vevő + quadrature sampling detector, utóbbi egy analóg MUX-ból is építhető akár. Persze ez csak papíron ilyen egyszerű, elég nehéz lenne egy sajátot nulláról megtervezni, de ha bejönne rajta a Kossuth akkor már tanultam belőle valamit.

[w2aew csinált egy kiváló videót egy SDR kit-ről](https://www.youtube.com/watch?v=6R4zQCs5iKA)

(fun fact: a Kossuth akár egy LM386-os erősítőn is simán bejön)

#### RF filter tesztelés

RF szűrők teszteléséhez segítene egy:

- fehérzaj-generátor
- comb generátor
- sweep generátor

közül bármelyik. Mindegyik építhető házilag, bár eléggé sok mindenben különböznek. A sweep generátor alapján saját spektrumanalizátort is lehetne építeni ha nagyon nagyba akarok belevágni (szokásom mondjuk, aztán csodálkozom ha pofára esek vele), de a legegyszerűbb megoldás egyértelműen az lenne ha vennék egy NanoVNA-t. Mivel még nem nagyon rádiózom, de akarok, így lehet hogy jó befektetés lenne később.

#### FPGA pong

A VGA megjelenítés egyik side-projektje lehetne egy működő Pong készítése.
A Pong nem túl bonyolult játék, akár monokróm megjelenítéssel is használható, viszont elég összetett is ahhoz hogy jó gyakorlat legyen.

#### FPGA mini projektek

Pár tanulóprojekt FPGA-hoz

- serial -> LCD (16x2)
- serial -> 7 szegmenses kijelző
- serial -> serial összeadó
- serial -> LCD összeadó
- serial -> LCD számológép (mondjuk veremalapon [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)-el?)
- stack machine (FORTH-szerű saját "processzor")

#### Mini projektek: erősítők

Beleolvasva a tranzisztoros erősítők működésébe elsőre megdöbbentem hogy mennyire összetett ezek tervezése.
Építenék párat hogy jobban megismerjem őket a gyakorlatban.

#### Mini projektek: oszcillátorok

Az erősítők működése után egy kicsit kísérleteznék oszcillátorok tervezésével is. Az elmélet (k*360°-os fáziseltérés, 1-nél nagyobb erősítési tényező) viszonylag egyszerű, de gyakorlatban egyet sem terveztem még.

#### U-I görbe rajzoló (curve tracer)

Félvezetők és egyéb alkatrészek vizsgálatára lenne alkalmas egy I-U görbe rajzoló. Kivitelezése többféle is lehet, az egyszerű analóg oszcillátortól a digitális megoldásig. Nem mindegy az sem hogy 2 vagy 3 lábú alkatrészeket akarok vizsgálni, illetve milyen feszültségtartományban.

### Folyamatban

#### Theremin

[Hidi Péter](https://www.youtube.com/user/Theremin1979)-től kaptam meg a [thereminjének](https://www.youtube.com/watch?v=bW8Dc-VpOtA) (ami egy módosított "silicon chip theremin" módosítása) építési leírását. Sajnos elég nehezen lehet némelyik alkatrészt (nevezetesen a KF-tekercseket) beszerezni, így a projekt félrerakásra került amíg nem sikerül beszereznem megfelelőt.

A problémám a fehér színkódú KF-ekkel volt, de mint kiderült jó a sárga is (bár mindenki csak hallott olyanról aki látott már olyat aki szerint talán leget hogy jó, de nagyon úgy tűnik hogy használható).

A hibakeresést tovább nehezítette hogy az elején nem volt semmilyen műszerem amivel megnézhettem volna hogy egyáltalán működik-e akár csak részben - azóta van egy EMG-4656-os szkópom (per pillanat nem működik de remélem hogy meg bírom javítani) és egy PM3323-as is.

A legutóbbi elővételkor minden működni látszott, csak a hangerőáramkör sávszűrőjén nem ment át elég nagy feszültség - mint kiderült szakadt a fekete KF szekundere... Ha nem sikerül szerezni egy sajátot, lehet hogy tekerek egy sajátot, rémlik hogy HP is ezt tette, majd előkeresem az emaileket...

#### Z80 számítógép

A C64-es assembly-s próbálgatásaim után elolvasni a Z80 adatlapját elég meglepő élmény volt. A Z80 sokkal sokrétűbb és többet tud mint a 6502, a programozása sem annyira rémálom. Akkor döntöttem el hogy én márpedig építek Z80 alapon számítógépet.

Mindig is akartam egy olyan számítógépet ami kapcsolókkal programozható. [Z80 alapon is találtam ilyet](https://hackaday.com/2014/12/01/a-z80-computer-with-switches-and-blinkenlights/)

Jobban beleolvasva viszont a Z80 működésébe, rájöttem hogy a Z80-nak bizony egy ilyen egyszerű gép majdhogynem méltóságon aluli lenne, így két külön gép tervezésén kezdtem gondolkozni. Az első lenne a kapcsolós, míg a második jobban fel lenne szerelve - de még mindig azon gondolkozom hogy a kettőt lehetne egyesíteni...

Van pár marék Z80-as cuccom, mellé EEPROM, SRAM és társai amit fel tudok majd használni. Van egy kezdetleges előlaptervem is a kapcsolós verzióhoz, de nagyjából itt áll a dolog.

[Találtam egy nagyon szép moduláris Z80 designt](https://www.ecstaticlyrics.com/electronics/Z80/system_design/), ami kiváló kiindulási alap lehet

#### EMG kalibráció / javítás

[(Saját aloldalra mozgattam)](elektro/emgrep/repair.md)

#### DOS PC

Amikor megtudtam hogy az (https://www.youtube.com/channel/UC8uT9cgJorJPWu7ITLGo9Ww)) DOS-ra tervez játékot, majdhogynem azonnal előrendeltem. Most a büszke tulajdonosa vagyok egy eredeti [Planet X3](http://www.the8bitguy.com/product/planet-x3-for-ms-dos-computers/)-nak, aláírt dobozban.

Kaptam egy digitális letöltést is, de az nem éppen az igazi, így nekiálltam összeszedni a dolgokat egy DOS-os PC-hez.
Már van alaplapom, procim, memóriám, hang és videókártyám és tápom is. Amim viszont sajnos nincs az egy IDE-kártya (ISA-s) - anélkül pedig nem tudok DOS-ra bootolni, így az alkatrészek szomorúan porosodnak a polcomon...

## Prog

### El sem kezdett

#### Programozási nyelvek

Elég sokféle programozási nyelvet kipróbáltam már, a `FORTH`-tól a `C#`-ig széles a működési elvek és az absztrakciók spektruma. Elgondolkoztam hogy szívesen terveznék egy-két sajátot, persze csak hobbiból. 

Érdekel a fordítóprogramok működése is, így valamikor bele is akarom majd ásni magam ezekbe, kiváló elfoglaltságnak tűni.

A fordított és interpretált nyelvek közötti különbség miatt elég sokféle projektet lehet kihozni a témából, a `FORTH` interpretertől a teljes gépi kód generálásig (és persze adja magát hogy valamilyen retró platform legyen a cél) széles a spektrum.

Pár alapötlet: 
- pascal-szerű (viszonylag egyszerű nyelvtan)
- B-szerű (szintén)
- FORTH interpreter (szinte nincs is nyelvtan)
- FORTH compiler (gépi kódra)
- TCL / lisp-szerű

Érdemes utánanézni a formális nyelvtanoknak, az azokhoz tartozó értelmezőprogramokkal együtt. Lua-hoz létezik az igen népszerű `lpeg` modul amivel érdemes lehet eljátszani.

#### Disassembler

Elég sok visszafejtő program létezik (Binary Ninja, Hopper, IDA, r2, Ghidra, stb.), amelyek nagyon hasznosak tudnak lenni a saját alacsonyszintű programjaink elemzésekor vagy mások által írt programok visszafejtésekor, de leginkább ha biztonságtechnikával foglalkozunk vagy csak CTF-et játszunk.

A különféle retró rendszerekre viszont viszonylag kevés ilyen program van, és ezeknél akár (viszonylagos egyszerűségükből adódóan) sokkal alaposabb elemzés is lehetségessé válna mind a modernebb rendszereknél.

Konkrétan 6502 / C64 visszafejtésre gondolnék, pszeudokódra illetve változóelemzésre (használt értékek forrásának visszakövetése). Elég nagy projekt lenne, de biztos sok szórakoztató kétségbeesett hibakereséssel járna.

#### RPG-motor

Egyszer régen elkezdtünk a haverokkal készíteni egy saját RPG játékot `RPG Maker`-el. Elég nagy kihívást jelentett viszont az, hogy a program abszolút kezdők számára készült, és mint olyan, elég sok mindent idegesítően körülményes megoldani benne - az elkészült részeken a hibák bő 80%-át az okozta hogy az egyik átmásolt "kódrészletet" (eventet) utólag módosítottam, de amikor újra átmásoltam akkor az egyiket kihagytam. A másik nagy kihívást az összedolgozás jelentette, mert olyan csak nagyon ritkán volt hogy ha ketten leültünk dolgozni akkor összerakáskor nem tűnt el egyikünk teljes munkája.

A játékon szeretnék majd még dolgozni, bár valószínűleg egyedül fogom tenni, és csak nagyon a szabadidőmben (és majdhogynem minden más után), folytatva az eredeti programmal.

Felmerült viszont bennem hogy írni kéne egy saját RPG motort, ami hasonló dolgokat tudna mint a Maker, viszont kiküszöbölve pár hibát:

- adatokat (legalábbis buildelésig) plain text-ben tárolva, segítve a verziókövetést
- rendes scriptelés alapból
- számozott switch-ek és variable-k helyett rendesen csinálva
- támogatni a verziókövető rendszerek használatával a csapatmunkát
- multiplatform: desktop, android, web?

Eredetileg Löve2D alapra gondoltam, de annak a teljesítménye lehet hogy nem lenne elég nagyobb játékokra.

#### Mini projekt: C64 pong

Valószínűleg egy nap alatt megcsinálható, mivel nem túl bonyolult dolog, viszont közepesen látványos.

#### Atari 2600 emulátor

A 2600 az egyik legelső videójáték-konzol, és mint olyan, manapság nevetségesen limitáltnak tűnik. Emulálni éppen ezért lenne könnyű (sokszorosan nagyobb számítási teljesítményünk van) és nehéz (nagyon alaposan kell emulálni mert a programok minden apró trükköt használnak).

#### Könyvelési segédprogram / excel-tábla

Jelenleg a bevételeim / kiadásaim számontartására egy excel-táblát használok (valójában ODF) és pár szép képletet, de néha nagyon az idegeimre megy. Ha jobban értenék a GUI programozáshoz már valószínűleg belevágtam volna egy segédprogram fejlesztésébe, de valószínűleg soha nem is fogok.

#### Sudoku megoldó

Sudoku-t megoldani nem is olyan nehéz. A legtöbb esetben eliminációs módszerrel megoldható az egész, de néha pár tipp is kell.

Ha írok egyet, akkor az:

- webapp lesz
- tippelés nélkül dolgozik
- tippelésnél branch-el és ha több megoldást talál, mindet megmutatja

Nem tűnik olyan nagy projektnek mint némelyik másik ezen a listám...

#### Saját blog

Ez a weboldal nagyon szép és jó mint átmeneti megoldás, de már most is kezd egy-két része idegesítő lenni - főként az MD fájlok manuális linkelgetése.

Mint tudjuk nem is programozó aki nem írt saját CMS-t, így előbb utóbb *muszáj* leszek írni egy sajátot.

Ötletek:
- firebase adatbázis
- MD-szerű formátum
- online szerkesztő

Ez is viszonylag nagy projekt.

#### Fizikai szimulációk

Pár fizikai szimuláció írása:

- inga
- csatolt inga
- hullámterjedés

Igazándiból csak ötlet szinten merült fel, de viszonylag látványosak lehetnének.

#### Roguelike

Elég addiktívak a roguelike játékok, így valami **nagyon egyszerűt** én is csinálhatnék. Ez is ilyen 1-2 napos projekt lenne.

#### High-level Verilog

Az FPGA-s játszadozásaim során elég sok furcsaságot találtam a Verilogban, ami egyrészt jelentősen megnehezítette a tanulást számomra, másrészt elég áttekinthetetlen kódot tud eredményezni. 

Vannak high-level HDL-ek, amelyek orvosolnak bizonyos problémákat, de gyakran teljesen újakat hoznak be. Kíváncsi vagyok én mit tudnék kihozni a témából...

Pár kritérium:

- Verilog / SystemVerilog MODUL legyen a kimenet az együttműködés érdekében
- case / if mint expression a deklaratív design érdekében
- segítő makrók pl. busz szélesség maximum érték alapján
- procedurális szekvenciális kódból automatikus state machine generálás

Ha egy nyelv ezeket tudná akkor erősen ütőképes lenne.

#### Raytracer

A 3D-s megjelenítés egyik módszere a fénysugarak szimulálása. A technika számításigényes, de látványos tud lenni.

[Vannak akik egy teljes raytracer-t képesek egy névjegykártya hátuljára nyomtani](https://fabiensanglard.net/rayTracing_back_of_business_card/)!

#### Beszéd / szófelismerő

Baromi látványos projekt lenne. Egy kimondott szó felimerése az adatbázisból nem könnyű feladat.

Találtam egy videót (sajnos már nem találom) ahol egy IBM XT-n oldották meg, ami enyhén szólva nem kis teljesítmény...

Alapötletnek az FFT-alapú elemzés tűnik ránézésre használhatónak, de nem próbáltam még ki semmit...

#### 3D megjelenítő

Saját 3D megjelenítő processzoron futtatva.

Az alap nem ANNYIRA bonyolult, alap lineáris algebra kell csak a transzformációkhoz és elég sokat lehet meríteni pl. az OpenGL API-ból.

Mindenképpen írni kell hozzá egy saját poligon-raszterizátort. 

[Bisqwit csinál egy nagyon hasonlót](https://www.youtube.com/user/Bisqwit)

#### Chip8 emulátor

Ha már felmerült az Atari2600 emulálása, akkor mindenképpen érdemes megnézni a Chip8-at, ami egy nagyon népszerű platform emulálásra.
Csak arra kell vigyázni hogy nehogy megnézzük mások emulátorait, mert az elveszi a saját verzió megírásának örömeit...

[Vissza](README.md)