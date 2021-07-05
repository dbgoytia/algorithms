package palindromeNumber

import (
	"math"
)

func isPalindrome(x int) bool {

	var r int = 0
	var count int = 0
	tmp := x

	// Get the multiplier for the number of digits
	for tmp > 0 {
		count++
		tmp = tmp / 10
	}
	count--
	multiplier := int(math.Pow(10.0, float64(count)))

	// Reverse the number
	tmp = x
	for tmp > 0 {
		r += (tmp % 10) * multiplier
		multiplier /= 10
		tmp = tmp / 10
	}

	if r == x {
		return true
	} else {
		return false
	}

}
