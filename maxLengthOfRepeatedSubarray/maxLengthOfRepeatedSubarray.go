package maxLengthOfRepeatedSubarray

func FindLength(nums1 []int, nums2 []int) int {

	res1 := findLength_helper(nums1, nums2)
	res2 := findLength_helper(nums2, nums1)

	if res1 > res2 {
		return res1
	}
	return res2

}

func findLength_helper(nums1 []int, nums2 []int) int {

	var max int = 0

	for i := 0; i < len(nums1); i++ {

		// Get all the positions position of nums1[i] in nums2, if exists result will be different than -1
		positions := getPosition(nums1[i], nums2)

		// If the number exists on nums2, process
		if len(positions) != 0 {

			for pos := range positions {
				// Start at the position of i
				x := i
				y := pos
				total := 0
				for nums1[x] == nums2[y] {
					total++

					// Prevent out of index errors
					if x+1 == len(nums1) {
						break
					}
					if y+1 == len(nums2) {
						break
					}

					x++
					y++
				}
				if total > max {
					max = total
				}
			}
		}
	}

	return max
}

// Gets the position of specified number in target slice
func getPosition(num int, nums []int) []int {

	res := []int{}
	for i := 0; i < len(nums); i++ {
		if nums[i] == num {
			res = append(res, nums[i])
		}
	}
	return res
}
