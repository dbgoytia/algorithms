15. 3Sum - Medium
=================

link: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


My approach:

With this problem I found out that we can use a hashmap, in which we will be storing "seen" numbers, and within each run we will also be only looking for the complement that sums up to target, this made thinking about the problem a lot easier, still it is not very optimal.

Good things about this problem is that it teaches you how to break down a problem into smaller problems, and still get an answer.
 
```
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

```
Example 2:

Input: nums = []
Output: []
```

```
Example 3:

Input: nums = [0]
Output: []
```

Current solution:
```
Runtime: 2575 ms, faster than 5.85% of Go online submissions for 3Sum.
Memory Usage: 9.6 MB, less than 16.16% of Go online submissions for 3Sum.
```