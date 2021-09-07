package validparenthesis_test

import (
	"github.com/dbgoytia/algorithms/leetcode/validparenthesis"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("ValidParenthesis", func() {

	Context("when having same parenthesis", func() {

		Context("the parenthesis validator", func() {
			It("should check if every parenthesis closes with the same kind", func() {
				Expect(validparenthesis.Whatever()).Should(Equal(0))
			})
		})

	})

})
