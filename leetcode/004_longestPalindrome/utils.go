package main

func LongestPalindrome(s string) string {
	res := allSubstrings(s)
	longestPalindrome := ""
	for _, substring := range res {
		if isPalindrome(substring) {
			if len(substring) > len(longestPalindrome) {
				longestPalindrome = substring
			}
		}
	}
	return longestPalindrome
}

// Gets all possible substrings of a string
// uses maps since they are concurrent safe
func allSubstrings(myString string) map[int]string {

	res := make(map[int]string)

	if len(myString) == 1 {
		res[0] = myString
		return res
	}

	// Convert all characters to runes for safe substrings
	runes := []rune(myString)
	// Make a map of all possible substrings of a string
	counter := 0
	for i := 1; i < len(runes)+1; i++ {
		for offset := 0; offset <= len(runes)-i; offset++ {
			// safeString := string(runes[offset : i+offset])
			res[counter] = string(runes[offset : offset+i])
			counter += 1
		}
	}
	return res
}

func isPalindrome(input string) bool {
	if len(input) == 1 {
		return true
	}
	// Convert input to runes for string safety
	runes := []rune(input)
	// Reverse the string
	var reversed string
	for j := len(runes) - 1; j >= 0; j-- {
		reversed += string(runes[j])
	}
	if reversed == input {
		return true
	}
	return false
}
