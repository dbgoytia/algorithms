package reverseInteger_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/dbgoytia/algorithms/007_reverseInteger"
)

var _ = Describe("ReverseInteger", func() {

	Describe("Reverse", func() {

		It("Reverses an postivie integer", func() {
			reverse := Reverse(123)
			Expect(reverse).To(Equal(321))
		})

		It("Reverses an negative integer", func() {
			reverse := Reverse(-123)
			Expect(reverse).To(Equal(-321))
		})

		It("Rounds up leftmost zeros", func() {
			reverse := Reverse(120)
			Expect(reverse).To(Equal(21))
		})

		It("Deals with zeros", func() {
			reverse := Reverse(0)
			Expect(reverse).To(Equal(0))
		})

		It("Deals with positive integer overflows, preflight", func() {
			reverse := Reverse(1534236469)
			Expect(reverse).To(Equal(0))
		})

		It("Deals with positive integer overflows, postflight", func() {
			reverse := Reverse(9646324351)
			Expect(reverse).To(Equal(0))
		})

		It("Deals with negative integer overflows, postflight", func() {
			reverse := Reverse(-2147483648)
			Expect(reverse).To(Equal(0))
		})

	})

})
