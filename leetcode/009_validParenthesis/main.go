package validParenthesis

import "fmt"

type Stack []string

// When pushing, save at the beginning of the stack
func (s *Stack) Push(str string) {
	*s = append(*s, str)
}

// Check for next element in stack
func (s *Stack) Peek() string {

	if s.isEmpty() {
		return "-1"
	}

	return (*s)[len(*s)-1]

}

// Check if stack is empty
func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

// When popping, remove from the end of the stack
func (s *Stack) Pop(str string) {
	// Remove last element from the stack
	index := len(*s) - 1
	*s = (*s)[:index]
}

func IsValid(sentence string) bool {
	var stack Stack
	for _, i := range sentence {
		fmt.Println(stack.Peek())
		if string(i) == "(" || string(i) == "{" || string(i) == "[" {
			stack.Push(string(i))
		}
		if string(i) == ")" || string(i) == "}" || string(i) == "]" {
			if stack.Peek() == string(i) {
				stack.Pop(string(i))
			}
		}
	}

	if stack.isEmpty() {
		return true
	} else {
		return false
	}
}
