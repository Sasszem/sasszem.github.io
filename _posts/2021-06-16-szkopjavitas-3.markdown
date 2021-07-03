---
title: Búvárkodás az EMG-1569 CRT áramkörében
layout: post
---

{% include imgpath.md %}
{% include latex.html %}

Az [előző részben]({% link _posts/2020-08-27-szkopjavitas-2.markdown %}) kijavítottam egy hibát a kisfeszültségű tápegységben és egy mechanikai hibát (amit amúgy mindkettőt én okoztam véletlenül), de a szkóp még mindig nem ad képet...

Azóta végül is csak majd' egy év telt el, szóval senki sem vádolhat azzal, hogy elhamarkodott döntések mentén össze-vissza próbálkoznék.     
Amúgy egész jó kifogásom is van, nevezetesen egyetemre vagy mire járok, és bár sajnos meglehetősen hamar hazaküldtek mindenkit, azért majdnem karácsonyig nem költöztem haza, aztán pedig vizsgaidőszak volt... Tavasszal meg a SecChallenge21 vitte az időt, aztán kiderült, hogy néha tanulni sem árt, végül pedig ismét jött egy vizsgaidőszak - de az SC21 után már volt erőm, időm és kedvem is foglalkozni a javítással, szóval történt egy kevés haladás.

# Hibakeresés

Próbáljuk szűkíteni a hiba lehetséges forrását! Oké, hogy nem ad képet, de ezt vajon mi okozza?

