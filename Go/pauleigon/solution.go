package main

import (
	"bufio"
	"fmt"
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
	var ranger []int
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		ranger = numbers(scanner.Text())
	}
	if int(float64(ranger[2]+ranger[1])/float64(ranger[0]))%2 == 0 {
		fmt.Println("paul")
	} else {
		fmt.Println("opponent")
	}
}
