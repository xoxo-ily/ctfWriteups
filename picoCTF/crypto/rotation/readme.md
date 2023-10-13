# rotation
## Overview
100 points

picoCTF 2023
## Description
You will find the flag after decrypting this file
Download the encrypted flag [here](https://artifacts.picoctf.net/c/389/encrypted.txt).
### Hints
Sometimes rotation is right
## Solution
The encrypted flag is `xqkwKBN{z0bib1wv_l3kzgxb3l_i4j7l759}`, which is encrypted with a caesar (rotation) cipher. 

Since we know the first character of the plaintext should be `p`, we can use math to find the rotation we need to rotate `x` to `p`, and then rotate it to give us the flag.

```python
f = open("encrypted.txt","r")
enc = f.readline()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# since x comes after p in the alphabet, we subtract the difference between the two from 26 to get the rotation
rot = 26+alphabet.index('p')-alphabet.index('x')

def rotate(enc, rot):
  plain = ""
  for l in list(enc):
    if l.lower() in alphabet:
      if l.isupper():
        plain += alphabet[(alphabet.index(l.lower())+rot)%26].upper()
      else:
        plain += alphabet[(alphabet.index(l)+rot)%26]
    else:
      plain += l
  return plain

print(rotate(enc,rot))
```

# picoCTF{r0tat1on_d3crypt3d_a4b7d759}
