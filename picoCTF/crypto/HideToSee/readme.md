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
Then decoding `krxlXGU{zgyzhs_xizxp_zx751vx6}` with the atbash cipher gives the flag:
```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse = list(reversed(alphabet))

def atbash(msg):
  new = ""
  for l in list(msg):
    if l.lower() in alphabet:
      if l.isupper():
        new += reverse[alphabet.index(l.lower())].upper()
      else:
        new += reverse[alphabet.index(l)]
    else:
      new += l
  return new

f = open("encrypted.txt","r")
enc = f.readline()
print(atbash(enc))
```

# picoCTF{atbash_crack_ac751ec6}
## website that helped
[website](https://stegonline.georgeom.net/checklist)
