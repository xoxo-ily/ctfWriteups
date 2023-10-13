# FindAndOpen
## Overview
200 points

picoCTF 2023
## Description
Someone might have hidden the password in the trace file.
<br>
Find the key to unlock [this file](https://artifacts.picoctf.net/c/496/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/496/dump.pcap) might be good to analyze.
### Hints
<ol>
  <li>Download the pcap and look for the password or flag.
</li>
  <li>Don't try to use a password cracking tool, there are easier ways here.
</li>
</ol>

## Solution
We can open the pcap file with [wireshark](https://www.wireshark.org/download.html).
<br>
We find `VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=`, in packet No. 48, encrypted in base64:
<br><br>
<img width="1179" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/d5056307-b0c9-48bd-87e8-edddda827cd2">
<br><br>
It decrypts to `This is the secret: picoCTF{R34DING_LOKd_`, which contains the first half of the flag. 
<br>
The packets before and after it contain hints: "Could the flag have been splitted?" and "Maybe try checking the other file?"
<br>
Using the first half of the flag as the password to open the zip file, we get a single file containing the flag
# picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}
