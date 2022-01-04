Given the triangle of consecutive odd numbers:

             1
          3     5   
       7     9    11   
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

Explanation:
            1 -> 1
          3     5  -> 8  
       7     9    11    -> 27
   13    15    17    19  -> ...
21    23    25    27    29
...

It means that the sum of each row is just going to be the cube root of the level,

examples: 
* for level 2, the cube root is going to be 8.
* for level 3, the cube root is oing to be 27.