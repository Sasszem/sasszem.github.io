# Jelszavas belépés

## Analízis

A program generál egy 8 karakteres random jelszót, majd kér egy nevet, üdvözöl, és kéri a (most generált) jelszót. Ha nem sikerül eltalálnunk, akkor vesztettünk, amúgy nyertünk.

Ránézésre a jelszót esélytelen eltalálni, hiszen random...

(a kódban is felhívtam rá a figyelmet, hogy ez a randomgenerálás nem biztonságos, viszonylag könnyen lekövethető amúgy, hiszen `time(NULL)`-al van seedelve, aminek a felbontása nem olyan nagy, egyszerre indítva egy másik példányt a két program pontosan ugyan azt a jelszót generálná - de nem akartam ezzel bonyolítani)

## Megoldás

Egy nagyon egyszerű hiba van a programban, a következő sorban:

`strncpy(strings.name, buffer, 32);`

Általában a fordító tiltakozni is szokott emiatt (persze most hogy ki akartam másolni az üzenetet nem tette), de a probléma: az `strncpy` nem biztos hogy lezárja a string-et 0-val.

Azaz, ha egy hosszabb szöveget másoltunk egy kisebb pufferbe, akkor nem biztos hogy a másolat érvényes C-string - azaz nem biztos hogy az utolsó bájtja 0.

Ez akkor fordulhat elő, ha a forrásszöveg hosszabb volt mint a célpuffer - ilyenkor a függvény simán átmásol annyi karaktert amennyit tud, aztán megáll.

Na de mi történik mikor egy érvénytelen szöveget megpróbálunk kiírni? Mindent kiírunk a következő 0-ás bájtig. Mi lesz itt ez a minden? A struct elrendezése miatt nem más mint a jelszavunk!

Tehát:
- 32 és 64 karakter közötti "nevet" beírni
- leolvasni a jelszót
- beírni a jelszót

[Vissza](cpuzzles.md)