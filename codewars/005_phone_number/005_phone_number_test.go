package phoneNumber_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/dbgoytia/algorithms/codewars/005_phone_number"
)

var _ = Describe("005PhoneNumber", func() {
	It("should return a valid phone number", func() {
		Expect(CreatePhoneNumber([10]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 0})).To(Equal("(123) 456-7890"))
	})
	It("should deal with only zeros", func() {
		Expect(CreatePhoneNumber([10]uint{})).To(Equal("(000) 000-0000"))
	})
})
