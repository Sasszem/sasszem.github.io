---
layout: post
title: "EMG 1569 javítás, kalibráció és elpakolás"
---

{% include imgpath.md %}
{% include latex.html %}

Az előző rész egy (nem túl) kellemes meglepetéssel zárult: amikor azt hittem hogy mindent kijavítottam, azonnal el kellett valaminek romlania. Az alany nem volt más mint az egyik legösszetettebb mechanikai alkatrész az egész készülékben, az időeltérítés baromi sok áramkört kapcsoló de még több állású forgókapcsolója.

# A forgókapcsolókról általában

![]({{imgpath}}/forgokapcsolo.jpg)

Bár nem a legjobb kép, de azért látszik hogy egyértelműen ez a készülék legnagyobb kapcsolója, ráadásul baromi összetett. Ez egy sokállású forgókapcsoló, magyarul YAXLEY, de angolul több sikerünk lehet a `"rotary switch"` vagy `"wafer switch"` kifejezésekkel. Az alap működése elég egyszerű lenne, egy tengelyen forgó érintkező zár rövidre kettő másik érintkezőt a tárcsán. Egy előnye viszont hogy elég szépen bővíthető, több tárcsával több áramkört is képes lehet kapcsolni egyszerre, illetve adott esetben egy tárcsára is tehetünk több érintkezőt hogy még több áramkört kapcsoljon (persze cserébe ilyenkor kisebb lehet a maximális elfordulása, mert különben a tárcsán kijelölendő tartományok átfednék egymást). A legelső, bár inkább "nulladik" tárcsán pedig a lépéseket létrehozó rugós szerkezet és a végállások ütközői kapnak helyet, illetve kivitelezhető hogy a tengely közepén egy másik tengely is helyet kapjon, amely például egy potmétert forgat, illetve magára a kapcsolóra is szerelhetők passzív alkatrészek.

![]({{imgpath}}/passives.jpg)

A látszólagos egyszerűség mögött viszont megbújik számtalan hibalehetőség, ötven drót a részáramkörökhöz, két tucat kapcsolóra szerelt passzív alkatrész, pár gonosz mechanikai hibapont, viszont meglepően kevés a kontakthiba - és akkor még nem említettem a kedvenc ilyen példányomat, az `EMG-1555` szkóp `EMG-1589-U-592` fiókjának hasonló időeltérítés kapcsolóját, aholis egy főtengelyen két ilyen csatolt YAXLEY mellett még belefért két további tengely finombeállító potmétereknek (a második forgókapcsoló külön forgatásához a forgatógombot ki kell húzni, amúgy együtt forognak).


Egyszóval részben érthető hogy miért mentek ki ezek a kapcsolók a divatból, de azért mégiscsak igen szép műszeralkatrészek, és a hozzáértő mérnökök régen mindent meg tudtak csinálni vele amit csak akartak, és szerencsére elég sokáig szoktak jól működni, ha már ilyen gyakran használt alkatrészek.

A hangsúly a "szoktak"-on van, mert mint említettem ez a példány úgy döntött hogy ő márpedig mindenképpen keresztbe fog tenni nekem, ráadásul valószínűleg azt is tudta magáról hogy pótolhatatlan darab.

# A hibajelenség

Egyszercsak amikor sávot akartam váltani, elég meglepő jelenséget tapasztaltam: nem kattant a kapcsoló! Erősen meglepődtem, az első gondolatom az volt, hogy a forgatógomb lazult meg, viszont ahhoz képest nehezen forgott, ráadásul a sávváltás sikeres volt. Innentől kezdve a kapcsoló úgy viselkedett mint egy analóg potméter, bárhová csavarható volt, sőt, akár körbe is tudtam forgatni, aminek semmiképpen sem lett volna szabad hogy sikerüljön.

Mint kiderült, a probléma a "nulladik" tárcsával volt, ezen tárcsa ugyanis nem forgott együtt a többivel, levált a főtengelyről. Utólag sem tudom hogy mi tartotta rajta (nem csavar vagy hasonló, de a ragasztás sem valószínű), így a javítás sem volt könnyű. Túlzottan kiszerelni sem tudtam az egészet, mivel hat tucat (természetesen csak fehér) kábellel van bekötve, mégpedig a túlsó oldalról, így lehetetlen hozzáférni hogy leforrasszam őket. Ránézésre úgy tűnt hogy leszerelhető róla az említett nulladik tárcsa, de a tengelykapcsolót, amely ezt a részt összeköti a többi tárcsával, nem tudtam leszerelni, így nem lehetett ezt sem leszedni, csak annyit értem el, hogy a rögzítő csavarok oldása után a fenti képeken látható módon félig kibillentettem.

Végül egy viszonylag egyszerű javítási módszer vált be. A tárcsa még mindig erősen súrlódott a főtengelyhez, de a rugós szerkezet jelentős ellenállást fejtett ki a forgása ellen. Utóbbi ellenállás csökkentésével (amit az összetartó, illetve feszítőcsavarok minimális meglazításával oldottam meg) a tengelyhez való súrlódás már elég ahhoz hogy a tárcsa újra együtt forogjon a főtengellyel, és így működjön az egész. Nem tökéletes javítás, de úgy tűnik hogy működik, és jobbat sajnos nem igazán tudtam.

