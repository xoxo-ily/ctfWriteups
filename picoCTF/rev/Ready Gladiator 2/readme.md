# Ready Gladiator 2
## Overview 
400 points

picoCTF 2023
## Description
Can you make a CoreWars warrior that wins every single round?
<br>
Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/283/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
<br>
`nc saturn.picoctf.net 52023 < imp.red`
<br>
To get the flag, you must beat the Imp all 100 rounds.
### Hints
If your warrior is close, try again, it may work on subsequent tries... why is that?

## Solution
We can do this with the [Imp Gate](impgate.red) from the CoreWars docs
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/7f0c482d-6751-48c2-8694-7e041c73e780)
## Resources
[corewars docs](https://www.corewars.org/docs/book1.html#:~:text=code%20self%2Ddestructs.-,%2D%2D3%2D%2D,-Name%3A%20%20%20%20%20%20%20%20%20%20%20Imp%20Gate)
