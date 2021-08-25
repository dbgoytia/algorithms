package palindromeNumber

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

const testName string = "Palindrome number"

var _ = Describe(testName, func() {

	Describe(testName, func() {
		It("Recognizes when it's not a palindrome", func() {
			Expect(isPalindrome(123)).To(Equal(false))
		})
	})

	Describe(testName, func() {
		It("Recognizes when it's a palindrome", func() {
			Expect(isPalindrome(121)).To(Equal(true))
		})
	})

	Describe(testName, func() {
		It("Recognizes when it's a palindrome", func() {
			Expect(isPalindrome(1001)).To(Equal(true))
		})
	})

	Describe(testName, func() {
		It("Doesn't care about negative palindromes", func() {
			Expect(isPalindrome(-121)).To(Equal(false))
		})
	})

})
