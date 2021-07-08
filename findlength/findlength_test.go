package findlength

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/dbgoytia/algorithms/findlength"
)

var _ = Describe("Findlength", func() {

	Describe("Find Length", func(){
		It("Initial testing", func(){
			input := [...]int{5, 2, 4, 6, 1, 3}
			output := [...]int{1, 2, 3, 4, 5, 6}
			Expect(findLength(input, output)).To(Equal(0))
		})
	})

})
