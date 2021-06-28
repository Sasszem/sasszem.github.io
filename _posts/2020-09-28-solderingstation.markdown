---
title: Egyszerű csináld magad forrasztópáka
layout: post
---

{% include imgpath.md %}

![Összerakott páka]({{imgpath}}/osszerakva.jpg)

Megjegyzés: az összerakás alatt nem fotóztam, utólag készültek a képek.

# A Fahrenheit páka

A forrasztás alapjait igen kiskoromban tanultam meg olcsó pisztolypákákkal. Ezek elég egyszerűek: ha nyomod a gombot, a végük meleg lesz, és lehet forrasztani. A hátrányuk a nagyobb méretük, ami miatt fárasztóbb őket használni, és nem is igazán alkalmasak precíz munkára.

(fun fact: a [Skori féle miniteslám]({% link _posts/2020-08-24-skori.markdown %}) (és persze a [Slayer Exciter]({% link _posts/2020-08-24-skori.markdown %}) is ilyennel készült)

Nyolcadikos koromban második lettem az (akkor még leendő) középiskolám által szervezett matekversenyen (és a fizikán is csapatban), amiért bezsebeltem egy kisebb pénzjutalmat. Ennek első feléből vettem magamnak egy __50W-os__ `28020-as Fahrenheit forrasztóállomást`.

Ez egy elég egyszerű szerkezet, mégis igencsak profinak érződött az előbbiekhez képest. Teljesen más a fogása, és az elején elég fura is volt a használata, de elég hamar sikerült megszoknom. Mindenféle pákahegyeket lehetett bele kapni a helyi boltban, amelyek egy-egy adott területen jobban teljesítettek.

Ami viszont negatívuma volt, az a nagy felmelegedési idő (5-10 perc is kellett neki), illetve hogy __csak a teljesítményét lehet szabályozni, a hőmérsékletéről semmilyen visszajelzés nincs__.

Olyan 3-4 év használat után már kezdett kinyúlni benne a fűtőszál, de a cseréje sem igazán segített, ezért úgy döntöttem hogy beszerzek egy újabbat.

# A készlet

Eredetileg egy `Hakko 936`-al kompatibilis kicsiolcsó Ebay-es készletben gondolkodtam, de végül meggyőzött a `T12`-es verzió (szintén Hakko klón). Ezeknél a "pákahegy" (cartridge-nak is nevezik) nem csak pákahegy, hanem beépítve tartalmazza a fűtőszálat és a hőmérsékletszenzort is.

A készlet pontos neve Ebay-en `Digital Soldering Iron Station T12 Temperature Controller Handle Kits for HAKKO`, és egy eredeti Hakko cartridge áráért adnak egy pákát, vezérlőt ÉS egy cartridge-t. 24V-ot szeret enni a kicsike, és akár `70W`-ot is tud, ami kombinálva a kis hőkapacitásával egy baromi gyors reagálást jelent.

Persze nem árt mellé venni egy tápot is, de szintén elég olcsón lehet hozzá 24V 3A-es kapcsolóüzemű tápot.

# Összerakás

## A páka

![Páka belsejének panele]({{imgpath}}/pakapanel.jpg)
A páka összerakása elképesztően egyszerű volt. Nincs is benne más csak egy egyszerű panel érintkezőkkel, illetve van azért benne egy tilt switch is, amit nekem kellett beforrasztani a kábelezéssel együtt.

![Összerakott páka]({{imgpath}}/paka_magaban.jpg)
A zsinórja amúgy szilikonos és hőálló, azaz a maxra tekert páka sem olvasztja meg a szigetelését. Bezzeg a Fahrenheit, azt az első napon elintéztem...

![Csúnya pákahegy]({{imgpath}}/pakahegy.jpg)
És persze adtak hozzá egy pákahegyet is amit a fotózás idejére már feketére használtam. Baromi jó cucc, és igen jól bírja, nagyon kényelmes vele dolgozni.

## A főpanel

![Főpanel]({{imgpath}}/fopanel.jpg)

A vezérlő panelt gyakorlatilag készre szerelten szállítják. Egyedül a páka csatlakozóját, a LED-et és a Rotary Encoder-t kellett nekem beforrasztanom (és persze a tápkábelt).

Egyébként elég okos kis vacak, digitális vezérlésű, hőmérséklet-visszacsatolással... Baromi könnyen kezelhető, és van benne extrának egy hasznos funkció, miszerint ha 5-10 percig ott hagyom a pákatartón, akkor automatikusan kikapcsol, de amint felveszem újra bekapcsol és felfűt...
(ehhez amúgy azt a tilt switch-et használja a pákában).

![Panel hátulja]({{imgpath}}/panel_hatulja.jpg)
Valószínűleg az SMD alkatrészek nagy száma miatt szerelték majdnem-készre.

![Panel alkatrészei]({{imgpath}}/panel_alkatreszek.jpg)
Elég minimális, MCU(nagy fekete bizbasz sok lábbal), Flash (valószínűleg, a kis fekete bizbasz nem olyan sok lábbal), kapcsolótranzisztor (valszleg MosFET, a fekete kocka kevés lábbal), és pár egyéb például saját kisáramú stabilizált táp, és a kijelző és egyéb perifériák kiegészítő alkatrészei. 

## PSU

![PSU]({{imgpath}}/psu.jpg)
A kapcsolóüzemű tápegység elég egyszerű állat (már kívülről, a belseje rendesen meg van pakolva). Semmi dolgom nem volt vele minthogy szerezzek hozzá egy hálózati zsinórt, és rákössem...

![Csatlakozók]({{imgpath}}/psu_csatlakozok.jpg)
Bemegy 230V váltóáram (és védőföld), és kijön 24V...

![Poti]({{imgpath}}/psu_poti.jpg)
A pontos finomhangoláshoz van egy poti is a szélén, de itt nem is igazán kell precíznek lennie.

## Előlap és borító

Persze csak úgy simán összedrótozhattam volna, de azért az még nekem is csúnya lenne, úgyhogy csináltam egy egyszerű előlapot alumítnumból:
![Előlap]({{imgpath}}/borito.jpg)

Erre simán mehet rá a panel, rögzíteni pedig a csatlakozó és a forgatógomb csavarja rögzíti:
![Előlap]({{imgpath}}/elolap.jpg)

Az U alak és pár csavarlyuk segítségével pedig egyenesen a tápegységre szereltem:

![Félig felszerelt előlap]({{imgpath}}/elolap_lent.jpg)

És az összeszerelt főegység:
![Összeszerelt főegység]({{imgpath}}/foegyseg.jpg)

Az egyetlen veszély hogy beleeset valami felűről, de erre vigyázok, illetve még rakhatok rá egy fedőlapot is.

## Pákatartó

![Páka a tartóban]({{imgpath}}/pakatarto_pakaval.jpg)
Ha új pákám van, kéne hozzá egy új pákatartó is...

A lehető legegyszerűbb tákolmány: egy darab fa két lyukkal, és egy kerítésdrótból hajlított tartó:
![Pákatartó]({{imgpath}}/allvany.jpg)

Még csak ragasztva sincs, csak a drót szorul a lyukban:
![Szétszedett pákatartó]({{imgpath}}/allvany_szetszedve.jpg)

Magát a tartót egy darab kerítésdrótból hajlítottam egy nagyobb csavarhúzó felhasználásával.

## Egyéb simítások

Ez olyan egyszerű cucc hogy még a hálózati kapcsolót is lespóroltam róla. Mivel fixen a műhelyasztal kapcsolós elosztójába lesz bekötve, így nincs is rá szükség...
![Elosztó]({{imgpath}}/eloszto.jpg)

Az vezérlő és PSU pedig igen professzionálisan van az asztalhoz rögzítve:
![Bluetek]({{imgpath}}/bluetek.jpg)

Na és nem igazán akart kattanni a forgatógomb kapcsolója, mert kicsit vastag lett az előlap, de elég könnyen megoldotta egy papírgalacsin:
![Galacsin]({{imgpath}}/galacsin.jpg)

És egy slusszpoén: megtaláltam azt a kis szigetelőbizbaszt ami az [EMG szkópom javítása]({% link _posts/2020-08-26-szkopjavitas-1.markdown %}) során esett le a 2N3055-ös áteresztőtranyó lábáról: 
![Kis izé]({{imgpath}}/kisbizbasz.jpg)

# Összefoglalás

Sokkal jobb mint a Fahrenheit, nagyon tudom ajánlani mindenkinek egy hasonló beszerzését!