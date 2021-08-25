package reverseInteger

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestReverser(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Reverser algorithm")
}
