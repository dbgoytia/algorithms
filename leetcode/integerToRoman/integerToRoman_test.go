package integerToRoman_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/dbgoytia/algorithms/integerToRoman"
)

var _ = Describe("IntegerToRoman", func() {

	testCases := []struct {
		number int
		roman  string
	}{
		{0, ""},
		{1, "I"},
		{2, "II"},
		{4, "IV"},
		{5, "V"},
		{1993, "MCMXCIII"},
		{2018, "MMXVIII"},
		{1111, "MCXI"},
		{2222, "MMCCXXII"},
		{444, "CDXLIV"},
		{555, "DLV"},
		{666, "DCLXVI"},
		{999, "CMXCIX"},
	}

	Describe("Converts integer to roman representation:", func() {
		It("Converts single digit numbers to roman:", func() {
			for _, testCase := range testCases {
				Expect(integerToRoman.IntToRoman(testCase.number)).To(Equal(testCase.roman))
			}
		})
	})

})
