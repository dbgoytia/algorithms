package atoi

import (
	"fmt"
)

func MyAtoi(s string) int {

	// First convert all characters to runes
	runes := []rune(s)

	for i := 0; i < len(runes); i++ {
		fmt.Println(runes[i])
		// fmt.Println(utf8.DecodeRune(runes[i]))
		ascii := runes[i]

		char := string(ascii)

		fmt.Println(char)
	}

	fmt.Println("")
	// if err != nil {
	// 	log.Fatal(err)
	// }
	return 0
}