Szerencsére a [műszerkönyvben](https://www.emg.hu/gepkonyvek/EMG_1569.pdf) (a 44. oldaltól kezdődően) van egy egészen jó leírás, ami segít*het* behatárolni a meghibásodást.

Az első pont az alapvető tápellátást, így a biztosítékot, kapcsolót és transzformátort ellenőrzi. Mind jól működik, bár a kapcsolónál ez korábban nem kevés munkámba került.

A második a kisfeszültségű tápegységeket ellenőrzi. Ezek is rendben voltak, a legutóbbi után nem volt kedvük szórakozni velem. Mindenesetre megpróbálkoztam csökkenteni az (amúgy rendben levő) brummot úgy, hogy új kondenzátorokat kapcsoltam párhuzamosan a régiekkel, de azok csak jelentősen rontottak rajta, szóval inkább maradtak a régiek.

A harmadik pont viszont már érdekesebb.
- Állítsuk be a kezelőszerveket (mert amúgy a hibás beállítás is okozhat olyat, hogy nem azt látjuk, amit kell)
- Meg kéne jelennie egy vízszintes fényvonalnak. Ha mégsem, akkor
- Ellenőrizni kell az időeltérítést - pipa, a megadott tranzisztoron pont olyan jel van, aminek lennie kell
- ellenőrizni kell a vízszintes erősítőt - ez is pipa, a kimeneten ott az erősített jel (bár ezt mérni nem olyan triviális, lévén differenciális jel, de egy kétcsatornás szkóp "add" és "invert" funkcióit kombinálva megoldható)
- ellenőrizni kell három helyen a **kivilágosító jelet**. Ez a jel ki- vagy bekapcsolja a fényt a képernyőn, attól függően, hogy éppen mit csinálunk. Ha rajzolunk, akkor be kell kapcsolni, míg amikor éppen a sugarat visszük vissza a kezdőpontba, akkor ki kell kapcsolni.
- ha van jel de még mindig nincs kép, akkor "leellenőrizzük a CRT áramkört"

A kivilágosító jelet háromból csak két helyen ellenőriztem, mivel a harmadik a "tyúkketrec" belsejében volt (lezárt doboz, amiben a nagyfeszültségű tápegység - is - van), és ott nem mertem mérni. Ez a jel a jobb oldali panel egyik áramkörétől indul (itt meg is találtam ahogy kell), majd bemegy a dobozba, ahol ráül egy kb. -900V-os egyenfeszültségű szintre illetve átmegy a *kivilágosító multivibrátor*-on, ami egy *emittercsatolt bistabil multivibrátor*, azaz ha a (nehezen fellelhető) irodalmat jól értelmezem gyakorlatilag egy SR flip-flop. A kimenet megy egyenesen a CRT katódjára. A katódon (illetve az oda menő drótot gombostűvel átszúrva) szintén tudtam mérni.

# Előtét

A probléma csak az, hogy itt már meglehetősen nagy feszültségekkel volt dolgom, és a működő szkópom nem alkalmas ilyen nagy jelek mérésére. Kaphatók persze előosztós mérőfejek, de még az "olcsó kínai" verzió is több mint 30 000 Ft lenne, [a felső határ pedig a csillagos ég](https://hu.farnell.com/tektronix/p6015a-option-1r/high-volt-passive-probe-1000-1/dp/2855078), tehát valami sufni verziót kellett összehoznom (ami összesen nem volt kétezer forint, de jól lábon is lőttem vele magam).

A legegyszerűbb megoldás a klasszikus ellenállás-osztó. A szkóp bemenete $1M\Omega$, tehát ha sorbakötünk vele mondjuk $10M\Omega$-ot, akkor pont 1:11 arányban osztottuk a jelet. Tudtam, hogy a frekvenciamenete közel sem lesz tökéletes, de arra, hogy egy jel ott van-e vagy sem még jónak tűnt. Ezzel a módszerrel megtaláltam a katódon egy jelet, és mivel nem írták, hogy pontosan minek kell lennie, kipipáltam, hogy jó lesz.

Mivel a jel elért a forrásától a célig (még ha egy közbenső állomást nem is ellenőriztem), úgy tűnt, hogy csak az utolsó pont maradt - "leellenőrizzük a CRT áramkört".

# CRT áramkör

Az áramkör kapcsolási rajza a gépkönyv 2/8-as ábrája, [a korábban is linkelt PDF](https://www.emg.hu/gepkonyvek/EMG_1569.pdf) 106. oldalán található.

![]({{imgpath}}/schema.png)

Kiemeltem a fontosabb részeket.
- a jobboldali tölcsérszerű dolog a katódsugárcső (CRT)
- a pirossal bekeretezett rész a nagyfeszültségű tápegység
- a vastag piros vonalak a tápegység `-900V` és `-860V`-os kimenetei
- a vastag kék vonal a tápegység `4.5kV`-os kimenete
- a kékkel bekeretezett rész a korábban említett *kivilágosító multivibrátor*
- a zölddel bekeretezett rész a fényerőszabályozás áramköre

De minek ennyi bonyolult dolog mikor mi csak képeket akarunk kirajzolni?

## Katódsugárcső és működése

Egy "sima" elektroncső is meglehetősen zseniális találmány, de egy CRT még ezt is bőven túlszárnyalja.

### Elektroncsövek

Az elektroncsövek működését igen kiválóan és részletekbe menően magyarázza el *Mr. Carlson* az alábbi videóban, de megpróbálom én is összefoglalni lentebb az alapokat.

{% include youtube.html url="https://youtu.be/oHjZs0bNwEs" %}

Az elektroncsövek működésének alapja a **thermionic emission** (a magyar wiki szerint a **termoelektromos effektus**, de a vacsorámba le merem fogadni, hogy ez hibás, de legalábbis elírás), amit korábban **Edison-effektus**nak is neveztek, bár az specifikusabb. A lényege, hogy egy melegített elektródából (katódból) elektronok lépnek ki, ugyanis a töltések hőenergiája nagyobb mint ami az elektróda elhagyásához szükséges. Ha van a közelben egy másik elektróda (anód), amire a katódhoz képest pozitív feszültséget kapcsolunk, akkor az vonzani fogja ezeket az elektronokat, és létrejön egy áram. Ha viszont az anód alacsonyabb feszültségen van, mint a katód, akkor taszítani fogja az elektronokat, és így nem jön létre áram - tehát csak az egyik irányba folyhat áram, azaz létrejött egy dióda. (Persze mindez csak akkor működik jól, ha az elektronok könnyen mozognak a katód és anód között, azaz - parciális - vákuumban vannak.) **Edison-effektus**nak ezt az egyirányú áramot nevezik.

A sima diódát kiegészíthetik egy harmadik elektródával, a *ráccsal*, ami az anód és katód közé kerül. Attól függően, hogy ezen mekkora feszültség van (a katódhoz képest), befolyásolja őket, azaz az anód-katód áram (pozitív áramiránnyal) a rács-katód feszültségtől függ - azaz ez az eszköz (*trióda*) használható erősítőként. 

A paraméterek további javítása érdekében újabb elektródákat lehet beépíteni, de léteztek olyan csövek is ahol egy tokba két triódát szereltek (például az ebben a szkópban használt `PCC88`-as), sőt olyan cső is volt, amibe majdnem egy komplett rádiót beleintegráltak - hogy az egyéb speciális csövekről amelyek nem is így működnek ne is beszéljek...

### CRT-k

Egy CRT alapjában véve hasonlít egy erősítésre használt elektroncsőhöz - a fűtött katódból kilépő elektronokat pozitív feszültséggel terelgetjük. A fő különbség az, hogy egy pont után egy jó nagy gyorsítófeszültséggel jól felgyorsítjuk őket, majd becsapódnak a képernyőn levő foszforrétegbe, ami erre világítással reagál. 

Beépítenek jó sok elektródát, amik az elektronsugár létrehozásához és alakításához vagy mozgatásához kellenek, de megmarad a rács is, ami az elektronáram szabályozásával a fényerősséget szabályozza - a színes képcsövek működése pedig még bonyolultabb.

Ami viszont közös, hogy valamilyen módon "mozgatják" a sugarat, ez megoldható elektromos vagy mágneses térrel. A TV-képcsövek általában mágnesesek, míg a szkópcsövek általában elektromos teret használnak.

## A D10-170GH

A felhasznált katódsugárcső a `D10-170GH` típus. Online megtaláltam az adatlapját a [Mullard technical handbook - Book two: Valves and tubes - Part two: Electro optical devices, Radiation detectors](https://www.rsp-italy.it/Electronics/Databooks/Mullard/_contents/Mullard%20Book%202%20Part%202%20Valves%201973-11.pdf) (PDF szerinti) 62 oldalától.

Ennek a típusnak 13 elektródáját számoltam meg
- (indirekt fűtésű - $h$) katód $k$
- vezérlőrács $g$
- első gyorsító és asztigmatizmus elektróda (összekötve) $a_1, a_3$
- fókusz elektróda $a_2$
- vízszintes eltérítés elektródapárja $x_1$ és $x_2$
- függőleges eltérítés elektródapárja $y_1$ és $y_2$
- árnyékolások $s_1$ és $s_2$
- utolsó anód és képernyő $a_4$

Szerencsére a legtöbb ezek közül viszonylag egyszerű, egy fix feszültséget kell rákapcsolni, esetleg egy poti kell, amivel az egy adott tartományban szabályozható. Ilyenek a fókusz, asztigmatizmus, árnyékolások, anód és elvileg a katód és rács is, de azok meg vannak bonyolítva. Az eltérítések a két elektróda közötti feszültségtől függenek, ezeket külön kell meghajtani. (A katód és a rács azért nem így működik, mert több okból is kell elektronikusan szabályozni a fényerőt, és így az is rá van kötve ezekre.)

Nem mennék végig az összes feszültségen, de
- a rács és a fókusz a katódhoz közeli feszültségen kell legyen
- a végső anód és képernyőn $+6kV$-os feszültség kell (itt inkább $5.5kV$ van, de működik így is)
- minden más a katódhoz képest kb. $+1000V$-on kell legyen.

Ezeket úgy oldották meg, hogy a katód, a rács és a fókusz kb. $-900V$-on van, és a gyorsítófeszültség $4.5kV$. Az egyéb elektródok a földhöz közeli feszültségen vannak, így egyszerűbbek lesznek az ezekhez tartozó áramkörök.

## Nagyfesz tápegység

Egy aranyos áramkör. A fenti rajzban látható két függőleges fekete vonal jelöli a transzformátort, amire az egész épül. A trafó az adatlap szerint $50kHz$-en van hajtva, de ez nem kifejezetten hangolt, így inkább $25kHz$-nek tűnik.

A trafó fő szekundere középleágazásos, ha jól értem akkor fele-fele arányban felosztva. A szekunderen így kb. $2\times1000V$ feszültség jelenik meg. Ebből egyik $1000V$ egyenirányításra kerül egy vákuumdiódával, ez adja a $-900V$ illetve $-860V$-os tápot, míg a teljes $2\times1000V$ egy két vákuumdiódával és két kondenzátorral felépített feszültségtöbbszörözőre kerül, aminek a kimenetén megjelenik a kb. $4.5kV$.   
(igen, tudom, hogy a számok nem jönnek ki, kettő duplája nem négyésfél, és ezer sem lesz kilencszáz, a pontos számokat viszont nem tudom, és közelítésnek jók ezek)

Van még három másik szekunder is, mint csőfűtés a vákuumdiódáknak, illetve egy sunyi szekunder a primer oldalon mint visszacsatolás az oszcillátor számára.

A $-900V$-os vonalról egy (valamelyest kompenzált) feszültségosztós visszacsatolás van a primer oldalra, amely automatikusan korrigálja a feszültséget, hogy pont jó legyen.

Látható, hogy itt igen nagy feszültségek vannak, ezért még földelt végű bottal sem akartam az áramkörhöz hozzányúlni korábban. Végül sikerült megúsznom, egyszer sem rázott meg egyik sem (lekopogom), ami jónak mondható. 

Az egyik kézi multiméterem $1000V$-ig tud mérni, amivel már tudom ellenőrizni a $-900V$-ot, de a gyorsítófeszültséget esélytelen. Kikapcsolás után szikrázik ha kisütöm a kondit egy földelt csavarhúzóval, szóval erre nem is nagyon gyanakodtam.

Ami viszont érdekes volt, az a jelalak a $-900V$-os tápon, a korábban ismertetett méréssel:

![]({{imgpath}}/szkopernyo.png)

Na most mivel ez egy negatív táp, ezért ez a jel fejre állva értelmezendő, úgy pedig akár rá is ismerhetünk a klasszikus exponenciális kondenzátor-töltődési görbére - ami hirtelen megszakad, majd újraindul - azaz a poti hirtelen kisült. A csúcsérték $102V$, de mivel $1:11$ osztót használtam, ez valójában $1122V$ lesz, ami egyrészt eleve magasabb, mint lennie kéne a feszültségnek, de brummnak főleg sok.

## Visszafejtés

Említettem már, hogy milyen jó a műszerkönyv ehhez a szkóphoz? Tartalmaz minden kapcsolási rajzot, és majdnem mindenről panelrajzot is.    
Na vajon mi az, amiről nincs semmilyen rajz?    
Hát persze, hogy a tyúkketrec belseje!   
Nincs más csak egy kapcsolási rajz, amely alapján nem igazán lehet bent tájékozódni, hogy mi micsoda. 

![]({{imgpath}}/belseje.jpg)

Mint látható, kicsit kusza a belseje...

Na sebaj, ha felismerek pár alkatrészt, akkor már el lehet indulni, és visszafejteni - pont ezt csináltam. A továbbiakban bemutatom pár (már letisztázott) jegyzetem, amit készítettem.

Az egész áramkör szét van dobva több kerámia forrasztólécre. Itt megjegyezném, hogy ezek forrasztásához csakis olyan ónt szabad(na) használni, amiben van $2-4\%$ ezüst is, mert különben tönkremennek. (a gépkönyv csak azt írja, hogy ez *megfelelőbb*, és nem mondja, hogy nem szabad)

Bejelöltem a kapcsolási rajzon, hogy melyik része az áramkörnek melyik forrlécekre van felépítve, illetve pár kábel színét is:
![]({{imgpath}}/elosztas.jpg)

(A sárgával bekeretezett rész a dobozon kívül volt, a doboz hátuljára szerelt forrlécen, míg a felső halványpiros a doboz aljában elhelyezett három forrlécre épül.)

Mint látható, a tápegységet magát a középső, jobb fölső és alsó forrléceken helyezték el. A bal felsőn a KV multivibrátor található, amelyet nem fejtettem vissza.

A középső és jobb felső rész:

![]({{imgpath}}/jegyzet1.jpg)

Illetve az alsó:

![]({{imgpath}}/jegyzet2.jpg)

## Újraépítés

Az előző infókkal felvértezve már neki mertem állni egy javításnak - a középső forrlécpár minden távtartója eltört, csak az alkatrészlábak / kábelek tartották őket a helyükön.

A szétszedés majdnem mindig könnyű. Szépen közben is kiegészítettem a jegyzeteim, hogy minden pontosan a helyére kerüljön vissza. Minden alkatrészt lemostam alkohollal, ugyanis a nagyfeszültség hatására igencsak gyűjtötték a port az elmúlt pár évtizedben.

A forrlécek kiszedése könnyű volt, mivel már konkrétan semmi sem tartotta őket. Nagy örömömre egy kivételével minden távtartó egyben volt, csak a hegyük tört le, de egyet pótolnom kellett. Szerencsére egy két centis színesrúd-darab pont méret volt. A házhoz ezt kétkomponensű ragasztóval rögzítettem, a forrlécek rögzítéséhez viszont ragasztópisztolyt használtam, ugyanis féltem, hogy később esetleg újra kell csináljam. Mindenesetre bevált, még mindig nem engedte el a kötést.

Természetesen mielőtt bármit visszaraktam volna, kimostam a doboz belsejét is alkohollal.

Az újraépítés során pár apróbb módosítást eszközöltem, pár alkatrészt más sorrendben forrasztottam be, így a kábelek könnyebben leszedhetők voltak később. A $680k$-s ellenállás elhelyezésén is variáltam, végül a harmadik verzió lett a végleges.

Összerakás után még mindig pontosan ugyanazt a képet kapom ugyanott mérve (csak az egyenáramú beállítás csúszott el egy picit, de ez a beállító-potméterrel könnyen korrigálható volt), szóval jól raktam össze.

## Hibakeresés

Kérdés, hogy mi okozza ezt a csúnya jelalakot, amikor nekem csak egy sima vízszintes vonalat kéne látnom.

Mivel ezt a tápegység kimenetén mértem, logikus, hogy először is megpróbáltam lekötni róla mindent, ami terheli a kimenetet, hátha az egyik ilyen okozza. Ha így van, akkor majd egyesével visszakötve kiderül, hogy mikor jön elő újra a hiba.

Sajnos nem így lett, mindent lekötve is ott volt a jel.

A következő ötletem az volt, hogy a visszacsatoló ágat megnézem, hogy ott észleli-e ezt. Nem teszi, ami kicsit furcsa volt. Amikor elkezdtem nyomozni, hogy hol tűnik el, azt találtam, hogy már az első ellenállás-kondenzátor páron sem jut át, de az egyenfeszültség viszont jól átmegy.

Gyanakodtam a simítókondenzátorokra is, így a háromból kettőt kiszereltem, a harmadikat meg variáltam, hogy melyiket kötöm be. Mindegyik produkálta ezt a jelet, sőt egy negyedik sem javított rajta, amit szereztem.

### HV ellenállásmérő

Ekkor édesapám egyszer csak előhúzott egy jó régi, leharcolt kábelszigetelés-vizsgáló készüléket valamelyik kacatos dobozából. Már ő is olyasmi állapotban vette ahogy ideadta. Soha nem volt bekapcsolva, a mutatós műszer meg sem mozdult, ráadásul az egészet szigszalag tartotta össze.

Mindenesetre nekifogtam, hogy kijavítom. A mechanikai felépítésnek igazándiból nem volt sok gondja, pár csavar segített rajta, bár így sem tökéletes, mivel pár távtartó eltört. Az elemtartó érintkezőit bedobtam ecetbe, és egy kevés (sok) szenvedés árán sikerült a műszert is életre keltenem - egy ragasztás engedte el a forgórészen belül, illetve a mutatón is görbíteni kellett, hogy ne érjen hozzá se a számlaphoz se az üveghez.

Sajnos mire (egy hét múlva) eszembe jutott az elemtartó az ecetben, már alig maradt belőle valami, viszont külső 6V-os tápegységről még mindig működik a készülék.

$1000V$-on mér ellenállást a kicsike, a felső méréshatára elvileg kb. $1G\Omega$, de mivel a skála nem lineáris (illetve a mutató kicsit görbe), nem fogadnék a pontosságára.

Arra viszont jó lehet, hogy megnézzem, hogy nem húz-e át valami $1000V$-on.

## Áthúzás ellenőrzése

Majdnem minden alkatrészt megnéztem, de egyik sem mutatott ilyesmit. A forrlécre forrasztva sem találtam semmit.

## Számítások

Gondoltam lemérem, hogy milyen gyors kisülését feltételezhetem a kondenzátornak a jelalak alapján. A szkópon megmértem a jel legkisebb és legnagyobb pontja közötti időt, ami $1\mu s$ lett.

Ha a rendszerben $C$ kapacitás van $U$ feszültségre feltöltve és $\Delta t$ idő alatt sül ki, akkor egy $\overline{I}=\frac{C\bullet U}{t}$ átlagos árammal számolhatunk. Nyilván a kisülés nem pont így működik, tehát ennél kisebb és nagyobb áramok is lesznek, de az integrálközépértéktétel szerint (ezt a felhasználást bezzeg nem tanították) lesz pillanat, amikor pont ekkora áram folyik.

Magyarán szólva, itt az átütés csakis földhöz történhet, mert másképpen nem tudna ilyen gyorsan kisülni.

Viszont akkor hogy lehet, hogy mindkét adag simítókondenzátoron ugyan ezt mértem, pedig van köztük több $k\Omega$ ellenállás?

Sok a furcsaság...

Közben viszont majdnem minden alkatrészt kiszereltem, és gyakorlatilag mindent kizártam, ami okozhatja! 

## Újabb mérések

Vettem pár $15M\Omega$-os ellenállást, amiket direkt nagyfeszre ajánlottak. Ezeket a szkóppal sorbakötve elég érdekes jelenséget tapasztaltam:   
Bármennyi ellenállást ($10-25-40M\Omega$) kötök sorba a szkóppal, egyáltalán nem változik ennek a furcsa jelnek az amplitúdója, csak a kondi feltöltési ideje lesz egyre nagyobb (és így a frekvencia egyre kisebb).

Itt csapott arcon az igazság. A kondi, ami ezt csinálja, nem is a vizsgált áramkörben van, hanem a mérésre használt szkópban! Mindeddig `AC` csatolással mértem, azaz még volt egy kondi az $1M\Omega$-s ellenállással sorosan! Ez persze elrontja a feszosztót, és az $1M\Omega$-ra, azaz a szkópra jutó feszültség nagyobb lesz mint számítottam! Még jó, hogy a szkópnak nem lett baja ettől...

`AC`-ról `DC`-re kapcsolva látszott, hogy a tápegység bizony jól működik és nem is zajos.

Szóval két hónapja kergettem egy hibát, amiről kiderült, hogy mérési hiba. Nem mondom, hogy túl boldog voltam, főleg hogy ezzel felmerült egy új kérdés: ha ez is jó, akkor mégis miért nincsen kép?

## Egy (remélhetőleg) jobb mérőzsinór

Találtam azóta egy videót egy házilag készült előosztóról, aminek a használata valószínűleg megmentett volna ettől a baklövéstől, de persze így utólag könnyű okosnak lenni. Mindenesetre ha kell nekem a jövőben ilyesmi, én ezzel a videóval fogom kezdeni a tervezést.

{% include youtube.html url="https://youtu.be/Rl8I4PO66Uw" %}

**folytatása következik**