package insertToTree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func InsertIntoBST(root *TreeNode, val int) *TreeNode {

	if root == nil {
		return &TreeNode{val, nil, nil}
	} else {
		if val < root.Val {
			if root.Left == nil {
				root.Left = &TreeNode{val, nil, nil}
			} else {
				InsertIntoBST(root.Left, val)
			}
		} else {
			if root.Right == nil {
				root.Right = &TreeNode{val, nil, nil}
			} else {
				InsertIntoBST(root.Right, val)
			}
		}
	}
	return root
}

func constructLevel(root *TreeNode, h int, levelOrder *[]int) {

	if root == nil {
		return
	}

	if h == 1 {
		*levelOrder = append(*levelOrder, root.Val)
	}

	if h > 1 {
		constructLevel(root.Left, h-1, levelOrder)
		constructLevel(root.Right, h-1, levelOrder)
	}
}

func heightOfTree(root *TreeNode) int {

	if root == nil {
		return 0
	}

	var left = heightOfTree(root.Left)
	var right = heightOfTree(root.Right)

	if left > right {
		return left + 1
	} else {
		return right + 1
	}
}

func LevelOrder(root *TreeNode) []int {

	levelOrder := make([]int, 0)

	if root == nil {
		return levelOrder
	}

	height := heightOfTree(root)

	for i := 1; i <= height; i++ {
		constructLevel(root, i, &levelOrder)
	}

	return levelOrder
}

// func main() {
// 	// Expected tree:
// 	//		  61
// 	//       /  \
// 	//      46  66
// 	//     / \  / \
// 	//    43  n n  88
// 	//   /
// 	//  39
// 	root := TreeNode{
// 		61,
// 		nil,
// 		nil,
// 	}
// 	// Basic tree
// 	insertIntoBST(&root, 46)
// 	insertIntoBST(&root, 66)
// 	insertIntoBST(&root, 43)
// 	insertIntoBST(&root, 39)

// 	// Insert
// 	insertIntoBST(&root, 88)

// 	// Inserts
// 	levelOrder(&root)
// }
