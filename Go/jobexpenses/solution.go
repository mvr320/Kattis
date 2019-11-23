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
	//var numcases int
	var expenses []int
	scanner := bufio.NewScanner(os.Stdin)
	expenses = numbers(scanner.Text())
	var summer int
	for i := 1; i <= 2 && scanner.Scan(); i++ {
		switch i {
		case 1:
			_ = numbers(scanner.Text())[0]
		case 2:
			expenses = numbers(scanner.Text())
		}
	}
	for _, item := range expenses {
		if item < 0 {
			summer += item
		}
	}
	fmt.Println(summer * -1)
}
