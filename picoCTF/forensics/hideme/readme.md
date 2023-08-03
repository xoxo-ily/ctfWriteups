# hideme
## Overview
100 points

picoCTF 2023
## Description
Every file gets a flag.
<br>
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/257/flag.png).
## Solution
Using `binwalk` on the image reveals that it's hiding another image called `secret/flag.png`, which we can extract:
<br><br>
<img width="716" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/9d9ce5b0-b2af-4242-9c89-82d74dfe2147">
<br><br>
We can then open this image and find that it contains the flag:
<br><br>
![flag](flag.png)
# picoCTF{Hiddinng_An_imag3_within_@n_ima9e_dc2ab58f}
