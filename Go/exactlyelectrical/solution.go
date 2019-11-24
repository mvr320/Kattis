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
	var start []int
	var end []int
	var battery int
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		start = numbers(scanner.Text())
	}
	if scanner.Scan() {
		end = numbers(scanner.Text())
	}
	if scanner.Scan() {
		battery = numbers(scanner.Text())[0]
	}
	manhattan := int(math.Abs(float64(start[0]-end[0])) + math.Abs(float64(start[1]-end[1])))
	if manhattan > battery {
		fmt.Println("N")
	} else {
		if (battery-manhattan)%2 == 1 {
			fmt.Println("N")
		} else {
			fmt.Println("Y")
		}
	}
}
