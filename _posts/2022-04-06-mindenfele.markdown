---
layout: post
title: "Mindenféle kisebb projekt"
category: ["elektro", "prog"]
---

{% include latex.html %}

{% include imgpath.md %}

# Nagyfeszültségű kábelszigetelés-vizsgáló - 2021 május

Még az EMG-1569-es szkóp javításakor, amikor azt hittem, hogy a nagyfeszültségű tápegységgel van a baj, apukám mutatott egy furcsa műszert amit soha nem használt, hátha az segít. Mint kiderült, pont erre (lett volna) szükségem, ha a baj nem teljesen máshol van, ez ugyanis egy kábelszigetelés-vizsgáló, avagy 1GOhm-ig működő ellenállásmérő. Nyilván nem akart működni, de egy szétszed-összerak kör, a görbe mutató viszonylagos kiegyenesítése (ez sajnos le is rontja a pontosságát, de a nem működéshez képest azért javulás) és az ónpaca eltávolítása a nagyfeszültségű tápegységről együtt meg is oldotta a problémát. Sajnos a rozsdás elemtartó-érintkezőt sikerült a kelleténél pár nappal tovább hagynom az ecetben, melynek következtében fel is oldódott teljesen, úgyhogy amíg nem csinálok valamiből újat addig csak labortápról megy, de ez annyira nem zavart azóta sem hogy megjavítsam, pedig már használtam erre-arra.

A pontossága nem tökéletes, de eleve van előlapi beállítószerve, szóval gyárilag sem hiszem hogy olyan pontos lett volna. Mindenesetre a tesztjeim során egészen jó volt.

# Brainfuck-2-C fordító - 2021 augusztus

Bátyámnak mutattam egyszer a Brainfuck nyelvet, és kb. fél óra alatt írtam is rá egy interpretert C++-ban. A sebesség javításának érdekében később beleraktam egy szimpla előfeldolgozást is, ami megsokszorozta a sebességét. Bátyám is nekiállt BF interpretereket írni, és a kód előfeldolgozásával eljutott odáig, hogy az ő python-os verziója gyorsabb volt mint az én C++-os egyszerű verzióm.

Na hát ez azért mégsem maradhat így! Pár napi munkával írtam egy aranyos python programot, ami a BF kódot értelmezi, előfeldolgozza, optimalizál rajta valamennyit, majd C kóddá alakítja. A keletkető C kódot valamilyen compilerrel lefordíthatjuk (esetleg ő is optimalizál valamennyit rajta), és így a sebessége több ezerszerese lesz az legjobban optimalizált Python-os verziónak is. Például a Hanoi tornyait kirajzoló program a bátyám programjával kb. 1 percig futott, az enyémmel viszont olyan gyorsan lefutott, hogy nem is látszott, kb. egyszázad másodperc alatt végzett is.

