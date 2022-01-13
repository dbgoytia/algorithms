package threeSum

import "sort"

func threeSum(nums []int) [][]int {
	threeSums := make([][]int, 0)
	sort.Ints(nums)
	for x, i := range nums {
		c := complement(i, 0)
		hashmap := make(map[int]int)
		twoSum := twoSum(nums[x+1:], c, hashmap)
		if len(twoSum) > 0 {
			for _, res := range twoSum {
				res = append(res, i)
				if isUnique(res, threeSums) {
					threeSums = append(threeSums, res)
				}
			}
		}
	}
	return threeSums
}

func twoSum(nums []int, target int, hashmap map[int]int) [][]int {
	twoSums := make([][]int, 0)
	for pos, n := range nums {
		c := complement(n, target)

		// Check if complement is in hashmap
		if _, ok := hashmap[c]; ok {
			res := []int{c, n}
			twoSums = append(twoSums, res)
			delete(hashmap, c)

		}

		// Add the current number to the seen numbers hashmap
		if _, ok := hashmap[n]; !ok {
			hashmap[n] = pos
		}

	}
	return twoSums
}

func isUnique(slice []int, matrix [][]int) bool {
	unique := true
	for _, slicetwo := range matrix {
		if testEq(slice, slicetwo) {
			unique = false
		}
	}
	return unique
}

func testEq(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func complement(num int, target int) int {
	return target - num
}
