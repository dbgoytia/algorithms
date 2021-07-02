package atoi_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/dbgoytia/algorithms/atoi"
)

var _ = Describe("Atoi package", func() {

	Describe("Atoi", func() {
		It("Converts a string to a number", func() {
			Expect(atoi.MyAtoi("32")).To(Equal(int32(32)))
		})
	})

	Describe("Atoi", func() {
		It("Respects negative numbers", func() {
			Expect(atoi.MyAtoi("-32")).To(Equal(int32(-32)))
		})
	})

	Describe("Atoi", func() {
		It("Doesn't care about leading whitespaces", func() {
			Expect(atoi.MyAtoi("      -32")).To(Equal(int32(-32)))
		})
	})

	Describe("Atoi", func() {
		It("Reads until first non-digit", func() {
			Expect(atoi.MyAtoi("12341 with words")).To(Equal(int32(12341)))
		})
	})

	Describe("Atoi", func() {
		It("If it starts with non-digits, returns a zero", func() {
			Expect(atoi.MyAtoi("with words 12341")).To(Equal(int32((0))))
		})
	})

	Describe("Atoi", func() {
		It("Treats all non-digits as zero.", func() {
			Expect(atoi.MyAtoi("only non-digits.")).To(Equal(int32(0)))
		})
	})

	Describe("Atoi", func() {
		It("Knows how to deal with integer overflows (clamp the integer) (negative values)", func() {
			Expect(atoi.MyAtoi("-91283472332")).To(Equal(int32(-2147483647)))
		})
	})

	Describe("Atoi", func() {
		It("Knows how to deal with integer overflows (clamp the integer) (positive values)", func() {
			Expect(atoi.MyAtoi("91283472332")).To(Equal(int32(2147483647)))
		})
	})

})
