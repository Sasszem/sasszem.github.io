---
title: "Communications task decoding"
layout: page
---

Writeup by `Sasszem`

We have got some strange text in the mail as the 'communication exercise':

```
TmhneWh2IFlodXZocWJjxZFuIQoKRCBucnBweHFsbsOhZmzDs3YgaWhvZGdkdyBkYyBkb8OhZWVsOgpIamIgdcO2eWxnIGZsbm5odyBuaG9vIG7DqXZjw613aHFsIGQgRllILTIwMjAtMTIzNTEgdsOpdcO8b8OpbmhxYnbDqWpobnXFkW8gZGMgZG/DoWVlbCB2Y2hwc3Jxd3JuIHZjaHVscXc6Ci0gT2hqYmhxIHfDtmVlLCBwbHF3IDE1MDAgbmR1ZG53aHUKLSBRaCBvaGpiaHEgd8O2ZWUgMjAwMCBuZHVkbndodXHDqW8KLSBPaGpiaHEgbsO2Y8OpdXdraHfFkSwgaGpiIHFocCBscWlydXBkd2xueHZxZG4gbHYgZGdtcnEgw6F3IGtkdmNxw6Fva2R3w7MgbHFpcnVww6FmbMOzdyAKLSBPaGpiaHEgZWhxcWggdmPDsywgcGx3IMOpdWxxdywgcGxvYmhxIHbDqXXDvG/DqW5ocWJ2w6lqIGhjIChvaGp2Y8O8bnbDqWpodmhlZSBwaHdkZGdkd3JuIGlob2dyb2pyY8OhdmQpIAotIE9oamJocSB2Y8OzIGQgdsOpdcO8b8OpbmhxYnbDqWogbmxrZHZjccOhb2tkd8OzdsOhasOhdcOzbywgaGNjaG8gbmRzZnZyb2R3cnYgd2hma3FsbmRsZWUgbWhvb2hqxbEgbHFpcnVww6FmbMOzdcOzbwotIE9oamJocSB2Y8OzIGQgecOpZ2huaGPDqXZ1xZFvLCBwaGpob8WRY8OpdnXFkW8KLSBPaGpiaHEgdmPDsyBkIHbDqXXDvG/DqW5ocWJ2w6lqIHfDoWpkZWUgbnJxd2hhd3h2w6F1w7NvIChxaHAgd2hma3FsbmRsIHXDqXZjKSAKLSBPaGpiaHEgc3Jxd3J2LCB3w6F1amJsb2RqcnYsIMOhd2/DoXdrZHfDsyB2Y2h1bmhjaHfFsSwgbsO2eWh3a2h3xZEsIHlsb8OhanJ2Ci0gRCBwcnFnZHdybiBuaHVobiBoasOpdmNobiDDqXYgcWJob3l3ZHFsb2RqIGtob2JodmhuIG9oamJocWhuCi0gUWJycGdkbsOpdmMsIGhqYiB2Y2Ruc3J1d8Ohb3JxIHlkamIgw7ptdsOhamVkcSBzeGVvbG7DoW9rZHfDsyBvaGpiaHEgKHdkdXdkb3BkY2NycSBmw61waHcsIG9oZGdodywgb2hqYmhxIMOpdXdob3BoY2tod8WRIHZjZG5kdmNybnVkIGVycXd5ZCkKLSBPaGpiaHFobiBkIHnDqWrDqXEgaXJ1dcOhdnJuIChwbHFscHhwIDMpLCBwaG9iaG4gaWhva2R2Y3HDoW/DoXZ1ZCBuaHXDvG93aG4gKGQgbmR1ZG53aHV2Y8OhcGVkIHFocCB2Y8OhcMOtd2RxZG4gZWhvaCkKLSBEIGZsbm4gb2hqYmhxIGhqYmhnbCDDqXYgdmRtw6F3CgpEIGZsbm5odyBodXVoIGRjIGgtcGRsb3VoIHnDoW9kdmN4byB5w6F1bXhuIHBkIMOpbWnDqW9saiBwZGpiZHUgcWJob3locSwgZCBpw6FtbyBxaHloIGQgZnZkc2R3cndybiBxaHloIG9oamJocS4gCkRjIMOpdXfDqW5ob8OpdiBkIGlocXdsIHZjaHBzcnF3cm4gw6l2IGQgbnJ1w6FlZWRxIG7DtmPDtm93IGhveWhuIHBocXfDqXEgd8O2dXfDqXFsbi4KIApWcm4gdmxuaHV3LCBodWhncMOpcWJodiBtw6F3w6lucncuCgrDnGd5w7Zjb2h3d2hvOgpLRlZGIHdoZHAK
```

