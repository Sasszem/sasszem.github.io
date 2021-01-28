# Dinamikus memória

## Analízis

Mélyebb átnézés nélkül is viszonylag egyértelmű, hogy a célunk a 15-ös sor (`printf("You won!\n");`) végrehajtása lenne, ennek pedig feltétele (14-es sor, `if (*admin_flag==12852) {`) hogy az `admin_flag` által mutatott int értéket beállítsuk egy adott értékre - ez lenne tehát a cél.

Ha lefordítjuk a programot (én GCC-t használtam), kapunk egy figyelmeztetést:
```
cursedheap.c:13:5: warning: format not a string literal and no format arguments [-Wformat-security]
   13 |     snprintf(str, 4096, line);
      |     ^~~~~~~~
```
ami ad egy tippet a későbbiekhez.

A program eleje ránézésre ártatlan inicializálás
- foglalunk egy 1024 elemű `int` tömböt `state` néven
- **elmentjük az utolsó elemének címét** `admin_flag` néven
- kinullázzuk ezt az elemet
- **felszabadítjuk a foglalt memóriát**

Nem véletlenül emeltem ki ezt a két sort, ugyanis ezek miatt most van egy `admin_flag` nevű `int` pointerünk ami olyan memóriára mutat, amely már nem a mienk. Az ilyenektől hagyományosan óvva intenek mindenkit, mivel mindenféle problémákhoz vezethet ha ilyet próbálunk használni - meg is tesszük, a 14-es sorban megpróbáljuk olvasni!

Szóval nemhogy az `admin_flag` által mutatott memóriába nem tudunk írni, de a program még fel is szabadítja ezt, tehát a további sorsa ismeretlen. Vagy mégsem?

A 11-es sor (`char* str = malloc(4096);`) újabb memóriafoglalást végez. Kis szerencsével lehetséges hogy pontosan ugyan azt a memóriablokkot kapjuk, mint korábban. (4 bájtos int típus esetén még a mérete is megegyezik).

Ezután `scanf()`-el beolvasunk 128 karaktert (egy újonnan foglalt pufferbe), és ezeket `snprintf()`-eljük `str`-be - tehát nem is lesz nehéz beírni ezt a számot ASCII karakterek formájában.

Egy nehézség még hátra van: a beírandó érték a 4096 elemű tömb végén található, de a program csak 128 karaktert olvas tőlünk.

A megoldás, amit a hibaüzenet is sugallt: `snprintf`. Ha egy `*printf`-es formátumot írnunk be, könnyen rávehetjük az `snprintf`-et hogy írjon több karaktert mint ahányat kapott. Erre egy jó módszer egy `padding` beállítása lehet ([példa](https://stackoverflow.com/a/293448/4379569)), de sajnos ahhoz kéne egy formázandó érték is.

Egy elsőre meglepő dolog a `*printf` függvényekkel, hogy hogyan viselkednek ha hibás formátunot kapnak. Ha kipróbáljuk a `printf("%d\n");`-t akkor valamilyen hibát várnánk, de helyette csak kiír egy számot, ami "hülyeség" (valójában van benne rendszer, de ez most annyira nem fontos). 

A lényeg viszont, hogy minket nem zavar ha egy hülyeség számot ír ki, csak az a fontos, hogy ezt is tudjuk formázni.

A működő megoldást nem lövöm le, játszani kell vele egy kicsit hogy milyen széles padding-al kell formázni, illetve ki kell találni hogy milyen karakterek ASCII kódjának felel meg a 12852.

Nem nehezebb mint egy dr. Fleiner-féle SzA feladat, szóval hajrá!

[Vissza](cpuzzles.md)