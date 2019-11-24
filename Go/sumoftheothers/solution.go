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
	for scanner.Scan() {
		ranger = numbers(scanner.Text())
		sum := 0
		for _, n := range ranger {
			sum += n
		}
		notdone := true
		for _, n := range ranger {
			if notdone {
				if sum-2*n == 0 {
					fmt.Println(n)
					notdone = false
				}
			}
		}
	}
}
