package atoi

import (
	"fmt"
)

func MyAtoi(s string) int32 {

	var res int32 = 0

	// First convert all characters to runes
	runes := []rune(s)

	// Record starting point of the conversion
	var start int = 0

	for i := start; i < len(runes); i++ {
		// Ignore all leading whitespaces
		if runes[i] == 32 { // 12341 with words -> This is a contradiction to this use case, you have two spaces, so it's going to start in position two instead of only ignoring leading whitespaces
			start++
		}
	}

	// Check if there's a signature at the beginning of the number
	signature := '+'
	var foundSignature bool = false
	if runes[start] == 45 {
		signature = '-'
		foundSignature = true
	} else if runes[start] == 43 {
		foundSignature = true
	}

	if foundSignature {
		start++
	}
	for i := start; i < len(runes); i++ {
		if runes[i] == 32 {
			fmt.Println("found whitespace!")
			break
		}
		if runes[i] > 48 || runes[i] < 57 {
			res = res*10 + int32(runes[i]-'0')
		}
	}

	// Add signature before returning
	if signature == '-' {
		return res * -1
	}
	return res
}
