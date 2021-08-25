package reverseInteger

import (
	"log"
	"strconv"
)

func Reverse(x int) int {

	// Check integer overflows, preflight
	if x > 2147483647 || x < -2147483648 {
		return 0
	}

	// First step is to parse the integer to a string
	numberString := strconv.Itoa(x)

	// Convert all characters to runes to reverse safely
	runes := []rune(numberString)

	// Check if first rune is a - symbol (for dealing with negatives)
	var isNegative bool = false
	if runes[0] == '-' {
		isNegative = true
	}

	// Reverses the string
	var reversed string
	for i := len(runes) - 1; i >= 0; i-- {
		if isNegative {
			if runes[i] != '-' {
				reversed += string(runes[i])
			}
		} else {
			reversed += string(runes[i])
		}
	}

	// Add minus if number was a negative
	if isNegative {
		reversed = string('-') + reversed
	}

	// Convert string to integer
	reversedInt, err := strconv.Atoi(reversed)

	if err != nil {
		log.Fatal(err)
	}

	// Check for integer overflows, postflight
	if reversedInt > 2147483647 || reversedInt < -2147483648 {
		return 0
	}

	return reversedInt
}
