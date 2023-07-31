# findme #
## Overview ##
100 points

PicoCTF 2023
## Description ##
Help us test the form by submiting the username as test and password as test!
The website running here.
### Hints ###
any redirections?
## Solution ##
We start with a login page: 

<img width="620" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/a1b07a7d-ec21-4746-b7a3-d295d6a72a70">
<br>

We log in with username `test` and password `test!` like it tells us to, and get to this page:
<br><br>
<img width="952" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/26b20790-ae08-414c-8ee0-d2cc4b0c5718">
<br><br>
If we open the Networks tab in developers tools, and go back and log in again, we'll see this:
<br><br>
<img width="232" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/163a6f3d-1e1d-40bd-9941-47629966c5f1">
<br>

After base64 decoding `cGljb0NURntwcm94aWVzX2Fs` and `bF90aGVfd2F5X2JlNzE2ZDhlfQ==`, we get the two parts of the flag, `picoCTF{proxies_al` and `l_the_way_be716d8e}`, respectively.
