package bfsLevelOrder

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {

	bfs := make([][]int, 0)

	h := height(root) // calculate this value later on
	n := 0
	for n < h {
		if n == 0 {

		}
		var values []int
		levelOrderHelper(root, n+1, &values)
		bfs = append(bfs, values)
		n += 1
	}

	return bfs
}

func levelOrderHelper(root *TreeNode, level int, values *[]int) {
	if root == nil {
		return
	}
	if level == 1 {
		*values = append(*values, root.Val)
	} else if level >= 1 {
		levelOrderHelper(root.Left, level-1, values)
		levelOrderHelper(root.Right, level-1, values)
	}
}

func height(root *TreeNode) int {
	if root == nil {
		return 0
	} else {
		leftDepth := height(root.Left)
		rightDepth := height(root.Right)

		if leftDepth > rightDepth {
			return leftDepth + 1
		} else {
			return rightDepth + 1
		}
	}
}
