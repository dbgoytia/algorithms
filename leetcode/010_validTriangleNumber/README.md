Problem statement
==================

Given an integer array *nums*, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle. 

See the Triangle Inequality Theorem:

"The sum of the lengths of any two sides of a triangle, has to be greater than the third side."

Examples:

Example 1.-
```
nums = [2,2,3,4]

# We have to find all numbers bigger than the number we're exploring

sort(nums)

Available triangles:
2,2,3 (when visiting the first 2)
2,3,4 (when visiting the first 2)
2,3,4 (when visiting the second 2)

Answer: 3
```

Example 2.-

```
nums = [4,2,3,4]

sort(nums) = [2,3,4,4]

Available triangles:
2,3,4 (when visiting the 2 with first 4)
2,3,4 (when visiting the 2, with second 4)
2,4,4 (when visiting the 2)
3,4,4 (when visiting the 3)

Answer: 4
```

Results so far:

```
Running Suite: ValidTriangleNumber Suite
========================================
Random Seed: 1626394721
Will run 3 of 3 specs

•••
Ran 3 of 3 Specs in 0.002 seconds
SUCCESS! -- 3 Passed | 0 Failed | 0 Pending | 0 Skipped
PASS

Ginkgo ran 1 suite in 2.266416526s
Test Suite Passed

Leetcode:
Beats 100% of golang submissions
```