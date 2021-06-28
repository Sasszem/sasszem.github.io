---
title: Slayer exciter minitesla
layout: post
---

{% include imgpath.md %}

Készítés ideje: 2015-2016 körül

![kép]({{imgpath}}/mikrotesla.jpg)

Az egyik leges legelső elektrós projektem. Még valamikor 8. környékén építettem egy miniatűr tesla-tekercset [Ludic Science videója alapján](https://youtu.be/4OC7cwI4RNM).

Nem egy nagyteljesítményű cucc, nem hoz létre kisüléseket sem, de fénycsöveket és glimmlámpákat egészen szépen be tud gyújtani a közelében.

Egy elég kreatív ötlet volt Ludic Science-től (hacsak nem ő is látta valahol) a tekercs tetőkapacitásaként egy sörösdoboz levágott alját használni, bár ennek még mindig viszonyleg éles a széle (bár itt úgy sem számít, mivel a teljesítmény túl kicsit ahhoz hogy kisülés jöjjön létre a csúcshatás miatt). 

Az áramkör egyszerűségéhez képest egészen látványos dolgokra képes. Egy egytranzisztoros oszcillátor hajt egy pár menetes primeren keresztül egy párszáz menetes szekundert. Az oszcillátor a szekunderről történő visszacsatolással működik.

Egy LED és egy ellenállás kell csak az NPN tranzisztor mellé, és egy 9V-os elemről egészen szépen működik az áramkör. Az egyetlen gyakori probléma a tekercsek polaritása, de megcserélve a primer polaritását majdnem minden esetben működni kezd.

Na most a "majdnem minden esetben" az rám pont nem vonatkozott. Igaz, nem én rontottam el - a boltban keverték össze a `BD135`-ös és `BD136`-os tranzisztorokat. NPN helyett PNP típust kaptam (egészen pontosan komplementer párt alkotnak, gyak. a pontos tükörképe). Viszont egyáltalán nem működik abban az áramkörben mint a párja...

Egy kis netes keresgélés után viszont arra jutottam hogy érdemes megpróbálkozni minden polarizált alkatrész (mármint a tranzisztor és a LED), illetve a tápfeszültség megfordításával. A dolog bevált, és egészen szépen működik is a kicsike...

[Kicsit később építettem egy valamivel nagyobb (és sokkal látványosabb) tekercset.]({% link _posts/2020-08-24-skori.markdown %})

<iframe width="1519" height="505" src="https://www.youtube.com/embed/02XNL2TRQUY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>