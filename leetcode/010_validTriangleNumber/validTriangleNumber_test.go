package validTriangleNumber_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/dbgoytia/algorithms/010_validTriangleNumber"
)

var _ = Describe("ValidTriangleNumber", func() {

	Describe("Valid Triangle Number", func() {
		nums := []int{2, 2, 3, 4}
		It("Knows when an array is already sorted", func() {
			Expect(TriangleNumber(nums)).To(Equal(3))
		})
	})

	Describe("Valid Triangle Number", func() {
		nums := []int{4, 2, 3, 4}
		It("Knows when an array is scrambled, and sorts it", func() {
			Expect(TriangleNumber(nums)).To(Equal(4))
		})
	})

	Describe("Knows how to deal with empty arrays", func() {
		nums := []int{}
		It("Knows when an array is scrambled, and sorts it", func() {
			Expect(TriangleNumber(nums)).To(Equal(0))
		})
	})

})
