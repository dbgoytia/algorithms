package reverseInteger

import (
	"testing"
	// . "github.com/onsi/ginkgo"
	// . "github.com/onsi/gomega"
)

func TestAdd(t *testing.T) {
	sum := Add(2, 3)
	if sum != 5 {
		t.Errorf("Sum, got: %d, want: %d.", sum, 5)
	}
}

// func TestAdder(t *testing.T) {
// 	RegisterFailHandler(Fail)
// 	RunSpecs(t, "Adder Suite")
// }
