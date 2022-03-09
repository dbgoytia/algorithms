package binaryTree

type binaryTreeNode struct {
	val   int
	left  *binaryTreeNode
	right *binaryTreeNode
}

// Creates a new node in the binary tree
func (n *binaryTreeNode) NewNode() {

}

// Inserts a new node on the binary tree
// or returns an error otherwise
func (n *binaryTreeNode) InsertNode() {
}

// Returns true if Item exists in tree
func (n *binaryTreeNode) Search(value int) bool {
	return true
}

// Visits all nodes in-order traversing
func (n *binaryTreeNode) InOrderTraverse() {
}

// Visits all nodes in pre-order traversing
func (n *binaryTreeNode) PreOrderTraverse() {

}

// Visits all nodes with post-order traversing
func (n *binaryTreeNode) PostOrderTraverse() {

}

// Returns item with the min value stored in tree
func (n *binaryTreeNode) Min() int {
	return 0
}

// Returns item with the max value stored in tree
func (n *binaryTreeNode) Max() int {
	return 0
}

// Removes the item from the Binary tree
func (n *binaryTreeNode) Remove(t binaryTreeNode) {
}

// Prints a CLI readable rendering of the tree
func (n *binaryTreeNode) String() {

}
