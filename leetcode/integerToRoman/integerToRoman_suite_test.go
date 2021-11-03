package integerToRoman_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestIntegerToRoman(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "IntegerToRoman Suite")
}
