package atoi

func MyAtoi(s string) int32 {

	var res int32 = 0

	// First convert all characters to runes
	runes := []rune(s)

	for i := 0; i < len(runes); i++ {
		//fmt.Println(runes[i])
		res = res*10 + int32(runes[i]-'0')

	}

	// if err != nil {
	// 	log.Fatal(err)
	// }
	return res
}
