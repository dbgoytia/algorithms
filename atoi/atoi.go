package atoi

import (
	"fmt"
	"math"
)

func MyAtoi(s string) int32 {

	var res int32 = 0
	var res64 int64 = 0

	// First convert all characters to runes
	runes := []rune(s)

	// Record starting point of the conversion
	var start int = 0

	// Ignore all leading whitespaces until first non-whitespace
	for runes[start] == 32 {
		if start > len(runes) {
			return int32(0)
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
		return int32(0)
	}

	for i := start; i < len(runes); i++ {
		if runes[i] == 32 {
			break
		}
		if runes[i] > 48 || runes[i] < 57 {

			// Cast to int64 and clamp to min or max int32 to prevent overflow
			res64 = res64*10 + int64(runes[i]-'0')
			if res64 > math.MaxInt32 {
				res = math.MaxInt32
				break
			}
			if res64 < math.MinInt32 {
				res = math.MinInt32
				fmt.Println(res)
				break
			}

			res = res*10 + int32(runes[i]-'0')

		}
	}

	// Add signature before returning
	if signature == '-' {
		res *= -1
	}

	return res

}
