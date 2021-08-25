package main

import (
	"strings"
)

func LongestPalindromeManachars(s string) string {

	process := preProcess(s)

	p := make([]int, len(process))

	id, mx := 0, 0

	maxLen, maxLenCenter := 0, 0

	for i := range p {

		// If i expands longer than mx, set p[i] (to keep it O(N) bound)
		if i < mx {
			p[i] = min(p[2*id-i], mx-i)
		} else {
			p[i] = 1
		}

		// Finds how long the Palindrome could expand
		for i-p[i] >= 0 && i+p[i] < len(process) && process[i-p[i]] == process[i+p[i]] {
			p[i]++
		}
		if p[i]+i-1 > mx {
			mx = p[i] - 1
			id = i
		}

		// Find longest possible expansion for the palindrome
		// if it expands more than the possible of this possition,
		// then set the maximum length of the palindrome as this one.
		if maxLen < p[i]-1 {
			maxLen = p[i] - 1
			maxLenCenter = i
		}

	}
	return nextProcess(process[maxLenCenter-maxLen : maxLenCenter+maxLen])
}

// Inserts a special character in between each rune
// example:  a b b a  => # a # b # b # a #
func preProcess(s string) string {
	var sb strings.Builder
	sb.WriteRune('#')
	for _, c := range s {
		sb.WriteRune(c)
		sb.WriteRune('#')
	}
	return sb.String()
}

// Removes the special character inserted between each rune
// example: # a # b # b # a # => a b b a
func nextProcess(s string) string {
	var sb strings.Builder
	for _, c := range s {
		if c != '#' {
			sb.WriteRune(c)
		}
	}
	return sb.String()
}

// Returns the minimum between two integers
func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
