package atoi_test

import (
	"math"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/dbgoytia/algorithms/atoi"
)

var _ = Describe("Atoi package", func() {

	Describe("Atoi", func() {
		It("Converts a string to a number", func() {
			Expect(atoi.MyAtoi("32")).To(Equal(32))
		})
	})

	Describe("Atoi", func() {
		It("Respects negative numbers", func() {
			Expect(atoi.MyAtoi("-32")).To(Equal(-32))
		})
	})

	Describe("Atoi", func() {
		It("Doesn't care about leading whitespaces", func() {
			Expect(atoi.MyAtoi("      -32")).To(Equal(-32))
		})
	})

	Describe("Atoi", func() {
		It("Reads until first non-digit", func() {
			Expect(atoi.MyAtoi("12341 with words")).To(Equal(12341))
		})
	})

	Describe("Atoi", func() {
		It("If it starts with non-digits, returns a zero", func() {
			Expect(atoi.MyAtoi("with words 12341")).To(Equal((0)))
		})
	})

	Describe("Atoi", func() {
		It("Treats all non-digits as zero.", func() {
			Expect(atoi.MyAtoi("only non-digits.")).To(Equal(0))
		})
	})

	Describe("Atoi", func() {
		It("Knows how to deal with integer overflows (clamp the integer) (negative values)", func() {
			Expect(atoi.MyAtoi("-91283472332")).To(Equal(math.MinInt32))
		})
	})

	Describe("Atoi", func() {
		It("Knows how to deal with integer overflows (clamp the integer) (positive values)", func() {
			Expect(atoi.MyAtoi("91283472332")).To(Equal(math.MaxInt32))
		})
	})

	Describe("Atoi", func() {
		It("Ignores all digits after a dot", func() {
			Expect(atoi.MyAtoi("3.14159")).To(Equal(3))
		})
	})

	Describe("Atoi", func() {
		It("Return a zero when length of string is zero", func() {
			Expect(atoi.MyAtoi("")).To(Equal(0))
		})
	})

	Describe("Atoi", func() {
		It("Returns zero when there's only a signature in the string", func() {
			Expect(atoi.MyAtoi("+")).To(Equal(0))
		})
	})

	Describe("Atoi", func() {
		It("Ignores all digits after intermediate signatuers", func() {
			Expect(atoi.MyAtoi("00000-42a1234")).To(Equal(0))
		})
	})

	Describe("Atoi", func() {
		It("Ignore strings that are only whitespaces", func() {
			Expect(atoi.MyAtoi("  ")).To(Equal(0))
		})
	})
})
