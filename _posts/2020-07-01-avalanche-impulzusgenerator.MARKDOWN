---
title: Avalanche-impulzusgenerátor
layout: post
category: elektro
---

{% include imgpath.md %}

![Teljes kép]({{imgpath}}/tdr.jpg)

Eredetileg koaxkábelek teszteléséhez (eldönteni hogy `75` vagy `50` ohmosak) akartam építeni egy `TDR`-t, de végül a kihívás hajtott hogy elő tudok-e állítani nagyon gyors impulzusokat.

# Mi az a TDR

A TDR (*time domain reflectometer*) egy olyan készülék, ami nagyon-**NAGYON** gyors felfutási idejű (pár `ns`!) jeleket generál. Olyan gyorsakat, hogy a jel felfutása gyorsabb mint ahogy a jel végighalad a kábelen - így hullámjelenségek (legfőképpen **visszaverődés**) lépnek fel, amelyek segítségével vizsgálhatjuk a kábel tulajdonságait.

A kábelen a jel egy adott `C` sebességgel terjed, amely megközelíti a fénysebességet (minimum `60%`-a, kábeltípusól függően), és a visszaverődő impulzus segítségével le tudjuk mérni hogy mennyi időbe telt a jelnek a kábelen *oda-vissza* végigmenni. Ez alapján a `C=2L/t` képlet alapján meghatározhatjuk a jel sebességét (ha tudjuk a kábel hosszát és az időt lemérjük) vagy a kábel hosszát (ha ismerjük `C`-t és lemérjük `t`-t). Utóbbi különösen hasznos lehet ha van egy hosszú, esetlegesen beépített kábeldarabunk, ami *valahol* el van szakadva (vagy rövidre zárva) - lemérhetjük a szakadásig tartó kábelszakasz hosszát.

A visszaverődés megszüntethető *impedanciaillesztéssel* - azaz ha a kábel végén az impedancia megegyezik a kábel karakterisztikus impedanciájával - ekkor az impulzus teljes energiáját elnyeli a lezáró impedancia, és nem jön létre visszaverődés. A nem helyesen illesztett impedancia visszaverődést okoz - a túl nagy azonos fázisút, a túl kicsi ellentétes fázisút. A szakadás (nyitott vég) itt végtelen nagy ellenállásnak tekinthető, míg a rövidzár 0 ohmosnak...
Természetesen nem kell (és nem is lehet) tökéletesen illeszteni az impedanciákat, de általában (legalábbis rádiófrekvenciák esetében) törekedni kell a minél jobb egyezésre.

A visszavert impulzus vizsgálatával megállapíthatjuk hogy megfelelően van-e illesztve a kábelünk, illetve hogy kisebb vagy nagyobb az impedancia a kábel végén mint kéne...

Egyszóval egy `TDR` nagyon hasznos ha valaki koaxkábeleket akar vizsgálni - persze én inkább a kihívás miatt építettem...

## Impulzusgenerátor

A neten többféle TDR-áramkör terjed, de két fő típus van: a 74AC-s logikai áramkörre épülő és az avalanche-effektusra épülő. Az előbbihez "speciális" IC-re van szükség, ami nem igazán volt nekem kéznél (a karantén miatt meg még nehezebb bármit beszerezni, de elvileg már úton van ez is), a második áramkör viszont rém egyszerű, csak a tápelleása bonyolult...

![generátor rajz]({{imgpath}}/sch_gener.jpg)

Az áramkör működésének alapja az avalanche (lavina) effektus. A tranzisztor, ha megfelelően nagy a C-E feszültség, spontán vezetni kezd, még ha a bázisáram 0 is - és ez a hirtelen átmenet nagyon gyors. 

A tranzisztor köré egy relaxációs oszcillátort építünk fel egy kondenzátorból és ellenállásból, illetve egy 50 ohmos ellenállást használunk az impedanciák illesztésére. A bázist a földre húzzuk hogy biztosan ne hamarabb vezessen át a tranzisztor.

