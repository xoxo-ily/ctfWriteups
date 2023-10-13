# Specialer
## Overview
400 points

picoCTF 2023
## Description
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.
### Hints
What programs do you have access to?

## Solution
Two commands that the shell lets you use are `echo` and `cd`. We can use `echo *` instead of `ls` and `echo "$(<file.txt )"` instead of `cat` to view files, since those two commands aren't allowed.
<br>
We then go through the files and directories until we find the flag in `ala/kazam.txt`
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/13690dfb-afe6-4aa0-ba69-9f60e4cb4c7a)

# picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_49193632}

## Websites that helped
[stack overflow](https://stackoverflow.com/a/22378194)

[another website](https://ubunlog.com/en/alternatives-to-ls-command/)
