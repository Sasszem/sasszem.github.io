# Brainfuck

## Analízis

Elolvasva a kódot, láthatjuk hogy bizonyos "parancsokat" hajt végre:
- `+` megnöveli eggyel az aktuális bájtot
- `-` lecsökkenti eggyel az aktuális bájtot
- `>` a következő bájtra lép
- `<` az előző bájtra lép
- `E` kilép
- `p` kiírja az aktuális bájtot
- `i` beolvas az aktuális bájtba
- `D` ha az `is_admin` változó 42, akkor nyerünk, amúgy kiírja hogy nincs jogunk ehhez

Látható, hogy a cél a `D` parancs végrehajtása lenne, de sajnos az `is_admin` alapból 0-ra van állítva, és nem állítjuk át sehol másra, főleg nem 42-re.
Első ránézésre tehát a feladvány megoldhatatlan, soha nem kapjuk meg az üzenetet.

## Megfigyelések

A bájtok, amiken dolgozhatunk, egy 256 elemű tömbben vannak, amely fix 0-kal van feltöltve induláskor.
A programban SEHOL nincs bekódolva, hogy csak ezzel a 256 bájttal dolgozhatunk, azaz ha elég `>`-t vagy `<`-t írunk, akkor más értékeket is átírhatunk a memóriában.
Akkor kérdés hogy milyen változót érdemes átírni, és mire. 
(Elég egyértelmű, hogy az `is_admint` és 42-re)

A kérdés hogy az hol van a bájtjainkhoz képest, és hogy kell átírni 42-re. Ebben segítség, hogy mind a bájttömbünk, mind az `is_admin` egy `struct` része, azaz a fordító szépen egymás mellé pakolja őket a memóriában, hogy együtt kezelhessük őket.
A pontos részletek (előtte vagy utána, pontosan mennyivel) akár változhatnak is fordítótól (és architektúrától) függően, de általában (x86 gépek, GCC fordító) előtte van közvetlenül.
(Erre nincs általános módszer, lehet hogy próbálgatni kell egy kicsit a memóriacímeket amíg jó lesz, de itt mindenkinek elsőre bejött :) )

Tehát "balra" kell 128+1-et menni, és ott találjuk az int-ünket?
Részben - az int ugye minimum 2 bájtot foglal C-ben, tehát VALAMELYIK bájtját találjuk ott.
Amit viszont át kéne majd írnunk, az a "legalsó" bájtja. Az int bájtjai kétféleképpen lehetnek a memóriában - először a legfelső, vagy először a legalsó - tehát vagy kapásból a jó bájton álltunk meg, vagy még menni kell párat (4 bájtos int esetén 3-at).
(be kell valljam olyanról még nem hallottam hogy valakinek az otthoni gépén 3-at kelljen menni még, mindenkinek pont a legalsó volt ott)

Tehát a terv:
- 129-et "balra"
- 42-t beírni

A pontos részleteket innen már elég egyszerű kitalálni

[Vissza](cpuzzles.md)