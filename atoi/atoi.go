package atoi

import (
	"math"
)

func MyAtoi(s string) int {

	// If length of string is zero, return zero
	if len(s) == 0 {
		return 0
	}

	var res = 0
	var res64 int64 = 0

	// First convert all characters to runes
	runes := []rune(s)

	// Record starting point of the conversion
	var start int = 0

	// Ignore all leading whitespaces until first non-whitespace
	for runes[start] == 32 {
		if start > len(runes) {
			return 0
		}
		start++
	}

	// Check if there's a signature at the beginning of the number and set it
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

	// Check if first non-whitespace is a non-digit character
	if runes[start] < 48 || runes[start] > 58 {
		return 0
	}

	for i := start; i < len(runes); i++ {

		// Stop when finding intermediate white-spaces
		if runes[i] == 32 {
			break
		}
		// Ignore all characters after a dot
		if runes[i] == 46 {
			break
		}

		// Ignore all non-digit characters
		if runes[i] > 48 || runes[i] < 57 {
			// Cast to int64 and clamp to min or max int32 to prevent overflow
			res64 = res64*10 + int64(runes[i]-'0')
			if res64 > math.MaxInt32 || res64 < math.MinInt32 {
				if signature == '-' {
					return math.MinInt32 // If negative return minimal Int32
				}
				return math.MaxInt32 // If positive return max Int32
			}
			res = res*10 + int(runes[i]-'0')
		}
	}

	// Add signature before returning
	if signature == '-' {
		res *= -1
	}

	return res

}
