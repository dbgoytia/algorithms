package validTriangleNumber

import (
	"sort"
)

func TriangleNumber(nums []int) int {

	// Deal with empty arrays
	if len(nums) == 0 {
		return 0
	}

	// Sorts the array
	sort.Ints(nums)

	var triangleCount int = 0

	for i := 2; i < len(nums); i++ {
		val := nums[i]
		start := 0
		end := i - 1
		for start < end {
			if nums[start]+nums[end] > val {
				triangleCount += (end - start)
				end--
			} else {
				start++
			}
		}
	}

	return triangleCount
}