# Indítási mód hiba

Természetesen előjött még egy hiba (valójában ez volt hamarabb, ennek javítása közben romlott el a kapcsoló), nevezetesen az előző részben egyszer már kijavított(nak hitt) indítási mód hiba. Szerencsére ismét csak a beállító potmétert kellett állítani, ami ezúttal szerencsére jobban sikerült.

# Kalibrálás

Ezután viszont szerencsére sikerült rendesen végigcsinálnom a kalibrációt, összesen egy hibaszerű jelenség maradt csak, bizonyos időalapoknál a trigger túl érzékeny lesz, és a fénysugár is furcsán indul. Ennek felderítése vagy javítása viszont bőven ráér, mivel így is eléggé jól működik, a korához képest meglepően kis hibával.

A kalibráció során használtam [az általam korábban írt jegyzetet](https://docs.google.com/document/d/1qmQ0HcECZFvDG5XUfFSKzFTRhJNQkfdh3wTJpYy6CwA/edit?usp=sharing), ami a gépkönyv kalibrációs fejezetét egészíti ki, illetve főbb hibáit javítja. Találtam közben pár hibát a sajátomban is, amelyeket szintén javítottam.

# Ellenőrzés

![]({{imgpath}}/25meg.jpg)

A két bemenetre `25MHz`-es szinuszjelet adtam ellenőrzésképpen (a szkóp sávszélessége papíron pont `25MHz`, valójában a `CH1` csatornát `38MHz`-nek míg a `CH2`-t `22MHz`-nek mértem). Ekkora amplitúdó-különbségre még így sem számítottam, de ennek egy része mint kiderült a kábel miatt volt, ugyanis valahol szakadt.

Mindenesetre egy érdekesebb kérdés a két jel közötti fáziseltérés:

![]({{imgpath}}/szkopernyo.jpg)

Mivel itt a szkóp $0.2\frac{\mu s}{cm}$ módban van, és ráadásul kihúztam a `PULL TO 5X` kapcsolót, $\frac{t}{l}=\frac{0.2}{5}=0.04\frac{\mu s}{cm}=40\frac{ns}{cm}$. Az eltérés két összetartozó zérushely között a jelben kb. egy kis osztás, ami egyötöd nagy osztásnak felel meg, azaz $\Delta t=8 ns$. Feltéve hogy a kábelben a jel a fénysebesség $ 70\% $-ával terjed (általában ebben a típusú kábelben ez jó közelítés), illetve a szkóp két bemenete között nincs időzítésbeli eltérés (valószínűleg van, de nem túl nagy), úgy $\Delta l = c \cdot 0.7 \cdot \Delta t = 1.68m$ - kicsit mellé lőtt a valós kétméteres kábelhossztól, de ez simán ráfogható leolvasási hibára (hiszen kicsit több is az mint egy kis osztás), `1.2` kis osztással számolva $\Delta l = 2.01 m$ ami viszont tűpontos.

Ezzel a példával valamelyest megmutattam hogy a műszer még elég jól működik, közelítő értékeket egész jól lehet számolni még a legfelső sávokban is, ennél sokkal többet pedig gyárilag sem tudott ezen a téren. Az alsó sávokban természetesen jóval pontosabb a leolvasás is, ott sokkal jobban használható.

# Modernizálás

Ha már szkópot javítunk, kicsit modernizálhatunk is ezt-azt rajta. _Szombathy Csaba_, a `BME-HVT` egyik oktatója tartott nemrég egy továbbképzést a `HA5KFU` rádiósklubnak, és ott (a spektrumanalizátorok és mérővevők felépítésén, működésén és használatán kívül) ismertette világuralmi terveit. Az egyik ilyen az volt, hogy amint ő lesz a világ ura, minden oszcilloszkópról eltünteti az `"Auto set"` gombot vagy menüpontot. Mivel az enyémen ilyen nincs, gyorsan raktam egyet rá, hogy legyen majd mit leszedni:

![]({{imgpath}}/autoset.jpg)

Aki ezt a gombot megnyomja, az megérdemli amit kap!

# Elpakolás

Igazi élmény volt a kalibráció végén elrakni ezt a készüléket a "szokásos" helyére, hiszen ezúttal nem azért került oda mert nem működik, hanem mert éppen nincs szükségem rá. Van pár tervem amihez akarom használni (különösen az XYZ modulációja érdekel), de azoknak sajnos várniuk kell.

Viszont úgy rákaptam az `EMG` eszközökre, hogy hirtelen felhalmozódott nálam pár egyéb készülék, oszcilloszkóp, freki és csővoltmérő, amelyek közül természetesen egy sincs ami jól működne (sőt, a legtöbb egyáltalán nem működik). Úgyhogy a régi műszerek javításával foglalkozó sorozatom még távolról sem ért véget!