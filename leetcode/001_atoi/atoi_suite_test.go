package atoi_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestAtoi(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Atoi Suite")
}
