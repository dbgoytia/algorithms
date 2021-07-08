package insertionsort

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

const testName string = "Insertion sort "

var _ = Describe(testName, func() {

	Describe(testName, func() {
		It("Sample", func() {

			input := [...]int{5, 2, 4, 6, 1, 3}
			output := [...]int{1, 2, 3, 4, 5, 6}

			Expect(insertionsort(input)).To(Equal(output))
		})
	})
})
