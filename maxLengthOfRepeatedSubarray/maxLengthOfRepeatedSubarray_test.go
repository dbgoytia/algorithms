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

})
