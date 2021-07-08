package maxLengthOfRepeatedSubarray_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/dbgoytia/algorithms/maxLengthOfRepeatedSubarray"
)

var _ = Describe("MaxLengthOfRepeatedSubarray", func() {

	Describe("Max length", func() {
		It("Detect repeated different numbers", func() {

			nums1 := []int{1, 2, 3, 2, 1}
			nums2 := []int{3, 2, 1, 4, 7}
			res := maxLengthOfRepeatedSubarray.FindLength(nums1, nums2)

			Expect(res).To(Equal(3))
		})
	})

	Describe("Max length", func() {
		It("Detects repeated same numbers", func() {

			nums1 := []int{0, 0, 0, 0, 0}
			nums2 := []int{0, 0, 0, 0, 0}
			res := maxLengthOfRepeatedSubarray.FindLength(nums1, nums2)

			Expect(res).To(Equal(5))
		})
	})

	Describe("Max length", func() {
		It("Compares longest repeated in both of the permutations available", func() {

			nums1 := []int{0, 0, 0, 0, 0, 0, 1, 0, 0, 0}
			nums2 := []int{0, 0, 0, 0, 0, 0, 0, 1, 0, 0}
			res := maxLengthOfRepeatedSubarray.FindLength(nums1, nums2)

			Expect(res).To(Equal(9))
		})
	})

	Describe("Max length", func() {
		It("A number can appear more than once in the opposite array", func() {

			nums1 := []int{1, 0, 1, 0, 0, 0, 0, 0, 1, 1}
			nums2 := []int{1, 1, 0, 1, 1, 0, 0, 0, 0, 0}
			res := maxLengthOfRepeatedSubarray.FindLength(nums1, nums2)

			Expect(res).To(Equal(6))
		})
	})

	Describe("Max length", func() {
		It("Detects a single digit repetition", func() {

			nums1 := []int{5, 14, 53, 80, 48}
			nums2 := []int{50, 47, 3, 80, 83}
			res := maxLengthOfRepeatedSubarray.FindLength(nums1, nums2)

			Expect(res).To(Equal(1))
		})
	})

	Describe("Max length", func() {
		It("Detects a single digit repetition", func() {

			nums1 := []int{83, 79, 64, 67, 90, 29, 8, 11, 70, 19}
			nums2 := []int{74, 66, 27, 16, 22, 79, 64, 67, 90, 29}
			res := maxLengthOfRepeatedSubarray.FindLength(nums1, nums2)

			Expect(res).To(Equal(5))
		})
	})

})
