# Ready Gladiator 0
## Overview 
100 points

picoCTF 2023
## Description
Can you make a CoreWars warrior that always loses, no ties?
<br><br>
Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/308/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
<br>
`nc saturn.picoctf.net 60950 < imp.red`
### Hints
<ol>
  <li>CoreWars is a well-established game with a lot of docs and strategy</li>
  <li>Experiment with input to the CoreWars handler or create a self-defeating bot
</li>
</ol>

## Solution
To lose in CoreWars, we just need to make a warrior that kills itself everytime, with the `dat` command that bombs itself.
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/89890d73-344e-463b-9a54-bc6460581dd5)

## Resources used
[cool website](https://vyznev.net/corewar/guide.html)
