# HideToSee
## Overview
100 points

picoCTF 2023
## Description
How about some hide and seek heh?
Look at this image [here](https://artifacts.picoctf.net/c/236/atbash.jpg).
### Hints
Download the image and try to extract it.
## Solution
We can extract the image using [steghide](https://steghide.sourceforge.net/):
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/f6b319c0-fb99-4e20-8e71-adc36e6d9cbe)
<br><br>
Then decoding `krxlXGU{zgyzhs_xizxp_zx751vx6}` with atbash cypher gives the flag
# picoCTF{atbash_crack_ac751ec6}
## website that helped
[website](https://stegonline.georgeom.net/checklist)
