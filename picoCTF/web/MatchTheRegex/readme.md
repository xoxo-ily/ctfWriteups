# MatchTheRegex #
## Overview ##
100 points

PicoCTF 2023
## Description ##
How about trying to match a regular expression
The website is running here.
### Hint ###
Access the webpage and try to match the regular expression associated with the text field
## Solution ##
The website asks for an input:

<img width="306" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/883b4daa-43c6-428f-9478-322927fdc190">
<br><br>
There's a comment in the source code that tells us that the regular expression pattern is `^p.....F!?`
<br><br>
<img width="421" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/d38c4ae6-f265-4feb-94ca-17d1e0e08320">
<br><br>
This means that the input has to start with `p`, with any five characters after it, then followed by `F`, ending with a `!` that appears 0 or 1 times (meaning it's optional).
<br>
Thus, submitting something like `picoCTF` gives you the flag:
<br><br>
<img width="502" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/0b4331e8-b6b2-4a2f-aeb7-363908799ef1">
<br><br>
Other things that would work include `picoCTF!`, `piiiiiF`, etc.
