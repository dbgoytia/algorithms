package cubes

import (
	"math"
)

func FindNb(m int) int {
	total := 0
	n := 0
	for total < m {
		n += 1
		total += mathFunc(n)
	}

	if total == m {
		return n
	} else {
		return -1
	}
}

func mathFunc(n int) int {
	return int(math.Pow(float64(n), 3))
}
