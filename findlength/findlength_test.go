package findlength_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Findlength", func() {

	Describe("Find Length", func() {

		It("Initial setup", func() {

			input := [...]int{5, 2, 4, 6, 1, 3}
			output := [...]int{1, 2, 3, 4, 5, 6}

			Expect(findlength(input[:], output[:])).To(Equal(0))
		})

	})
})
