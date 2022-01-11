package cubes_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/dbgoytia/algorithms/codewars/006_pile_of_cubes"
)

var _ = Describe("006PileOfCubes", func() {
	It("should handle basic cases", func() {
		Expect(FindNb(4183059834009)).To(Equal(2022))
		Expect(FindNb(24723578342962)).To(Equal(-1))
	})
})
