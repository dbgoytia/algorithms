package insertToTree_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	insertToTree "github.com/dbgoytia/algorithms/011_insert_into_binary_tree"
)

var _ = Describe("001InsertIntoBinaryTree", func() {

	It("Test scenario 1:", func() {
		// Expected tree:
		//		  61
		//       /  \
		//      46  66
		//     / \  / \
		//    43  n n  88
		//   /
		//  39
		root := insertToTree.TreeNode{
			61,
			nil,
			nil,
		}
		// Basic tree
		insertToTree.InsertIntoBST(&root, 46)
		insertToTree.InsertIntoBST(&root, 66)
		insertToTree.InsertIntoBST(&root, 43)
		insertToTree.InsertIntoBST(&root, 39)
		insertToTree.InsertIntoBST(&root, 88)

		Expect(insertToTree.LevelOrder(&root)).To(Equal([]int{61, 46, 66, 43, 88, 39}))

	})

	It("Test scenario 2:", func() {
		// Expected tree:
		//		  4
		//       / \
		//      2   7
		//     / \  / \
		//    1  3
		root := insertToTree.TreeNode{
			4,
			nil,
			nil,
		}
		// Basic tree
		insertToTree.InsertIntoBST(&root, 2)
		insertToTree.InsertIntoBST(&root, 7)
		insertToTree.InsertIntoBST(&root, 1)
		insertToTree.InsertIntoBST(&root, 3)
		insertToTree.InsertIntoBST(&root, 5)
		Expect(insertToTree.LevelOrder(&root)).To(Equal([]int{4, 2, 7, 1, 3, 5}))
	})

	It("Test scenario 3:", func() {
		// Expected tree: (just the root)
		//       5
		root := insertToTree.TreeNode{}
		insertToTree.InsertIntoBST(&root, 5)
		Expect(insertToTree.LevelOrder(&root)).To(Equal([]int{5}))
	})
})
