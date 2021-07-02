package atoi

func MyAtoi(s string) int32 {

	var res int32 = 0

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
		return int32(0)
	}

	for i := start; i < len(runes); i++ {
		if runes[i] == 32 {
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
