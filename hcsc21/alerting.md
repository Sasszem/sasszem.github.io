---
title: "Alerting"
layout: page
---

- JavaScript
- Web security
- XSS
- easy

# Description and resources
## Mission brief
In this challenge, your task will be to inject an `alert()` to the webapp exploiting an XSS vulnerability.

## Instructions
You can log in as `john` with password `johnny1`.

---

# Writeup

It was rather easy. I could insert most HTML tags as comment on the challenge website, but no script tags. A simple bypass was the `<img onerror="alert(1)" />`.