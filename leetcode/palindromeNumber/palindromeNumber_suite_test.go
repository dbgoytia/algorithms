package palindromeNumber_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestPalindromeNumber(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "PalindromeNumber Suite")
}
