---
title: EMG 1569 tranyócsere és hálózati kapcsoló
layout: post
---

{% include imgpath.md %}

# Tranyócsere

Az [előző részben]({% link _posts/2020-08-26-szkopjavitas-1.markdown %}) kiderítettem hogy az egyik tápfeszültség áteresztőtranzisztora, egy klasszikus 2N3055-ös kicsit megadta  magát (nyilván magától, az hogy én véletlen rövidre zártam a tápot biztosan nem járult ehhez hozzá), és nem ártana kicserélni, ámde a kelleténél jobban el volt rejtve és körbebástyázva hogy nehogy hozzá lehessen férni.

![]({{imgpath}}/log.jpg)

Mivel majd' egy évvel később írom ezt, az agyam már sikeresen kitörölte az emlékét annak hogy milyen szenvedés volt mégis kiszerelni távtartóstól, hogy csak lengedezzen ott a kábelén, így már azt sem tudom hogyan csináltam. Csak nehogy még egyszer cserélni kelljen...

![]({{imgpath}}/ovoltaz.jpg)

Ő volt az! Őmiatta szívtam ennyit! Ő meg miattam, szóval csak magamat okolhatom...

![]({{imgpath}}/bazisemitter.jpg)

Ezen a távtartón csücsült, a jobb oldalt látható csillámlemezzel elválasztva tőle. Tök jó hogy feliratozták, melyik kivezetés melyik, bár elég sokáig kell nézni hogy meg is tudjuk különböztetni a **B**ázist az **E**mittertől...

![]({{imgpath}}/kulcstarto.jpg)

Nekem viszont van egy "új" kulcstartóm! Menőbb és strapabíróbb mint az EDOram, az biztos!

![]({{imgpath}}/ujtranyo.jpg)

Na és persze van új tranyóm is. Nem pont ugyanúgy néz ki, de befér a helyére, szóval remélhetőleg jó lesz.

(mivel ezt fél évvel később írom így pontosan tudom hogy működött, szóval nem tudom miért írok ilyeneket)

A kis piros izék meg szigetelők, amikből az egyiket a kép készítése után a legszebben elhagytam, [és csak később találtam meg]({% link _posts/2020-09-28-solderingstation.markdown %})...

![]({{imgpath}}/beszerelve.jpg)

A kivezetések jók, és pont nem ér túl a távtartó peremén.

![]({{imgpath}}/kekkabel.jpg)

Ami nagy fejtörést okozott, és legalább háromszor szedtem ki és raktam vissza az egészet miatta, az az volt hogy azt a kék kábelt merre vezessem, végül ez a verzió nyert.

Mondtam már hogy nem szeretem az ilyen kábelezést?

![]({{imgpath}}/bekotve.jpg)

Mondjuk szerencsére a többi kábel már viszonylag könnyen visszaköthető volt, és a tápegység elsőre rendben is működött...

![]({{imgpath}}/pcccso.jpg)

Ezt a képet nem tudom miért lőttem, gondolom hogy eszembe jusson hogy miért szedtem ki azt a csövet onnan. Ha így volt, akkor nem működött, ötletem sincs mit akartam vele...

Amúgy érdekes ez a szkóp, tranzisztorizált majdnem teljesen, de van benne két elektroncső (ha a CRT-t és a nagyfeszt előállító vákuumdiódákat nem számoljuk). Ennek oka leginkább az lehet, hogy a bemeneti impedanciának minél nagyobbnak kell lennie, és ezt csak csővel tudták elérni. Manapság FET-et használnának, de az akkoriban még nem nagyon volt elérhető.

![]({{imgpath}}/csatlakozo.jpg)

A másik borzalmas dolog ebben a szkópban ez a csatlakozótípus a kábelek és panelek között. Amúgy meglepően üzembiztos, nem kontaktos, viszont sok van belőle és mindig le kell húzni őket egyesével akárhányszor valamit akarok a baloldali panelen - a kábelek meg éppencsak elég hosszúak...

![]({{imgpath}}/balpanel.jpg)

Ő pedig az imént említett bal oldali panel. Lakhelye a tápegységek nagy részének és a függőleges erősítőknek. Ahhoz képest egyébként kevés beállítószerv van rajta, csak 15-öt látok hirtelen.

Azt hittem végeztem mára, de...

# Hálózati kapcsoló

Nem akar bekapcsolni!

Mondjuk még mindig jobb, mint ha nem akarna kikapcsolni, de akkor sem szeretem az ilyesmit. Az intensity potméter is (ezzel van összeépítve a főkapcsoló) szabadon forog körbe-körbe.

