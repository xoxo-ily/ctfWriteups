# Ready Gladiator 1
## Overview 
200 points

picoCTF 2023
## Description
Can you make a CoreWars warrior that wins?
<br>
Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/409/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
<br>
`nc saturn.picoctf.net 60883 < imp.red`
<br>
To get the flag, you must beat the Imp at least once out of the many rounds.
### Hints
You may be able to find a viable warrior in beginner docs
## Solution
We can accomplish this using the [Imp Gate](impgate.red) in the CoreWars docs:

![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/f878257a-ea18-4a29-a135-2de129b0573e)

## Resources used
[corewars docs](https://www.corewars.org/docs/book1.html#:~:text=code%20self%2Ddestructs.-,%2D%2D3%2D%2D,-Name%3A%20%20%20%20%20%20%20%20%20%20%20Imp%20Gate)
