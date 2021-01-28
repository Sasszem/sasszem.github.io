# Havas tájkép

A kép ránézésre nem tartalmaz semmit, teljesen fehér - mégis el van benne rejtve két dolog is

## gyors és egyszerű megoldások

A képet letöltve valamilyen elemzőprogrammal (`zsteg`, `binwalk`) átugorhatunk pár lépést (az egyetlen megoldás `binwalk`-ot használt).

## megoldás

A képet letöltve és valamilyen képszerkesztővel (PhotoShop, GIMP, szinte bármi ami nem Paint) megnézve láthatjuk, hogy nem teljesen egyszínű, valójában egy nagyon picit sötétebb színnel tartalmaz egy feliratot: `cGxhY2Vob2xkZXI=` (páran akik idáig eljutottak `Z`-nek olvasták a `2`-t).

Az egyenlőségjel elárulja, hogy ez Base64-es kódolás, dekódolva azt kapjuk, hogy `placeholder`. Beírva az ellenőrző weblapra:
```
Congratulations!
You have found the fake flag!

Don't worry though!
Here's a hint:
the first lines of the script the image was made with were:

import struct
import zlib
```

Tehát sajnos nem ilyen egyszerű a dolgunk, van itt még más is elrejtve...

Amit viszont leszűrhetünk, hogy valószínűleg mélyebben bele kell néznünk a PNG-be, és valószínűleg tömörített adatokkal is lesz dolgunk (zlib)

## PNG

(["ajánlott irodalom" ha érdekelnek a pontos részletek](http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html))

Kis "mese" a PNG formátum működéséről

Egy PNG fájlban elég sokféle módon szerepelhet képadat, lehet szürkerányalatos kép, színes, átlátszósággal vagy anélkül, a színek lehetnek per-pixel kódolva vagy egy palettából...

Ezenkívül tartalmazhat még mindenféle extra adatokat, leírást, készítés helyét, stb. Ha palettából vannak a színek, akkor a palettát is tárolni kell.

Mindezt a PNG, hasonlóan más formátumokhoz, úgy valósítja meg, hogy különféle típusú "chunk"-okat tartalmaz, bennük adatokkal. Minden "chunk"-nak van neve/típusa, mérete, illetve jár mellé egy ellenőrzőöösszeg (CRC checksum).

Ha belenézünk, a mi PNG képünkön nem látszik hogy bármit "matattak" volna az adatokkal, de ez persze csak azt jelenti hogy a CRC-t újraszámítottam.

Az egyetlen chunk, amelyik `zlib`-tömörített adatot tartalmaz viszont, az az `IDAT`, azaz "image data" chunk. Ha simán kiprinteljük a tartalmát, máris megláthatjuk hogy a végén valamilyen extra adat van: 
> Li4gLyAtLi4gLi0gLS0gLS4gLyAuLi4uIC4tIC0gLiAvIC4uLiAtIC4gLS0uIC8gLS4tLiAuLi4uIC4tIC4tLi4gLi0uLiAuIC0uIC0tLiAuIC4uLg==

Ismét Base64, kitömörítve: 
> .. / -.. .- -- -. / .... .- - . / ... - . --. / -.-. .... .- .-.. .-.. . -. --. . ...

Ami pedig Morze, a jelentése: 
> I DAMN HATE STEG CHALLENGES

Ez beírva az oldalra: 
> Wow, not bad, PM me on discord, and also tell me how you did it!

Igen, amúgy eléggé utálom ezeket a feladatokat, mert baromi sok tippelgetés kell hozzájuk, és ha nem találod el a pontos keresőszavakat, a Google sem segít...

## Az ötlet

A feladat ötletét a 2020-as `Hungarian Cyber Security Challange` (HCSC) egyik feladata (`Rock on Snow`) adta. Egy titkos üzenetet kellett megfejtetni, ehhez adtak:

- egy fura dalszöveget txt-ben
- egy megnyithatatlan PNG képet

A dalszövegről a csapatunkkal kiderítettük hogy egy `Rockstar` nevű "vicc" programozási nyelven írták, és számokat bont prímtényezőkre. Szintén feltűnt hogy a sorok végén sok fura whitespace (space és tab) volt, de nem tudtunk ezzel mit kezdeni.

A PNG képen én dolgoztam. Kiderítettem hogy a "header" chunkból kitörölték a szélesség/magasság értékeket (lenullázták mindkettőt), és ennek megfelelően a checksum is téves volt. 

A PNG formátumba való mélyebb elmerülésem után kiderítettem hogy hogyan függ ezen adatoktól a tömörített adatok mérete (bájtban), és írtam egy kis programot ami próbálgatással kereste az eredetieket. 

Miután harmadjára is kijavítottam az "összes" hibát, meg is találta a helyes kombinációt (és a checksum is helyes volt - ezt nem használtam a keresésnél, mert elfeledkeztem róla) - és a képen olvasható volt egy szöveg.

A következő lépést viszont baromi lassan tettük meg: próbálgatással kiderítettem hogy a tab/space karakterek a dalszöveg végére valószínűleg egy `stegsnow` nevű programból kerültek - ez a program pont így rejt el adatokat szöveges fájlokban. (Előtte tippeltem a `Whitespace` nevű (szintén "vicc") programozási nyelvre, tab/space bináris vagy éppen morze kódra, hármas számrendszerre tab/space/újsorokból, és még sok egyébre). 

Amint megtaláltam ezt a programot, biztos voltam benne, hogy erre utalt a "Rock on Snow" cím. Az adatokat kinyerni viszont még így sem sikerült elsőre, mert a programot többféleképpen is lehet használni, tud tömöríteni is vagy éppen jelszóval levédeni.

Pár próbálkozás után viszont sikerült megtalálni a helyes opciókat, és a jelszó pedig a PNG-ből leolvasott szöveg volt - és meg is találtuk az elrejtett adatot, és megoldottuk a feladatot.

A feladat eleje véleményem szerint nagyon jó volt, de a végén nagyon sokat kellett tippelgetnünk mire eltaláltuk hogy mit is kéne csinálni - és pont ezek miatt utálom ezt a feladattípust...

[Vissza](cpuzzles.md)