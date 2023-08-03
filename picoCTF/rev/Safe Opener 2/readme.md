# Safe Opener 2
## Overview 
100 points

picoCTF 2023
## Description
What can you do with this file?
<br>
I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/289/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
### Hints
Download and try to decompile the file.

## Solution
doing `strings - SafeOpener.class | grep picoCTF` gives you the flag, no reversing needed

<img width="673" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/6fab9dca-8d77-4406-8658-acb5767c4869">

# picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}
