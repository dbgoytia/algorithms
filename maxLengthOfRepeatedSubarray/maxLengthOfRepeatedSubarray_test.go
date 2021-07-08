package maxLengthOfRepeatedSubarray_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/dbgoytia/algorithms/maxLengthOfRepeatedSubarray"
)

var _ = Describe("MaxLengthOfRepeatedSubarray", func() {

	Describe("Max length", func() {
		It("Passes test suite", func() {
			Expect(maxLengthOfRepeatedSubarray.FindLength()).To(Equal(0))
		})
	})

})
