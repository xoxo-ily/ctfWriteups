# PcapPoisoning
## Overview 
100 points

picoCTF 2023
## Description
How about some hide and seek heh?
<br>
Download this [file](https://artifacts.picoctf.net/c/375/trace.pcap) and find the flag.
## Solution
We can open this file using wireshark.
<br>
At first, we'll see a "Malformed DNS Packet" that tells us the flag is close: 
<br><br>
<img width="1001" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/3f37fc4d-4907-4a2f-8f6c-1bb49f4dde93">
<br><br>
After scrolling through the packets for a bit, we'll find it in number 507:
<br><br>
<img width="1318" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/6ab9ec8b-0a8f-4935-896d-aa5a73a5cb49">
# picoCTF{P64P_4N4L7S1S_SU55355FUL_5b6a6061}
