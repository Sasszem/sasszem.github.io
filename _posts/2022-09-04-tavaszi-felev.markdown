---
layout: post
title: "2021/22 tavaszi féléves dolgok"
category: ["elektro", "prog"]
---

{% include latex.html %}

{% include imgpath.md %}

Most, hogy nyakunkon az őszi félév, lassan ideje megírnom a régen tervezett cikket az előző féléves egyetemi dolgokról.

# Memrisztoros irodalomkutatás - Mikroelektronika

Mikroelektronikából iMsc pontokért kellemes feladatot adtak ki: készítsünk (két fős csapatban vagy egyénileg) irodalomkutatást valamilyen választott témában, és írjunk belőle pár oldalas dolgozatot. Egyik évfolyamtársammal vágtunk bele csapatban, és a választott témánk a kiadottak közül a memrisztorok témája volt.

A memrisztor egy igen érdekes áramköri elem, a működését elméleti alapon jósolták meg, direkt fizikai realizációja a mai napig nincs (bár vannak olyan szerkezetek, amelyek így viselkednek, de mások vitatják, hogy ezek ténylegesen memrisztornak tekinthetők-e). Egyik legnagyobb jelentősége talán, hogy a memrisztív hatás solid-state adattárolásra lenne alkalmas, több feltörekvő memória-technológia (FeRAM, Intel Optane, stb.) is modellezhető vele.

Mivel irodalomkutatást végeztünk, így nem készült semmilyen új eredmény, mérést, szimulációt, számítást sem végeztünk, viszont beleástuk magunkat a témába, és elolvastunk sok publikációt is, amelyek közül meglepően sok volt igencsak frissnek mondható.

![]({{imgpath}}/karakter.jpg)

Egy mérést végül mégis elvégeztem: kimértem egy vasmagos tekercs U-I hiszterézisgörbéjét illusztrációs célból. Az egyik első dolog, ami eszembe jutott ugyanis a hiszterézis-alapú adattárolásról nem volt más, mint a mára már szinte elfeledett ferritgyűrűs memóriák működése. Mind az elméleti memrisztív, mind a történelmileg igen jelentős ferritgyűrűs RAM (core memory) (illetve több egyéb, feltörekvő technológia) hiszterézis segítségével tárol adatot. Kicsit alaposabban utánajárva kiderült, hogy ennek ellenére jelentős különbségek vannak a tárolási módokban, amit legjobban talán a hiszterézisgörbe alakja határoz meg, és ennek kapcsán, demonstrációs céllal mértem ki egy mágnesezettségi görbét.

A dolgozatban végül egy részt a core memory és a memrisztív adattárolás összehasonlításából írtam, mert meglepően sok hasonlóság van a két technológia között. Érdekes módon találtam pár hasonló összehasonlítást az irodalomkutatás során, sőt, egy olyan kutatást is, amely ez alapján elindulva próbált memrisztort realizálni, de a végeredmény viselkedése jobban hasonlított a core memoryra.

A teljes dolgozat jelenleg nem publikus, így linkelni sajnos nem tudom.

# Rádióamatőr hívójelkönyvecske - Informatika 2

**Informatika 2** tárgyból elég sokféle témát tanultunk, többek között webfejlesztést `XAMPP` alapon. A tárgyból a vizsgát meg lehetett úszni, ha készítünk egy (opcionális) nagyházi projektet, és én éltem ezzel a lehetőséggel.

Volt pár követelmény, pl. `XAMPP` stack használata, az adatbázis összetettségére minimumkövetelmény, `SQLi`-védelem, illetve voltak opcionális követelmények, amelyek külön-külön értek pontokat, pl. felhasználó-kezelés és jelszó tárolás (szigorúan hashelve), több téma implementálása, és hasonlók. Végül a legtöbb követelmény teljesítettem, mert biztosra szerettem volna menni.

A választott témám egy rádióamatőr hívójelkönyv/logalkalmazás lett, főleg alap funkciókkal. Hogy a saját életemet ne nehezítsem meg a kelleténél jobban, `docker`izáltam az egész appot (és inkább `NGINX`-et használtam Apache helyett, de elfogadták). PHP-ban korábban főleg csak keretrendszerrel dolgoztam (`Laravel`), úgyhogy most megtanultam az alap PHP-t is, illetve leginkább összedobtam egy saját keretrendszert benne. Elég sok szenvedés volt mire működni méltóztatott az `NGINX` routing kiiktatása és a front controllerem, majd a PHP-s regex alapú routing (senki nem kérte, hogy _gyors_ is legyen, bár ez annyira nem súlyos talán). Ezen kívül **MVC** felépítést alkalmaztam, de saját templating rendszer írására már nem vállalkoztam, viszont egy minimális automatikus dependency injection támogatás készült. A legkuszább része az oldalnak az adminpanel lett, mivel itt a PHP kód az adatbázis szerkesztéséhez szükséges oldalakat előzetes ismeret nélkül, csak az adatbázis elemzésével készíti el.

A PHP-s backend mellé minimalista frontend készült *Bootstrap* alkalmazásával, és minimális kliensoldali scripteléssel. Több *Bootstrap* témát is beépítettem, a következő képek a *"Sketchy"* nevűvel készültek:

![]({{imgpath}}/search.jpg)
![]({{imgpath}}/profile.jpg)

# 14MHz-s AM-DSB-SC adó-vevő - NAR (Nagyfrekvenciás áramkörök realizációja)

Felvettem egy ígéretesnek hangzó 2 kredites szabadon választható tárgyat is. A félév során Dudás Levivel (aki megígérte, hogy mindenkit megbuktat aki lemagázza) készítettünk el egy általa tervezett AM-DSB adó-vevőt. Levi megtervezte az áramkört, az én dolgom pedig a realizáció volt - az áramkör bevitele `KiCAD`-be, egy panelterv készítése, majd a paneleket a jól bevált vasalós módszerrel legyártottuk, és a kész panelt összeraktam. A vasalással már komplikációk voltak, Levi vasalója ugyanis csak neki engedelmeskedik, rajta kívül nem igazán születtek szép eredmények vele, az én panelem végül az otthoni felszerelésemmel készült (de azzal elég szép lett). Az élesztés ismét trükkös volt, a tekercs kivitelezésére igen érzékeny az áramkör, és a vételi oldal pedig indokolatlanul gerjedt. Levi tanácsai alapján jó párszor átforrasztottam, de nem segített (viszont a panel igen csúnya lett miatta), végül a tápellátás áramkörében lett meg a - tervezési - hiba. Elég sokáig kerestük, de amint meglett kiderült, hogy másoknak is csak ez volt a baj, és egyetlen ellenállás kicserélésével meg is javult az áramkör.

![]({{imgpath}}/top.jpg)
![]({{imgpath}}/kesz.jpg)
![]({{imgpath}}/keszkozel.jpg)
![]({{imgpath}}/mod.jpg)

