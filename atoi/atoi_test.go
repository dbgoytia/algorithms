package atoi_test

import (
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
		It("Reads until first non-digit", func() {
			Expect(atoi.MyAtoi("with words 12341")).To(Equal(0))
		})
	})

	Describe("Atoi", func() {
		It("Treats all non-digits as zero.", func() {
			Expect(atoi.MyAtoi("only non-digits.")).To(Equal(0))
		})
	})

})