![]({{imgpath}}/fokapcsolo.jpg)

Valahogy így néz ki az egybeépített szerkezet. A fekete izé a kapcsoló, az ezüstszürke valami amire rá van szerelve az INTENSITY potméter, az őt az előlappal összekötő barna dolog meg egy tengely meghosszabbítás, aminek okát nem teljesen értem, elvégre szerelhették volna az egészet közvetlenül az előlapra is.   
(Ekkor még nem tudtam hogy ezen a potméteren bizony meglehetősen nagy feszültség van, de ez sem magyarázza meg, ugyanis az alatta levőn is hasonló van, az pedig simán az előlapra van szerelve.)

![]({{imgpath}}/kabelezes.jpg)

Kicsit (baromira) homályos kép a főkapcsoló bekötéséről, ami alapján később vissza tudtam szerelni. Készült ilyen a potméterről is, de az még homályosabb, úgyhogy nem mutatom meg.

![]({{imgpath}}/kapcskiszerelve.jpg)

Nem volt túl nehéz kiszerelni az egészet.

![]({{imgpath}}/potikapcsolo.jpg)

A poti és a kapcsoló magukban tűrhetően működnek, kipróbáltam.

![]({{imgpath}}/tengely.jpg)

Szóval marad a tengelyhosszabbító.

![]({{imgpath}}/tengelybelseje.jpg)

Nem egy összetett szerkezet ez sem. A házban csak egy tengely van, és egy tengelykapcsoló, ami összeköti a potival.

Mindegyik elég egyszerű szerkezet, de az egyik csak elromlott!

![]({{imgpath}}/elsoranezes.jpg)

Első ránézésre ez jó. A tengelyeken levő bevágásba illeszkedik ez a kiálló valami, és így kapcsolja őket össze.

![]({{imgpath}}/masodikranezes.jpg)

Másodikra már nem annyira! Így persze hogy nem működik!

![]({{imgpath}}/alu.jpg)

Mivel nem volt hasonló alkatrészem se, ki kellett találnom valamit. Úgy gondoltam, ha alulemezből vágok egy darabkát, az helyettesítheti.

![]({{imgpath}}/celszerszam.jpg)

Ez kérem speciális mikroelektronikai célszerszám!

![]({{imgpath}}/kiskocka.jpg)

Egy ilyen kis alukocka pont jó méret lesz.

![]({{imgpath}}/ujkapcsolo.jpg)

Ismét egy jól fókuszált kép (jól, ámde rosszra fókuszált). Valahogy így néz ki összerakva a ház nélkül.


Sajnos a továbbiakról nincs egy fél képem se, viszont itt még nem ért véget az aznapi szívás.

Kezdésnek kiderült, hogy az alumínium meglehetősen puha anyag, és lazán elkenődött, amikor a kapcsolót próbáltam átkapcsolni vele. Vágtam egy új lemezdarabot acélból, az megoldotta a problémát.

Valamilyen csoda folytán a kapcsoló úgy döntött, hogy ő mostantól nem hajlandó átkapcsolni. Szétszedtem az egybeépített poti+kapcsoló blokkot, majd a kapcsolót is teljesen, úgyhogy ráment pár órám, mire újra összeraktam.   
(Megjegyzem ennek nagy része a szoba túlsó felére ugrott rugó keresésére ment el, csak hogy miután megtaláltam, két perc múlva újra repüljön...)

Miután sikerült megjavítanom a kapcsolót, valahogy sikerült a potit túl erősen tekerve a benne levő egyik bakelitalkatrészt kettétörnöm. Szerencsére a kétkomponensű epoxyval jól ragasztható volt, és azóta is gyakorlatilag hiba nélkül működik, ámde nem voltam így sem túl boldog, hogy eltörtem.

# Másnap


Másnapra megszáradt a ragasztó, és újra működött minden ami korábban. Kép az persze még mindig nem volt...

![]({{imgpath}}/osszecsomagolva.jpg)

Mindenesetre összecsomagoltam az egészet, és félreraktam, hogy majd később folytassam, hiszen kezdődött az egyetem, és nem lett volna jó ötlet kihagyni a kolis beköltözést vagy a nulladik heti kocsmatúrákat.

![]({{imgpath}}/drot.jpg)

Ezt a darab drótot pedig az egész közepén találtam csak úgy odaejtve, úgyhogy csoda hogy nem csinált bajt. Az eredete számomra ismeretlen, bár rémlik hogy régebben mintha a bal panelen levő csőfoglalathoz mintha tartozott volna valami ilyesmi - de akkor meg azt nem értem hogy hogy jött le róla...

**Folyt. köv!**