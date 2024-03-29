---
title: Silly stack VM
layout: post
category: prog
---

Avagy a *legegyszerűbb* módszer az első száz fibonacci-szám kiírására pythonban

[Github gist](https://gist.github.com/Sasszem/1f7b1b1fc342d0deffd7d151c21fd1c5)

# Miért

Mind hozzászoktunk már ahhoz hogy kezdő programozók a házijukat kirakják fórumokra vagy kérdés válasz-oldalakra hogy csináljuk meg helyettük. A legtöbben nem reagálnak ilyenkor semmit, mások leszúrják őket amiért nem próbálkoztak megoldani maguk, megint mások elkezdik irányított kérdésekkel terelni őket a helyes megoldás felé, de úgy hogy meg is kelljen dolgozni érte...

Ennek a jelenségnek egy új szintjét érte el az a kedves kommentelő egy Pythonos Facebook-csoportban, aki, miután jelentkezett egy fejlesztői állásra, az online kapott tesztfeladatot kérte hogy oldjuk meg neki. Mondanom sem kell hogy nem lett túl népszerű az ötletével... A feladat amúgy néhány fibonacci-szám kiírása volt. Néhányan elkezdtünk mindenféle működő, ámde a legkevésbé praktikus megoldást küldeni neki - nagyon tetszett például az, amely az `1` mint konstans helyett a

```python
min(random.randrange(1, 100) for _ in range(10000))
```

kifejezést használta, mindemellett naiv rekurzióval dolgozott, tehát exponenciális aszimptotikus futásidővel rendelkezett...

# Az én megoldásom

Engem hirtelen elkapott a "de terveznék egy virtuális gépet"-hangulat. Persze egy ilyen extrémmód bonyolult feladathoz megfelelő virtuális gép is kellett, szóval pár tervezési sajátosság:

- veremalapú
- a felső 3 verem-elem alattiakat NEM lehet elérni
- nincsenek globális változók, csak a verem
- a numerikus literálokat hármas számrendszerben kell megadni
- a `+` parancs összead, a `-` negál, így a kivonás `-+` lesz
- parancs az `o` és az `O`, de szám a `0`
- a nop a `#`
- a `B (branch)` utasítás attól függően hogy ugrott vagy sem vesz le egy vagy két elemet a stack-ről

Egyszóval igyekeztem elég hülyére tervezni, ami valamennyire sikerült is. Nem olyan elvetemült mint pl. a `malbolge` amit konkrétan a lehetetlennel határos programozni, inkább ránézésre ártatlan de belül hülye.

# Fibo

A végső fibonacci-programkód:

```python
v = SVM("1O101o10200#0#1DR+DO101oR1-+D01121SBdRR120JH")
while not v.HALT:
    v.step()
```

(lehagyva a VM implementációját)

A fibonacci lekódolása tovább tartott mint a VM-é. A program kiírja az első 100 darab fibonacci-számot azután kilép.

A teljes program 71 sor hosszú.