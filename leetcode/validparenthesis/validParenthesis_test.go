package validParenthesis_test

import (
	"github.com/dbgoytia/algorithms/validParenthesis"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("ValidParenthesis", func() {

	Context("when having same parenthesis", func() {

		Context("the parenthesis validator", func() {
			It("should check if every parenthesis closes with the same kind", func() {
				Expect(validParenthesis.IsValid("()")).Should(Equal(true))
			})
			It("should be able to detect differentt kind of parentheses", func() {
				Expect(validParenthesis.IsValid("{}")).Should(Equal(true))
			})
			It("should detect when there's a missing closing parentheses", func() {
				Expect(validParenthesis.IsValid("(")).Should((Equal(false)))
			})
		})
	})

	Context("when havin mixed parentheses", func() {
		Context("the validator", func() {
			It("should understand nested parentheses", func() {
				Expect(validParenthesis.IsValid("{[]}")).Should(Equal(true))
			})
			It("should detect when there's a missing colsing parentheses", func() {
				Expect(validParenthesis.IsValid("{(")).Should(Equal(false))
			})

		})
	})

})
