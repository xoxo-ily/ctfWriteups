# Permissions
## Overview
100 points

picoCTF 2023
## Description
Can you read files in the root file?
<br>
The system admin has provisioned an account for you on the main server:
<br>
`ssh -p 60195 picoplayer@saturn.picoctf.net`
<br>
Password: `x+T6aPgE4-`
<br>
Can you login and read the root file?
### Hints
What permissions do you have?

## Solution
If we do `sudo -l` in the terminal, it tells us that 

    User picoplayer may run the following commands on challenge:
        (ALL) /usr/bin/vi

Since this is here, we probably need to use it to solve the challenge. First we can try to run `vi /root`, but nothing shows up.
<br>
However, when we run it as the root user with `sudo vi /root`, we are taken to the netrw page, where we see `flag.txt` inside of the root file
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/a9c7f09a-2e57-47b7-8af9-8d2007b50a8e)
Accessing that file gives us the flag
# picoCTF{uS1ng_v1m_3dit0r_f6ad392b}