First guess when seeing stuff like this is always base64. It was a hit this time:

```
Nhgyhv Yhuvhqbcőn!

D nrppxqlnáflóv ihodgdw dc doáeel:
Hjb uöylg flnnhw nhoo névcíwhql d FYH-2020-12351 véuüoénhqbvéjhnuőo dc doáeel vchpsrqwrn vchulqw:
- Ohjbhq wöee, plqw 1500 ndudnwhu
- Qh ohjbhq wöee 2000 ndudnwhuqéo
- Ohjbhq nöcéuwkhwő, hjb qhp lqirupdwlnxvqdn lv dgmrq áw kdvcqáokdwó lqirupáflów
- Ohjbhq ehqqh vcó, plw éulqw, plobhq véuüoénhqbvéj hc (ohjvcünvéjhvhee phwddgdwrn ihogrojrcávd)
- Ohjbhq vcó d véuüoénhqbvéj nlkdvcqáokdwóvájáuóo, hccho ndsfvrodwrv whfkqlndlee mhoohjű lqirupáflóuóo
- Ohjbhq vcó d yéghnhcévuőo, phjhoőcévuőo
- Ohjbhq vcó d véuüoénhqbvéj wájdee nrqwhawxváuóo (qhp whfkqlndl uévc)
- Ohjbhq srqwrv, wáujblodjrv, áwoáwkdwó vchunhchwű, nöyhwkhwő, yloájrv
- D prqgdwrn nhuhn hjévchn év qbhoywdqlodj khobhvhn ohjbhqhn
- Qbrpgdnévc, hjb vcdnsruwáorq ydjb úmvájedq sxeolnáokdwó ohjbhq (wduwdopdccrq fíphw, ohdghw, ohjbhq éuwhophckhwő vcdndvcrnud erqwyd)
- Ohjbhqhn d yéjéq iruuávrn (plqlpxp 3), phobhn ihokdvcqáoávud nhuüowhn (d ndudnwhuvcáped qhp vcápíwdqdn ehoh)
- D flnn ohjbhq hjbhgl év vdmáw

D flnnhw huuh dc h-pdlouh yáodvcxo yáumxn pd émiéolj pdjbdu qbhoyhq, d iámo qhyh d fvdsdwrwrn qhyh ohjbhq.
Dc éuwénhoév d ihqwl vchpsrqwrn év d nruáeedq nöcöow hoyhn phqwéq wöuwéqln.

Vrn vlnhuw, huhgpéqbhv máwénrw.

Ügyöcohwwho:
KFVF whdp
```

Well that's more interesting. We can see a lot of accented characters(á, é, ó, ü), but all is garbage. From the accented chars I suspected this was in hungarian (the competition is for hungarians only).

That led me to belive that "D" in "D nrppxqlnáflóv ihodgdw dc doáeel" is for an "A", "Dc" in "Dc éuwénhoév d ihqwl" is an "Az", "Ügyöcohwwho" was "Üdvözlettel" and `KFVF` was `HCSC`.

Now that sure looks like a simple caesar-cipher. First I miscalculated the distance as 4, but it's really 3. Also, only ascii letters were sifted.

I quickly made a simple python script to decode it:

```python
from string import ascii_uppercase, ascii_lowercase


be = """..."""

ki = ""

for l in be:
    if l in ascii_lowercase:
        i = ascii_lowercase.index(l)
        i -= 3
        i = (i + len(ascii_lowercase))%len(ascii_lowercase)
        ki += ascii_lowercase[i]
    elif l in ascii_uppercase:
        i = ascii_uppercase.index(l)
        i -= 3
        i = (i + len(ascii_uppercase))%len(ascii_uppercase)
        ki += ascii_uppercase[i]
    else:
        ki += l

print(ki)
```
