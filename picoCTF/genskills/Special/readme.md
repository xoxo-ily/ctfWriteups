# Special
## Overview
300 points

picoCTF 2023
## Description
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
Start your instance to see connection details.
### Hints
Experiment with different shell syntax

## Solution
This took a lot of experimenting, but what worked in the end was using the `\` to escape the character after it, which made the spellcheck ignore it, allowing things to run properly.
<br>
Using this with `bash` got me out of the spellcheck:

    Special$ bash
    Why go back to an inferior shell?
    Special$ \b\a\s\h
    \b\a\s\h
    ctf-player@challenge:~$

After that, we can just use normal shell commands to get the flag:

    ctf-player@challenge:~$ ls
    blargh
    ctf-player@challenge:~$ cd blargh
    ctf-player@challenge:~/blargh$ cat flag.txt
    picoCTF{5p311ch3ck_15_7h3_w0r57_f578af59}
