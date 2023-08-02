# who is it
## Overview
100 points

picoCTF 2023
## Description
Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
<br>
Can you help us identify whose mail server the email actually originated from?
<br>
Download the email file [here](https://artifacts.picoctf.net/c/499/email-export.eml). Flag: picoCTF{FirstnameLastname}
### Hints 
whois can be helpful on IP addresses also, not only domain names.

## Solution
Opening the email file, we see the IP `173.249.33.206` stated a few times as the IP of the sender. 
<br>
Searching it up on [whois](https://www.whois.com/whois/173.249.33.206) gives us the name of the owner of the mail server:
<br><br>
![image](https://github.com/xoxo-ily/ctfWriteups/assets/68173773/8603b319-744f-4a39-88dc-a3bfe76e4092)
# picoCTF{WilhelmZwalina}
