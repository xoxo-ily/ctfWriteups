# ReadMyCert #
## Overview ##
100 points

PicoCTF 2023
## Description ##
How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file [here](https://artifacts.picoctf.net/c/423/readmycert.csr).
### Hints ###
Download the certificate signing request and try to read it.
## Solution ##
The certificate looks like it's encrypted in base64. Decoding it gives us
```
0‚§0‚�0<1&0$UpicoCTF{read_mycert_57f58832}10U)	ctfPlayer0‚"0
	*†H†÷
�‚�0‚
‚�Ö]{†Ê?ÿ<l4DÍ›øL†£ªZÀk´=Lâ4ÀÄôÂßÒÝê ÙÁð:
í÷*ùníI¤dÿ£¿•¢Á œfpS§Z~JIÿ’0[²9ÜÎé@sû¸„ ¥NOÇ‚ó‡,ÛVÁÀW¿Ûw0Áóµöžåæ+Äsþp¢BhÂôl²=¾pù–‹!lÖ{KD@FP¥ q¨M™1{ýhš°…%Íf©ÿ†lHê¨«0Þ™õ7ÖwúGµˆ*XÕëJ ™`ö,£ô^,û—I½ã¿æE{’JdûµWßDÖßÒÓôáµÃTçU~aQ½¡	B`‰ÄnI0«M� &0$	*†H†÷
	100U%0
+0
	*†H†÷
�‚�x¡Š, Ï¯o1ÇGH¡6RÕ
i÷r_®Ç.Õ|#DèûuP§íò§l‡4ËÄ±jnŸáÙSfU’JÛGJ:uZ:n”+JžÀ6î,\±	]ŽöÂmV·R‹[n)9åókÌ™w¹bÔ_.õÂlÊGåž‘þI]@ÀPUçrnD?æÍ8ÿáB½dˆà–íé˜e*õõX!2lêzj ðÇƒ¶Òn?p†Õk)êüöh0äi ½ÅgßË;]¸‘]pµDd§´UòÔ ÔwžH…*�Ù¡tùûŸ†¢C<ä’““½/õF{fP»)¾7"$mðf#á^sï›8
```
with the flag in it. 
# picoCTF{read_mycert_57f58832}