A nagyfeszültségű áramforrás az ellenálláson keresztül tölti a kondenzátort, amelyen így viszonylag egyenletesen nő a feszültség. Amikor ez a feszültség eléri a kritikus értéket, a tranzisztor átvezet, és kisüti a kondenzátort - létrehozva az impulzust, és újraindítva a kört...

Az áramkör egyszerűsége lenyűgöző, gyakorlatilag változtatás nélkül minden neten fellelhető verzió megegyezik - bár van ahol 50 ohmos ellenállás helyett két 100 ohmosat kötnek be párhuzamosan... A tranzisztor szinte mindenhol a 2N3904-es típus, ami elég gyakori darab - nálam is akadt egy itthon, szóval minden meg is volt a generátorhoz.

![Közeli kép]({{imgpath}}/gener_kozel.jpg)

Az egyetlen nehézség a ~200V előállítása elegáns módon. Amíg a generátorrész mindenhol megegyezett, itt nem volt két egyforma megoldás - és az enyém is csak egy újabb lett...

## A tápegység

A neten két megoldás volt gyakori: önrezgő boost-konverter feszültség-többszörözővel, illetve 
kapcsolóüzemű IC-s transzformátoros. Én az utóbbival kezdtem el kísérletezni...

Az egyetlen gondot az jelentette, hogy nem volt itthon kapcsolóüzemű tápegység IC, és a karantén miatt beszerezni sem nagyon tudtam. Találtam viszont egy 555-öst, illetve egy *valamilyen* transzformátort - valószínűleg egy LCD monitor háttérvilágításából bontottam...

![PSU rajz]({{imgpath}}/sch_psu.jpg)

Az első kísérlet egy egyszerű önrezgő áramkör volt. Hasraütve 22kHz-re állított frekvenciával és a fiókból véletlenszerűen választott tranzisztorral az áramkör éppen nem érte el a szükséges feszültséget - egészen az egyik estig, amikor (valószínűleg az áramkör melegedése miatt) egyszer csak működni kezdett, egészen amíg le nem ütöttem véletlenül az asztalról, de azután többet egyszer sem...

A tápegységet tökéletesítgettem még egy darabig, mire újra sikerem volt. A transzformátort kimérve függvénygenerátorral rájöttem hogy 10kHz-n a legjobb az átvitel. A reflexből beépített antiparallel (flyback) diódát is kiszereltem, illetve kapott egy kondenzátort a tápot stabilizálandó. Így minden kontroll nélkül több mint 500V-ra felment a szekunder oldalon a feszültség...

A tápegységben az igazi áttörést a szabályozás bevezetése hozta. Az ötletet [innen vettem](https://www.dos4ever.com/flyback/flyback.html), és csak csodálkozni tudok az eredeti kitaláló zsenialitásán. A visszacsatolás bevezetése automatikusan megoldotta a feszültségszabályozást problémáját, de az áramfelvétele is jelentősen lecsökkent, megoldva a túlmelegedést is...

Az új tápegységgel már elsőre működött a generátor, és onnan már csak a méretét kellett miniatürizálnom...

![PSU közeli kép]({{imgpath}}/psu_kozel.jpg)

## Impulzusok

Sajnos a szkópom nem tudja  a teljes impulzust felvenni, mivel az nagyon gyors és elég nagy amplitúdójú, így a tetejét sajnos levágja...

### Illesztett impulzus - minimális visszaverődés

![illesztett impulzus]({{imgpath}}/illesztett.jpg)

### Rövidre zárt kábelvég - teljes negatív visszaverődés

![rövidre zárt]({{imgpath}}/rovidre.jpg)

### Szabadon hagyott kábelvég - teljes pozitív visszaverődés

![szabad vég]({{imgpath}}/szabad.jpg)

### Impulzusszélesség - kb. 10ns

![impulzus szélesség]({{imgpath}}/szelesseg.jpg)