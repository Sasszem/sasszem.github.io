---
title: "Seek More Rats"
layout: page
---

- Web Security
- Operations
- Git
- Python
- Medium

Writeup by `Sasszem`

# Description and resources
## Mission brief
Can you break into a corporate Smack Workspace and leak the internal chat messages?

## Instructions
You receive a copy of an in-development CLI tool, designed to read chat messages via the command line. The CLI tool interacts with the Smack API to list the latest messages. This tool was created by a developer working at the company you are trying to break into. Your goal is to carefully inspect the CLI tool and hack into the corporate Smack Workspace of the target company. Also, the developer's computer once crashed while saving some work. Hopefully, that didn't cause any issues...

---

# Writeup

Here's the python file for reading messages:
```python
import requests, os
from datetime import datetime

token = os.environ['SMACK_TOKEN']
channel_id = "C31337"
try:
    r = requests.get("http://api.smack.com/api/conversations.history", params={"token": token, "channel": channel_id})
except:
    print("Request to Smack API failed...")
    exit()

if r.status_code != 200:
    print("Smack API returned error code " + str(r.status_code) +  " with message: " + r.text.replace("\n", ""))
    exit()

# TODO: Implement pretty-printing of messages
# for message in r.json()["messages"]:
```

Not much can be done with this alone, since we don't have a valid `token`, but when cloning it to my computer I noticed that it's version-tracked by git.

`git log` shows 3 commits:
- Add better error handling
- This should be in an env var
- Initial commit

A-HA! So Bob possibly hard-coded the token first, and only later made it an env var. Sweet, but for some reason (maybe that crash?) corrupted the git files so it can't show me what did the `This should be in an env var` commit change (I was interested in the original).

Turns out, git stores diffs and stuff in it's `.git/objects/` directory. I went lazy and wrote a script to decode all - they are mostly just compressed by `zlib`

```python
import zlib
import os
for path, subdirs, files in os.walk(".git/objects/"):
    for name in files:
        path = os.path.join(path, name)

        with open(path,"rb") as f:
            print(path)
            print(zlib.decompress(f.read()))
```

From that, I found a valid token. I made the program use that, then added the missing printing of the messages. One of them directed me to another *channel*, and there I had the flag.