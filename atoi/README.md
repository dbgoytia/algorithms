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
Random Seed: 1624629142
Will run 6 of 6 specs

•
------------------------------
• Failure [0.000 seconds]
Atoi package
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:10
  Atoi
  /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:18
    Respects negative numbers [It]
    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:19

    Expected
        <int32>: -268
    to equal
        <int32>: -32

    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:20
------------------------------
• Failure [0.000 seconds]
Atoi package
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:10
  Atoi
  /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:24
    Doesn't care about leading whitespaces [It]
    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:25

    Expected
        <int32>: -1777776268
    to equal
        <int>: -32

    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:26
------------------------------
• Failure [0.000 seconds]
Atoi package
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:10
  Atoi
  /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:30
    Reads until first non-digit [It]
    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:31

    Expected
        <int32>: 316595355
    to equal
        <int>: 12341

    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:32
------------------------------
• Failure [0.000 seconds]
Atoi package
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:10
  Atoi
  /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:36
    Reads until first non-digit [It]
    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:37

    Expected
        <int32>: -669916427
    to equal
        <int>: 0

    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:38
------------------------------
• Failure [0.000 seconds]
Atoi package
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:10
  Atoi
  /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:42
    Treats all non-digits as zero. [It]
    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:43

    Expected
        <int32>: -2111109276
    to equal
        <int>: 0

    /Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:44
------------------------------


Summarizing 5 Failures:

[Fail] Atoi package Atoi [It] Respects negative numbers 
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:20

[Fail] Atoi package Atoi [It] Doesn't care about leading whitespaces 
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:26

[Fail] Atoi package Atoi [It] Reads until first non-digit 
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:32

[Fail] Atoi package Atoi [It] Reads until first non-digit 
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:38

[Fail] Atoi package Atoi [It] Treats all non-digits as zero. 
/Users/diego_canizales/go/src/github.com/dbgoytia/algorithms/atoi/atoi_test.go:44

Ran 6 of 6 Specs in 0.002 seconds
FAIL! -- 1 Passed | 5 Failed | 0 Pending | 0 Skipped
--- FAIL: TestAtoi (0.00s)
FAIL

Ginkgo ran 1 suite in 7.470324547s
Test Suite Failed
```



References:
https://blog.golang.org/strings