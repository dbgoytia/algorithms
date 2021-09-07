package validparenthesis_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestValidParenthesis(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "ValidParenthesis Suite")
}
