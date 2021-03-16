# Xenia Laurencia Maria

- medium
- special

We have a friend, Xenia Laurencia Maria. She is very cool, but sometimes annoying, but mostly cool. She likes to answer with riddles and tasks to our every question. Yesterday we asked her for a password only she knows. She responded with a very large excel sheet... A classic. We've executed it and it does no harm, but runs very slowly. Could you please acquire the password?

https://secchallenge.crysys.hu/Book1.xlsm

MD5: 95a24099cbea584d04bd270dfedf5893 SHA-1: 5b6b24504cc57eff076a91df3af007027b093ccf

_author: tcs_

## Writeup

The attached file is a HUGE Excel XLSM workbook. XLSM means it's using some ancient macros from the times before VBA existed. It's so big it won't open in excel, and just crashes LibreOffice.

I've unzipped it and extracted the one and half gigabyte big `sheet1.xml`. It contains a bazillion of cells with formulas.

Many commands are just garbage, like `WINDOW.MOVE`, `WINDOW.SIZE`, `WAIT` or `ALERT` with static text (and not the flag, sadly). I've written a little script in python that parses the XML and exports the commands filtered:

```python
from xml.dom import pulldom
import re


doc = pulldom.parse('sheet1.xml')
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'c':
        doc.expandNode(node)
        r = node.getAttribute("r")
        d = node.firstChild
        c = d.firstChild
        if c.nodeValue!="0":
            # toxml because it parses strings with &lt; and &gt; wrongly, possibly a bug with the parser
            replaced = d.toxml()[3:-4].replace("&quot;","\"").replace("&lt;","<").replace("&gt;",">")
            replaced = re.sub('WAIT\(NOW\(\)\+"00:00:[0-9]+"\)', "",replaced)
            replaced = re.sub('ALERT\("[^"]+"\)','', replaced)
            replaced = re.sub('WINDOW\.MOVE\([0-9]+,[0-9]+\)','',replaced)
            replaced = re.sub('WINDOW\.SIZE\([0-9]+,[0-9]+\)','',replaced)
            for i in range(10):
                replaced = re.sub(',,',',',replaced)
            print(f"{r}|{replaced}")
```

After that, I've created a list of all used functions after the filtering:
```python
import re
V = set()

with open("parsed2.txt") as f:
    for l in f:
        V.update(re.findall("([A-Z.]+)\(",l))
print(V) 
```

That told me that there are still `ALERT`s - with the results of `CHAR` concatenated together.

Most variables passed to `CHAR` are initialized and the written many times - the random one I've checked was written 32 times! It's always plus or minus the previous value. I've checked if doing them all results in an ascii character, and it does - because if it is not, then reversing it is much harder.

So, my plan was to extract all variables:
```python
import re
import pickle

V = set()
S = []

with open("parsed2.txt") as f:
    for l in f:
        V.update(re.findall("CHAR\(([A-Z]+)\)",l))
        if "&amp;" in l:
            S.append(l)

with open("CHARS","wb") as f:
    pickle.dump(V, f)

with open("STRINGS","wb") as f:
    pickle.dump(S, f) 
```


```python
import pickle
import re


with open("CHARS","rb") as f:
    CHARS = pickle.load(f)

VALS = {}

print("first run:")
with open("parsed2.txt") as f:
    for l in f:
        found = re.findall('DEFINE\.NAME\("([A-Z]+)",([+-]?[0-9]+),3,TRUE\)',l) + re.findall('SET\.NAME\("([A-Z]+)",([0-9+-]+)\)',l)
        if not found and "DEFINE.NAME" in l:
            print(l)
            exit()
        if found:
            for f in found:
                c, v = f
                VALS[c] = int(v)

with open("char_values","wb") as f:
    pickle.dump(VALS,f)

# part 2 - can be done in 2 runs

with open("char_values","rb") as f:
    VALS = pickle.load(f)

print("First pass done")

with open("parsed2.txt") as f:
    for l in f:
        found = re.findall('SET.NAME\("([A-Z]+)",([A-Z]+)([+-][0-9]+)\)',l)
        #if not found and "SET.NAME" in l:
        #    print(l)
        #    exit()
        if found:
            for f in found:
                s,s2,d = f
                assert s==s2, l
                VALS[s] = VALS[s]+int(d)
print("Done")
with open("char_values_final","wb") as f:
    pickle.dump(VALS,f) 
```

And then just print all strings:
```python
import re
import pickle
import string

with open("STRINGS","rb") as f:
    strings = pickle.load(f)

with open("char_values_final","rb") as f:
    CHARS = pickle.load(f)

mapped = [re.findall("CHAR\(([A-Z]+)\)&?a?m?p?;?",s) for s in strings]


for s in mapped:
    res = ""
    fail = False
    for key in s:
        if fail or CHARS[key] > 127 or CHARS[key]<0 or chr(CHARS[key]) not in string.printable:
            print(f"CAN NOT PARSE, '{key}'={CHARS[key]}")
            fail = 1
        else:
            res += chr(CHARS[key])
    if not fail:
        print(res)

```