[Link a kódhoz](https://gist.github.com/Sasszem/308614f96149e5741aeeace72c169936)

# EMG-1555 javítása - 2021 szeptember eleje

Vettem még 2021 áprilisában egy használt és nem igazán működő EMG-1555 típusú oszcilloszkópot. Nem lehetett ott hagyni egy kétfiókos, 100MHz-s, kétcsatornás és két időalapos készüléket, főleg, hogy kaptam hozzá gépkönyvet és egy extra differenciálerősítős fiókot is. Igaz, elhozni sem volt könnyű, mivel több mint 30 kiló.

![]({{imgpath}}/emg-1555.jpg)

Gyönyörű műszer, sehol egy NYÁK-lap, minden kerámia lécekre van összerakva, nem triviális a javítása ha valami nem működik.

![]({{imgpath}}/emg-1555-tap.jpg)

![]({{imgpath}}/emg-1555-fiok.jpg)

De mint mondtam, és vállaltam a kihívást, hogy kijavítom a hibáját. A hibajelenség elég fura: igen hülye alakú vonalat rajzolt egyenes helyett is. 

![]({{imgpath}}/emg-1555-gnd.jpg)

Rögtön tápfeszültégre gyanakszik ilyenkor az ember, és igen nagy szerencsém volt, mivel tényleg ezzel volt a baj, bár nem volt egyértelmű hogy melyik táp is hülyéskedik. Úgy tűnt, hogy pufferkondit kell majd benne cserélni, de mint kiderült csak lelazultak a rögzítőanyák, meghúzva őket szinte azonnal működni is kezdett a szkóp.

![]({{imgpath}}/emg-1555-jo.jpg)

Ennek a szkópnak egy (amúgy viszonylag ritka) képessége, hogy dual timebase, azaz két időalapja van. A második időalap az első után indul állítható késleltetéssel, és a lefutás sebességét külön lehet állítani. Ennek segítségével a kirajzolt jel egy darabja kijelölhető, ahogy a képen is látható, majd egy gomb elfordításával csak a kijelölt szakasz kirajzolható, azaz a jel egy darabjára rá lehet nagyítani. Sajnos nem képes egyszerre az egész és a kinagyított szakaszt kirajzolni, ami apró szépséghiba. Léteznek olyan szkópok amik ezt is képesek megcsinálni, de sem ez, sem a Tektronix 647A, amiről ezt másolták, nem képes erre.

Apropó, Tektronix 647A...

![](https://w140.com/tekwiki/images/4/4d/Tek_647a_trace5.jpg)

Mint mondtam, az EMG-1555-öt erről másolták. Igen jó munkát végeztek ahogy az látható, megtévesztésig hasonlít a kettő. Az egyetlen amit sajnálok, hogy lehagytak azok a fiókok fogantyúi, ezen kívül a kettőt nem is lehet összehasonlítani annyira egyformák.

# Műszerpark-bővülés - 2021 október

Említettem [egy korábbi bejegyzésben]({% post_url 2021-08-22-noaa-20 %}), hogy nincs spektrumanalizátorom. Megkeresett Ricsi, akitől a Phillips-PM3323-as szkópot is vettem, hogy nem érdekelnek-e eladó műszerek, mivel családi okból szabadulni szeretett volna pártól, és szerette volna ha jó kezekbe kerülnek. Az egyik műszere egy Takeda Riken *TR-4122B* típusú spektrumanalizátor volt, amire nem lehetett nemet mondani:

![]({{imgpath}}/sa.jpg)

Ezzel már ki fogom tudni mérni a koaxkábeles sávszűrőt is, illetve igen hasznos lesz ha bármilyen nagyfrekvenciás áramkört építek (amit azért tervezek csinálni). Jelenleg várok hogy megérkezzenek a BNC-N átalakítók amiket rendeltem, ugyanis ez már elég komoly műszer ahhoz, hogy N csatlakozóval lássák el, ámde én főleg BNC-t használok.

Egy másik műszer amire igent mondtam egy Fok-Gyem TR-9162/A típusú kettős labortápegység volt:

![]({{imgpath}}/psu.jpg)

Ez kétcsatornás, földfüggetlen, 40V/1A (20V-ig 2A, természetesen csatornánként), áramkorlátozott labortápegység. Egyetlen hátránya, hogy az alakja miatt még nem tudtam beilleszteni (ezt sem) az asztalon állandóan elhelyezett műszerek közé, úgyhogy akárhányszor használni akarom, elő kell szedni a szekrényből, amit nem könnyít meg a tény hogy dögnehéz. Utóbbi oka egyébként az, hogy a két csatorna annyira független egymástól, hogy csakis a föld és a 230V-os bemenetük közös, még hálózati trafójuk is külön-külön van.

# Mátrix 2021 - 2021 október

Részt vettem szerelőként a 2021-es Schönherz mátrixban is.

Az idei mátrixról készült videó:
{% include youtube.html url="https://youtu.be/BFk55DCdfws" %}


# HCSC21 - 2021 október-november

Ismételten részt vettünk csapatunkkal (*KosmX* és *kecskemekeg*) a Hungarian Cyber Security Challange-n, végül holtverenyben negyedikek lettünk (értsd: 4x holtverseny volt az első helyen, de mi voltunk a leglassabbak). Ezúttal a szervezés bőven nem volt a helyzet magaslatán, amiről írtam is egy kisregényt, viszont mivel a feladatok és megoldások *lehet*, hogy bizalmasak (értsd: a saját megoldásaimat sem biztos, hogy közzétehetem, a hivatalosat egészen biztosan nem, nem mintha azt az izét megoldásnak lehetne nevezi ahol random előhúzzák a hátsó felükből a szerver forráskódját). Összességében jól is éreztük magunkat, de a szervezésre -100 pontot kapnak tőlünk.

Nem értem mi olyan bonyolult abban a csapatnévben, hogy `0118 999 881 999 119 7253`.

# Előre nem látott laptopjavítás - 2021 november

Csak hogy jól érezzem magam, az esti sorozatnézés előtt sikerült véletlenül kb. negyed liter szőlős márkát elhelyeznem a laptopom belsejében. Sajnos a következő bekapcsolásig nem száradt ki rendesen (türelmetlen voltam egy kicsit), és rövidesen elment a kép. Mint kiderült, csak az LCD háttérvilágítása halt meg, és piszok mázlim volt, mivel csak a tápfeszültséget biztosító kapcsolóüzemű áramkör simító kondenzátorára került némi cucc ami azt rövidre zárta. Másnap letakarítottam alkohollal, és meg is javult. Nem csúnya látvány egy laptop kiterítve a koliszobában az asztalon, de nem akartam volna amúgy belenézni.

A kondi tisztítás előtt:

![]({{imgpath}}/kondi_kampec.jpg)

És tisztítás után:

![]({{imgpath}}/kondi_jo.jpg)

A billentyűzet is kapott egy keveset, amit sikerült azóta kiszednem belőle sok-sok alkoholos átmosással. Sajnos az első szétszedési kísérletemnek, amelyet a netes "hogy szedd szét ezen laptop billentyűzetét" videó alapján próbáltam a kontroll (egészen pontosan a jobboldali) elvesztésével járt. Elvileg lehet kapni külön billentyűket bizonyos helyekről, de még nem jutottam oda, hogy megjavítsam, ha már volt annyi eszem, hogy a leghaszontalanabb billentyűvel próbálkozzak először.

# Frekvenciaszámláló javítása - 2021 decembere

Hozzájutottam egy Híradástechnika szövetkezet által gyártott, TR-5258 típusú digitális 25MHz-s frekvenciaszámlálóhoz. Levágott zsinórral került hozzám, és nem is sikerült bekapcsolni. Kis méregetéssel arra jutottam, hogy valószínűleg megszakadt a hálózati trafó primere, ami elég nagy baj, mivel nem triviális ilyet javítani. Szerencsére sikerült hozzá gépkönyvet találni hozzá, amiben ráadásul benne volt a trafó tekercselési rendje is, tehát az alapján akár új trafó is készíthető.

Szerencsére kicsit több áskálódás után kiderült, hogy csak a hálózati kapcsoló és a feszültségváltó kapcsoló kontaktos, szóval viszonylag gyorsan helyre is lehetett hozni ismételt átkapcsolásokkal. Sajnos kontakt tisztítót nem tudtam a kapcsolókba fújni, mivel nem lehetett ezekhez hozzáférni, de így is működik a készülék.

De hogy még mennyire működik azt az is mutatja, hogy 25MHz-s műszer létére egy 30MHz-s jellel még simán megbirkózik:

![]({{imgpath}}/overclock.jpg)

Egyébként ezen műszer pontosságát nem más adja, mint egy fűtött kályhában elhelyezett rezgőkvarc. Ha igazán pontos műszert akarnak akkor a mai napig használják ezt a módszert.

A hozzá való 250MHz-s előosztó szerencsére első kísérletre működött, úgyhogy építhettem analóg elektronikai Lego-tornyot:

![]({{imgpath}}/lego.jpg)

# Képek rajzolása fourier-sorral - 2021 december

Az FFT algoritmussal kapcsolatos prezentációm és a témában való elmélyülés részeként készítettem egy kisebb Python programot ami ábrákat rajzol SVG-ből forgó körök segítségével. Ez főleg az idő- és frekvenciatartomány közötti áttérés szemléletes megértését segíti. Az ábrák viszont látványosak, ami minden projekt esetében pluszpont.

![F-anim kép](https://raw.githubusercontent.com/Sasszem/fourieranim/main/examples/fft.gif)

# Kettő-az-egyben képek a discordon - 2021 december

Az egyik BME-s discord szerverre küldött be valaki egy érdekes képet: 

![]({{imgpath}}/waldo.jpg)

Viszont ha megnyitjuk akkor más jelenik meg:

![]({{imgpath}}/waldo_2.png)

Elégé meglepődtem, hogy előnézetben egy ártatlan kép jelenik meg, de megtekintve rickroll. Kicsit nyomoztam, hogy hogyan is működik ez, és úgy tűnik, hogy az előnézet ignorálja a PNG-ben beállított gamma értéket, és így készül a két kép - a pixelek két csoportra vannak osztva, attól függően hogy melyik képhez is tartoznak, és az egyik jóval sötétebb mint a másik. Amikor az előnézetet látjuk, akkor a gamma érték ignorálva van, a nyers pixeladatok renderelődnek, és a rejtett kép el van sötétülve. Amikor a gamma érték érvényre jut, akkor az egész kép világosabb lesz, amitől az előnézézet eltűnik, míg a rejtett kép láthatóvá válik.

[Írtam is egy programot Pythonban](https://gist.github.com/Sasszem/d3b6973fb4a1d30ae19a0cbcdcfd5df97) ami ilyen képeket állít elő két képből. A működése elég egyszerű, csak összerakja a pixeleket, majd a végén egy kis bináris szerkesztése a PNG adatoknak, hogy beírjam a gamma értéket.

Az egyik általam generált kép előnézete:

![]({{imgpath}}/mc_prev.jpg)

És amikor megjelenik:

![]({{imgpath}}/mc_real.jpg)

# Fast Fourier Transform kiselőadás - 2022 január

A tavaszi féléves "Jelek és rendszerek 2" tárgyhoz extra pontokért [készítettem egy kiselőadást]({{imgpath}}/FFTprezi.pptx) az FFT algoritmusról. Nem nagyon extra, amit kiemelnék az a 6. dia szemléletes ábrája (wikipédia "Spectral Leakage" c. cikkében volt egy majdnem pont ilyen, amihez octave kódot is mellékeltek), illetve a 10. dia ábrája, amit a rekurziómentes algoritmus szemléltetéséhez készítettem.

Felhasználtam továbbá a prezentációban pár animációt amit a korábban említett animációkészítő programommal csináltam.

# Yaesu-FT252 rádió frekvenciakiterjesztése - 2022 január

Hozzájutottam egy Yaesu FT-252 típusú kézirádióhoz, aminek az akkumulátora gyengélkedik. Mivel csak egy darab, nem tudtam nagyon kipróbálni, de elvileg a 2m-es amatőrsávban (144-146MHz) kéne működnie. Ha viszont már van egy ilyenem, érdemes lenne kideríteni, hogy nem tudja-e a kolis rendezvényeken használt közeli, de a sávon kívül eső frekvenciákat. Mint kiderült tudja, de csak vételre, az adást nem engedi. Létezik általában a rádiókhoz "frekvenciakiterjesztés", azaz az ilyen tiltás feloldása. Ez rádiótól függően más és más módon történik, az újabbakba kódot kell beütni, a régebbieknél pedig jumpereket kell átforrasztani. Ehhez a rádióhoz viszont semmit sem találtam. Nem mertem vele túlzottan kísérletezni, úgyhogy inkább megkértem Danit a HA5KFU-ból, ha már úgy is ért mindenhez, egy gyrostálért találja már ki, hogy ezt hogy lehet. Elég gyorsan kiszúrta az alaplapon található 4 jumpert, majd nekiálltunk variálni, és találtunk olyan kombinációt, amelynél a rádió nem tiltotta az adást. Sajnos ekkor viszont nem hallatszott semmi a vevőként használt rádióból, de mint kiderült, a többi sávon sem ad túl nagy teljesítménnyel - majdhogynem semennyivel. Valamibe belehalt a végfok, aminek a típusát sem ismerjük, de van rá azért tippünk - ha legközelebb közösen rendelünk olyan beszállítótól aki tartja, belerakjuk.

A helyes jupmerek: a 4 jumperből a processzor és a csavar közül felülről a 2.-at kell beforrasztani, a többit kinyitni.

# HA5KFU szkóplogó - 2021 október - 2022 február

Kicsit hosszabb, és igazándiból kétrészes projekt volt a HA5KFU-ban standoláshoz használt szkóplogó javítgatása, később újratervezése.

Az eredeti ötlet az, hogy egy számítógép hangkártyájára mint analóg kimenetre küljünk adatokat két csatornán, és azzal egy XY módba kapcsolt oszcilloszkópon ábrákat jelenítsünk meg. A korábban használt python program azonban elcsúszott és erősen vibráló képeket rajzolt, ezért próbálkoztam először azt helyrepofozni.

Kis nehezítés hogy a gépemen a python kódot WSL-ben futtattam, és az nem fért hozzá a hangkártyához. Miután ezt megoldottam, kiderült, hogy a windows szereti "javítás" néven elrontani a hangot, ami ilyen ábrát eredményezett:

![]({{imgpath}}/scopelogo_pc_windows.jpg)

A kód kis farigcsálása után a legjobb eredmény amit elértem:

![]({{imgpath}}/scopelogo_pc_jo.jpg)

Ez sajnos még mindig torz és vibrál.

Közvetlenül ez után másnap viszont elkezdtek beszélni róla, hogy kéne egy újat tervezni, ami megfelelő célhardverre épül és nem okozna ilyen problémákat. Ez a projekt azóta is haladgat, főleg Keri dolgozik rajta ha jól tudom.

Leálltam viszont vitázni vele, mivel ő mindenképpen számláló->EEPROM->DAC sémájú áramkört akart építeni, míg én amellett érveltem, hogy egy egyszerű ESP32 és a beépített DAC-ja tudja ugyan ezt. Keri viszont nem értékelte a mikrokontrolleres javaslatomat.

![]({{imgpath}}/keri.jpg)

Mindenesetre összeraktam gyorsan egy egyszerű programot ESP32-re. Első tesztnek rajzoltam egy kört:

![]({{imgpath}}/scopelogo_kor.jpg)

Innen már tovább lehetett fejleszteni a klub logójával - lefotózni a szkópernyőt nehezebb volt mint átírni a kódot.

![]({{imgpath}}/scopelogo_sotetben.jpg)

A képpontokat SVG-ből generáltam egy python programmal ami a Fourier-es képrajzolóm hasonló modulját használja újra. [A kódot felraktam githubra.](https://github.com/simonyiszk/esp-scopelogo)

A HA5KFU-s szkópon viszont sajnos nem nézett ki ilyen jól:

![]({{imgpath}}/scopelogo_pontos.jpg)

Viszont a minták közötti idő csökkentésével ez javítható volt.

![]({{imgpath}}/scopelogo_vegso.jpg)

# Kettő-az-egyben képek a discordon II - 2022 március

Ismét beküldött valaki egy érdekes képet discordra:

![]({{imgpath}}/courier_prev.jpg)

Megnyitva viszont ez fogad:

![]({{imgpath}}/Courier.png)

Ennek okát viszonylag könnyű volt kideríteni: a kép egy animált PNG kép. Ezeknél külön beállítható egy előnézet, ami megfelel a "sima" png specifikációnak, így az animációt nem kezelő programok csak ezt jelenítik meg. Az animált rész egyetlen képből áll, és ez jelenik meg minden programban ami kezeli ezt.

Erre nem írtam programot, de nem is lenne túl bonyolult.

# Galvanikusan leválasztott kisteljesítményű tápegység - 2022 március

Egy nagyobb projekt egyik legelső lépéseként építettem egy 6.3V effektív értékű, 300mA-es terhelhetőségű galvanikusan leválasztott váltakozóáramú tápegységet.

A galvanikus leválasztást természetesen transzformátorral végeztem. Az őszi félévben tanultunk elektrotechniából trafóméretezést. Az alapvetően használt egyenlet, amely megadja egy tekercsben indukált feszültséget:

$$U_{csúcs}=N\frac{\partial \Phi}{\partial t}=2\pi fABN$$

Gyakorlatban inkább szinuszos időfüggvénnyel és ennek megfelelően effektív értékkel számoltunk:

$$U_{eff}=\frac{2\pi}{\sqrt{2}}A_{vas}fB_{max}N$$

Aholis $A_{vas}$ a vasmag hasznos keresztmetszete, $f$ a működési frekvencia, $B_{max}$ a vasmagban az indukció csúcsértéke és $N$ a tekercs menetszáma. $B_max$ és $A_{vas}$ általában meg fog egyezni minden tekercsre a transzformátoron. A $\frac{2\pi}{\sqrt{2}}$-re jó közelítés a $4.44$, de négyszögjel mint időfüggvény esetében $4$-el kell számolni.

Egy másik gyakorlati forma:

$$4.44NfB_{max}A_{vas}=10^8U$$

Itt viszont $B_{max}$ Gauss-ban van megadva ($10^4G$ egy Tesla), és $A_{vas}$ $cm^2$-ben. Ezek miatt jön be a $10^8$ szorzó, ettől eltekintve ez a képlet is megegyezik az előzővel.

Ferritmagos transzformátort terveztem bontott magból. Ez azt jelentette, hogy $A_{vas}$ már fix, és a veszteségek elkerülése végett $B_{max}$-ot is limitálnom kell - pontos értéket nem találtam, de elvileg $1300-2000G$ nagyon nagy valószínűséggel jó. $U$ szintén adott ($6.3V$), így már csak $f$-et vagy $N$-et kell megválasztani. Mivel $fN=konstans$ formájú az összefüggésem, $f$-re alacsony értéket tippeltem be, mivel így biztosan elég nagy $N$-t kapok. Ha $Nf$ túl nagy akkor $B_{max}$ fog csökkenni, ami nem akkora baj, mivel ez csak azt jelenti, hogy nem használom ki teljes egészében a ferritmagot, de ezen kívül nem okoz bajt.

Összességében 35 menetet számoltam a trafó mindkét oldalára. A primer oldalon 12V csúcstól-csúcsig négyszögjellel hajtottam, ami így valamivel kisebb szekunder feszültséget eredményezett mint 6.3V.

Az első ilyen módon készült trafó:

![]({{imgpath}}/trafo_1.jpg)

Kérdés viszont, hogy hogyan hajtsam ezt. Külső oszcillátoros kapcsolással sajnos nem jött össze a megfelelő hatásfok, mivel kb. 1A-es áramfelvételt mértem, ami így $<20%$-os hatásfokot jelentett, ami minden szempontból igen vacak. Ennek két oka lehetett: kapcsolási veszteség, mivel a kapcsolást nem a trafó önrezgési frekvenciáján végzem, illetve az, hogy az árammérőm nem átlagértéket mért, hanem csúcsértéket, és az áramfelvétel időben változik.

Nosza, hajtsuk akkor önrezgő kapcsolással, az majd csökkenti a kapcsolási veszteségeket! Kaptam egy olyan tippet, hogy a [skori-féle kisteljesítményű kapcsolóüzemű tápegység-kapcsolás](http://skory.gylcomp.hu/kistap/kistap.html) jó kiindulási alap lehet nekem is, ha a középleágazásos tekercsét középleágazásos transformátorra cserélem. Készítettem ehhez egy új tekercset:

![]({{imgpath}}/trafo_2.jpg)

Ez a kapcsolás jól működött, de sajnos csak addig amíg a terhelő ellenállást rá nem kapcsoltam, mert akkor azonnal leállt, és bárhogyan módosítottam, nem tudtam rávenni, hogy terhelés mellett is működjön.

Végső elkeseredésemben elővettem kedvenc kis- és középfrekvenciás oszcillátoromat, a keresztbecsatolt tranzisztorpárt. Sok variálás után a következő áramkörhöz jutottam:

![]({{imgpath}}/schema.jpg)

Ehhez egyébként egy régi zavarszűrő transzformátort szedtem szét és tekercseltem újra 42+42 menetes primerrel.

Látható, hogy az áramkör nem tartalmaz semmiféle visszacsatolást a két oldal között. Próbálkoztam optocsatolóval, de sajnos többet rontott az egyszerű P típusú szabályzóm a stabilitáson mint használt. A zárt hurkú szabályozás helyett került be a primer oldalra a potenciométer, amellyel valamelyest (meglepően pontosan) beállítható a kimeneti feszültség, és az egészen pontos, kb. 5%-on belül marad. A két tranzisztort próbálgatással határoztam meg, mivel ezekre viszont valamivel érzékenyebb az áramkör - a **D1308**-as típusú NPN darlingtonnal, **BD242**-es PNP tranzisztorral (helyes polaritás mellett természetesen) nem volt az igazi, végül a fiókban talált **C3039**-es NPN-el viszont vígan működött. Nem próbáltam ki olyan sokfélét, valószínűleg más mezei NPN-el is jól működik, ámde nekem nem volt túl sokfajtából készletem.

A megépített áramkör:

![]({{imgpath}}/aramkor.jpg)

Terhelésnek egy ECC84-es elektroncsövet használok, mivel ez pont 300mA-t fogyazt 6.3V-on, ráadásul foglalatom is akadt hozzá - de ez csak egy teszt terhelés volt.

Előnyös tulajdonság azonban, hogy mivel nem tud túl nagy teljesítményt átvinni, nagyobb terhelés hatására csökken a kimeneti feszültség - gyakorlatilag lágyindítóként is működik az áramkör.

További előnye, hogy az áramfelvétele alacsonyabb. Még mindig előfordulnak benne csúcsok, de átlagértéket véve az általam számolt hatásfok minimum 80%.

A kimeneti jelalak:

![]({{imgpath}}/kimenet.jpg)

Végezetül egy hangulatos kép az új RGB műhelyvilágításomról:

![]({{imgpath}}/rgb_muhely.jpg)

Pirosan világít a csőfűtés és az elosztó, kéken a forrasztóállomás, míg a szkóp szép zöld fényt áraszt...

# HA5KFU tanfolyam - 2022 március

A HA5KFU tavaszi tanfolyamában tartottam két témából, nevezetesen "elektronikai alapok"-ból és "szoftverrádiók"-ból kiselőadást. Ha minden jól megy akkor utóbbi témából a gyakorlatot is tarthatom én.

# Cikk a HA5KFU.hu-n

A HA5KFU.hu-ra is [írtam egy cikket](https://ha5kfu.hu/2021/11/11/szakmai-tovabbkepzes-a-rohde-laborban/) a közösen hallgatott vektorhálózat-analizátoros továbbképzésről.

# Amatőrvizsga - február 24

Végre írtak ki rádióamatőr vizsgára időpontokat, úgyhogy február 24-én megpróbálkoztam HAREC fokozatú vizsgát tenni. Sajnos a jogi részből egy ponttal a határ alá kerültem így megbuktam, viszont sikeres morze-vizsgát tettem (bár ez sem ment túl jól, de megadták). Mivel csak egy témából nem mentem át, így csak ezt kell pótolnom a következő vizsgaalkalommal.

