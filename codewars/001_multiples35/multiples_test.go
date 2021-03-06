package multiples

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Multiples of 3 and 5", func() {

	It("should handle basic cases", func() {
		Expect(Multiple3And5(10)).To(Equal(23))
	})

	It("should handle division by zero", func() {
		Expect(Multiple3And5(0)).To(Equal(0))
	})
})
