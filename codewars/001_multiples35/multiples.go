package multiples

func Multiple3And5(number int) int {
	total := 0
	for i := 0; i < number; i++ {
		if (i%3 == 0) || (i%5 == 0) {
			total += i
		}
	}
	return total
}
