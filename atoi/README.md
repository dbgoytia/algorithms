Problem statement
---------------

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
	
The algorithm should be as follows:

    1. Read in, and ignore any leading whitespace.

    2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is either a positive or a negative number. Assume postive if neither is present.

    3. Read in next characters until the next non-digit character or end of the input is reached. The rest of the string is ignored.

    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

    5. If it's out of the 32-bit signed integer range (integer overflow), then clamp the integer so that it remains in the range.

    6. Return the integer as final result


This self made Atoi function was a great place to learn about Ascii and unicode in general. For example, did you know that a string is not a slice of runes, but rather a slice of bytes? Interestign huh? That means you can't safely convert each of the bytes to integer as you may encounter some weird characters, like a Kanji 字, leaving some weird results in the output.

Instead I found that the preferred and best approach is to first convert the string (or slice fo bytes) to a slice of runes, to get the ASCII or Unicode value of each of the pieces. Then, you need to convert to int.

Then going back to an ascii table, you get the following values:
Ascii | value |
------|-------|
48    |   0   |
49    |   1   |
50    |   2   |
51    |   3   |
52    |   4   |
53    |   5   |
54    |   6   |
55    |   7   |
56    |   8   |
57    |   9   |
58    |   :   |  

As you can see the ascii codes 48 - 58 represent digits. So to get their values you simply substract the value ascii value of 0 to the ascii digit you're trying to get

```
int32 ( rune - '0')
```
example:
```
int32 ( 51 - '0' ) would be ( 51 - 48 ) resulting in the integer value of 3.
```

Of course, this logic will be simply broken if you go past 58, or anything previous to 48 (ascii), so the algorithm of Atoi needs to be able to handle this.



Results so far:
```
Running Suite: Atoi Suite
=========================
Random Seed: 1625253735
Will run 9 of 9 specs

•••••••••
Ran 9 of 9 Specs in 0.001 seconds
SUCCESS! -- 9 Passed | 0 Failed | 0 Pending | 0 Skipped
PASS

Ginkgo ran 1 suite in 1.863640663s
Test Suite Passed
```



References:
https://blog.golang.org/strings