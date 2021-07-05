package insertionsort_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/dbgoytia/algorithms/sorting/insertionsort"
)

var _ = Describe("InsertionSort", func() {

	Describe("Insertion Sort", func() {
		It("returns a test", func() {
			Expect(insertionsort(2)).To(Equal(true))
		})
	})
})
