package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)
	var txtlines []string

	for scanner.Scan() {
		txtlines = append(txtlines, scanner.Text())
	}

	var inc = true
	var dec = true
	var last string
	for index, eachline := range txtlines {
		if index != 0 {
			if index == 1 {
				last = eachline
			} else {
				if inc || dec {
					if last > eachline {
						inc = false
					} else {
						dec = false
					}
					//fmt.Println(inc, dec, last, eachline)
					last = eachline
				}
			}
		}
	}
	if inc {
		fmt.Println("INCREASING")
	} else {
		if dec {
			fmt.Println("DECREASING")
		} else {
			fmt.Println("NEITHER")
		}
	}
}

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
