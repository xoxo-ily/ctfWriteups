# MSB
## Overview 
200 points

picoCTF 2023
## Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
<br>
Download the image [here](https://artifacts.picoctf.net/c/305/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)
### Hints
What's causing the 'corruption' of the image?

## Solution
"MSB" stands for Most Significant Bit, which is "the highest-order place of the binary integer" (wikipedia). Since the image is corrupted, this probably means there's something hidden in the most significant bits of the image.
<br>
So I used a [cool website](https://stegonline.georgeom.net/extract) to extract that data:
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/5f3df806-7496-44dc-9397-3ac298dbfe0a)
<br><br>
A [cool book]() was extracted, with the flag in it
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/55b8f482-7595-4674-a9a8-35d211787f27)
# picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_572ad5fe}
