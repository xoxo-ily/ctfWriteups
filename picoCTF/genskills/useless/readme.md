# useless
## Overview
100 points

picoCTF 2023
## Description 
There's an interesting script in the user's home directory
The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
## Solution
We first ssh into the server with `ssh picoplayer@saturn.picoctf.net -p [port #]`. There is a file named "useless" that doesn't do much, but seeing as one of the challenge tags is `man`, we try `man useless`, which gives us the flag at the bottom.
# picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6173}
