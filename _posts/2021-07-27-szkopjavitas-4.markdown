---
layout: post
title: "EMG-1569 javítás - végre van kép!"
---

{% include imgpath.md %}

Keresvén bárminemű kép hiányának okát a szkópomban [legutóbb]({% link _posts/2021-06-16-szkopjavitas-3.markdown %}) alaposan elmerültem a CRT áramkör és a hozzá tartozó nagyfeszültségű tápegység rejtelmeiben.

Mint később kiderült, mindez teljesen felesleges volt, ugyanis a hibásnak vélt viselkedést egy általam elkövetett aranyos mérési hiba okozta. Csekély vigasz, hogy nem egy gyakori amatőr hiba volt, viszont legalább biztos, hogy többet hasonlót nem fogok elkövetni, illetve amúgy is rengeteg érdekes dolgot megtanultam - még ha nem is jutottam közelebb a hiba megtalálásához.

A tévútra részben a [gépkönyv](https://www.emg.hu/gepkonyvek/EMG_1569.pdf) hibakeresési leírása vezetett, így amikor kiderült, hogy egy mérési hibát kergettem két hónapig duplán bajban voltam, hiszen ha ott sincs a hiba akkor ötletem sem volt, hogy mégis hol lehet, lévén a fontosabb rendszereket a hibakeresési leírás segítségével ellenőriztem, és minden bántóan rendben működött.

# CRT hiba?

A CRT áramkört elég alaposan áttanulmányoztam már, és minden érték a megfelelő paraméterek között volt, az adatlapok szerint a `CRT`nek képet kéne adnia. 

Hogy egyszerűsítsem a helyzetet, megpróbáltam leválasztani a `CRT`-t pár más rendszerről - nevezetesen az eltérítésekről. Ilyenkor nem elég simán lekötni a kábeleket, hanem ajánlott a két lemezpárt összekötni és egy fix feszültségre kapcsolni. Mivel mindkét eltérítés meghajtása differenciálerősítővel történik, így az egyik lemezhez menő vezetéket simán leforrasztottam és rákötöttem a másikra. (természetesen a függőlegest a függőlegessel, a vízszintes eltérítést a vízszintes eltérítéssel kötöttem össze)

![]({{imgpath}}/fenypotty.jpg)

Na ez már haladás! Ez megerősíti, hogy a `CRT`-nek és a hozzá tartozó áramköröknek nincs baja - viszont valamelyik eltérítés áramköre hibás, vagy már ők is hibás jelet kapnak.

Igaza volt hát *Tennōji Yūgo*-nak, szégyellem is, hogy a katódcső hibájára gyanakodtam!

![]({{imgpath}}/yugo.png)

> Nem vagy elég szeretettel a katódsugárcsövek iránt.

(viszont az a kötény *nagyon* menő, kell nekem egy ilyen)

## Eltérítések

Innen már egyszerűbb a helyzet, csak követni kell a nyomokat. Persze rögtön kettéágazik az ösvény, ugyanis a vízszintes és függőleges eltérítés egyaránt elromolhatott, de az sem kizárt, hogy mindkettő bekrepált.

Szerencsére egyszerű eldönteni, hogy mi a helyzet - ha az egyik eltérítést bekötve fényvonalat kapok, akkor az az eltérítés (legalább részben) működik. Ha viszont a visszakötés hatására újra elmegy a kép (és a kezelőszervekkel nem hozható vissza) akkor az adott eltérítésnek mindenképpen baja van.

Két ilyen tesztből ki is derítettem, hogy csak a függőleges eltérítés halt meg.

## Függőleges eltérítés

Nosza akkor nyomozzunk, mi lehet a gond. A kimeneten túlzottan nagy feszültségkülönbséget mértem (ez is differenciális, azaz a két kimenet közötti feszültség számít), ez húzta el az amúgy megjelenő sugarat a képernyőről. Szerencsére a [műszerkönyv](https://www.emg.hu/gepkonyvek/EMG_1569.pdf) 99. oldalán (2/1-es ábra) nem csak a függőleges részleg kapcsolási rajza szerepel, hanem az egyenfeszültségű beállítás közelítő értékei is. Hovatovább mivel egyik csatornával sem kaptam képet, feltételezhető, hogy a közös végerősítő szállt el. (vagy az egyik csatorna úgy, hogy a másikat is elhúzza, de ez valószínűtlen).

A kapcsolási rajz mellé felhasználva a panelrajzot is (118. oldal, 14/2-es ábra) ellenőrizni is tudtam ezeket a feszültségeket - kisebb-nagyobb eltéréssel de mind rendben volt, kivéve az utolsó erősítőfokozatnál.

Az utolsó fokozatot két `KF504`-es tranzisztor alkotja, amelyek `hosszufarku erősítő pár`, amely ha jól értem a `long-tailed pair` fordítása lenne. Ezt az erősítőkapcsolást hívják még `differential pair`-nek is, mivel a két bemenete közötti feszültségkülönbséget erősíti, és a két kimenete közötti feszültségkülönbség a valódi kimenet. Az itt használt verzió némiképpen eltér azoktól amit a neten találtam, de látszik, hogy ez lenne a cél.

## Végerősítő tranzisztorok

A két tranzisztor a bal oldali panel tetején van elhelyezve. 

![]({{imgpath}}/../2020-08-26-szkopjavitas-1/doboznelkul.jpg)

Ez a kétoldalú panel a szerelést megkönnyítendő lehajtható ha kicsavarunk két csavart. Apró szépséghiba, hogy féltucat drót csatlakozik rá, amelyek csatlakozóit ilyenkor egyesével le kell huzigálni, illetve visszacsukáskor visszadugni - jó esetben pont oda ahonnan lehúztuk őket. Persze minden drót fehér, maximum a csatlakozón levő apró (és az öregedéstől néha olvashatatlan) színjelölés alapján tippelhetünk, hogy hová való - no meg persze a hosszából, mivel mindegyik éppen csak, hogy elég hosszú.

![]({{imgpath}}/../2020-08-26-szkopjavitas-1/belseje.jpg)

Tekintve, hogy már mióta kínzom én ezt a szegény készüléket már egész rutinosan megy ez az oda-visszaszerelés. 

A katódcső függőleges eltérítésének kicsatolása nagyon közel van a végerősítő tranzisztorokhoz, olyannyira, hogy az azokon levő hűtőcsillag hozzá is ér a kábelek szigeteléseihez. (az előző képen a panel szélén levő két fekete valamik a hűtőcsillagok)    
Amikor viszont visszaszereltem ezeket a kábeleket, kicsit forgatni akartam a hűtőcsillagokon, hogy több helyem legyen. Ekkor vettem észre, hogy a két tranzisztornak más a fogása - az egyik lényegesen stabilabban áll a helyén, mint a másik.

Elsőre csak hibás forrasztásra gyanakodtam, mivel az is okozhat ilyesmit. Ilyenkor a legegyszerűbb eljárás kiforrasztani az alkatrészt, majd vissza, és ezzel jó esetben meg is van oldva az egész. 

Na nyilván nem volt ilyen szerencsém (ha már véletlenül belebotlottam egy hibába). A kiforrasztandó tranzisztor lábai ugyanis ottmaradtak a pákám hegyén - a tranzisztoron meg semmi. Nem is tudom mi tartotta őt addig a helyén...

![]({{imgpath}}/nincslaba.jpg)

Mivel **a tranzisztor egy háromlábú állat**, logikusan következik, hogy ez - lévén ennek egy lába sincs - nem tranzisztor. Ez pedig meg is magyarázza, hogy miért nem működik az erősítő - csak adja az ég, hogy ne legyen más baj is emellett!

Arról viszont halványlila gőzöm sincs, hogy mi intézte ezt így el - mi ette meg az aranyozott felületet így, hogy csak ez a barna valami maradt, azt is eltakarta a hűtőcsillag, hogy nehogy észrevegyem...

## KF504

A másik probléma pedig az, hogy ezt a tranzisztort már régen nem gyártják, de még a hasonló paraméterekkel rendelkező helyettesítőire sem találtam hazai forrást ahonnan beszerezhetném.

Már éppen kezdtem elfogadni, hogy kénytelen leszek ismét kifizetni ötezret egy százforintos alkatrész szállításáért, amikor eszembe jutott, hogy megnézzem az *eBay*-en - és bingó, **new-old-stock** formájában ötösével rendelhető. Az aukció persze pár órán belül véget ért, de az már nem zavart...

No és persze rakhattam megint félre az egészet amíg várok a csomagra...

## Beszerelés után

![]({{imgpath}}/negyszog.jpg)

Mázlim volt! A beszerelés után szinte minden működött, bár mint a képen látszik, nem tökéletesen, hogy mást ne mondjak a négyszögjelátvitel borzalmas... Ezzel viszont már érdemes nekifutni egy kalibrációnak, amihez korábban a műszerkönyv alapján [írtam is egy segédletet](https://docs.google.com/document/d/1qmQ0HcECZFvDG5XUfFSKzFTRhJNQkfdh3wTJpYy6CwA/edit?usp=sharing)...

## Váltottsugaras indítás

A funkciók próbálgatása közben feltűnt sajnos, hogy az egyik üzemmód nem működik - nevezetesen a váltottsugaras indítás.

Ez a szkóp egysugaras, de kétcsatornás. Egy sugárnyalábbal két csatorna jelét kirajzolni nem feltétlen triviális, bár adja magát, hogy időosztással kell megoldani a problémát. Két opciót is kínál erre ez a szkóp: `CHOPPED` üzemmódban viszonylag gyorsan (kb. `1MHz`-el) váltogat ide-oda a két csatorna között (a váltás ideje alatt természetesen nullára állított fényerővel), míg `ALTERNATE` módban minden indítójel hatására teljesen kirajzol egy csatornát, de, hogy melyiket azt váltogatja. (És persze van lehetőség csak az egyik vagy a másik csatornát megjeleníteni.) Előbbi lassabb, míg utóbbi gyorsabb jelek esetén hasznos.

A hibajelenség az volt, hogy `ALTERNATE` állás esetén csak az egyik csatornát rajzolta ki - de, hogy melyiket, az valamelyest véletlenszerű volt.

A két csatorna között az izgalmas nevű `kapcsoló multivibrátor` dönt. Ennek (és a közeli áramköröknek) a kapcsolási rajza a gépkönyv 103. oldalán (2/5-ös ábra) található. Ennek az áramkörnek a megértésére ráment egy kis időm, de nem olyan bonyolult.

![]({{imgpath}}/schema.jpg)

A bal felső két keresztbecsatolt tranzisztorban felismerhető a klasszikus `bistabil multivibrátor` kapcsolás - a két tranzisztor kölcsönösen ki akarja kapcsolni egymást, így két stabil állapot jöhet létre, amikor az egyik teljesen ki van kapcsolva és a másik meg teljesen be. A két tranzisztorról két kimenet van kicsatolva, amelyek az adott csatornát kapcsolják ki vagy be.

(Ez az áramkör egyébként közeli rokona a klasszikus két tranzisztoros kétledes villogónak, de az (`astabil multivibrátor`) nem rendelkezik stabil állapottal, ezért ott a két labilis állapot egymást váltja.)

Ha viszont az éppen aktív tranzisztort mi kívülről kényszerítjük, hogy kikapcsoljon, akkor képesek vagyunk átváltani az áramkör állapotát, így ez a kapcsolás SR tárolóként is használható.

(a tankönyvi SR tároló általában NOR kapukból épül fel, míg ez, vagy legalábbis ennek NPN tranzisztorokból felépített verziója inkább NAND kapukra hasonlít, de ugyanúgy működik)

Ez a klasszikus áramkör itt pár diódával és kondenzátorral van kiegészítve, amik azt érik el, hogy egyetlen kapcsolóimpulzust juttatnak el mindig az aktív tranzisztorhoz - azaz bármilyen állapotban volt az áramkör, az impulzus hatására átvált - így ez az áramkör már inkább a T-flip-floppal van rokonságban.

Az üzemmódváltó kapcsoló egyik tárcsája erre az áramkörre rákényszerítheti az egyik vagy a másik stabil állapotot, így megoldva az egyik vagy a másik csatorna kizárólagos kijelzését. 

A váltást előidéző impulzus forrása kétféle lehet. A `Tr818` tranzisztor mint oszcillátor működik (ha a kapcsoló a `CHOPPED` állásban van), így a két csatorna között folyamatosan oda-vissza váltogatunk. `ALTERNATE` állásban viszont a fűrészjelet is indító jel vált a két csatorna között.

Mivel csak az `ALTERNATE` állás nem működik jól, feltételezhető, hogy ez az indítóimpulzus nem jut el a tárolóhoz, ennek útja pedig visszakövethető - lenne, ha tudnám, hogy ez az áramkör fizikailag hol helyezkedik el. A panelrajzokon mindenesetre nem szerepel...

Van még pár eldugottabb hely a szkópban, például egy kisebb panel a hálózati transzformátor oldalán vagy egy sor forraszléc a doboz alján. Mivel a kisebb panelen nem láttam diódákat, így a doboz alja maradt...

Na de, hogyan férek ehhez hozzá? Hát felborítom az egészet, és így az alja lesz az oldala!

![]({{imgpath}}/alja.jpg)

Hát szép, az ilyesmin aztán nem triviális kiigazodni.

Lőttem viszont róla egy viszonylag éles fotót, és azután a kapcsolási rajz alapján viszonylag könnyen el tudtam igazodni rajta.

![]({{imgpath}}/reversed.jpg)

Végül nem is kellett rajta javítani, a `P823`-as potméter beállítása meg is oldotta a hibát, bár elsőre itt is csak úgy tűnt, hogy jó a beállítás, elég érzékeny ez az áramkör.

Persze ahhoz, hogy a potihoz hozzáférjek, megint az oldalára kellett fektetni.

![]({{imgpath}}/cso.jpg)

Hát ez viszont elég veszélyes mellékhatás! Elektroncsövet fejjel lefelé? A végén még kipotyognak az elektronok, aztán söpörhetem őket össze!

## Előzetes

> - Jöhet a kalibrálás! - gondolta Stirlitz.
> - Én megadom magam, nem bírom ezt a terhelést! - gondolta az időalap kapcsolójának tengelye.

Már éppen azt hittem minden simán megy, amikor egyszer csak feltűnt, hogy a nevezett kapcsolót a kelleténél többször tudom körbeforgatni, miközben a szokásosnál kicsit kevesebbet kattan...
