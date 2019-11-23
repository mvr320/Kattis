package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func numbers(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, err := strconv.Atoi(f)
		if err == nil {
			n = append(n, i)
		}
	}
	return n
}

func main() {
	var ranger float64
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		ranger = float64(numbers(scanner.Text())[0])
	}
	fmt.Println(math.Pow(ranger, 2.0) * math.Pi)
	fmt.Println(math.Pow(ranger*2.0, 2.0) / 2.0)
}
