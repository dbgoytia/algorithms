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



References:
https://blog.golang.org/strings