# two-sum
## Overview
100 points

picoCTF 2023
## Description
Can you solve this?
<br>
What two positive numbers can make this possible: `n1 > n1 + n2 OR n2 > n1 + n2`
<br>
Enter them here `nc saturn.picoctf.net 56305`. [Source](https://artifacts.picoctf.net/c/450/flag.c)
### Hints
<ol>
  <li>Integer overflow</li>
  <li>Not necessarily a math problem</li>
</ol>

## Solution
Looking at the source code tells us that there's a function called `addIntOvf` that returns `-1` if there's an interger overflow, and `0` if there is not. 
```c
static int addIntOvf(int result, int a, int b) {
    result = a + b;
    if(a > 0 && b > 0 && result < 0)
        return -1;
    if(a < 0 && b < 0 && result > 0)
        return -1;
    return 0;
}
```
Then later in the code, it shows that if there is an integer overflow, it will give us the flag if either of the numbers is greater than 0. 
<br>
Therefore, we just need to enter 2 positive numbers whose sum will exceed `2147483647`, the upper range for C integer data types
<br><br>
<img width="559" alt="image" src="https://github.com/xoxo-ily/ctfWriteups/assets/68173773/ade9be0b-14ef-40de-9bd2-581ec92fb618">

# picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_76f333c8}
