package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		if strings.Contains(strings.ToLower(scanner.Text()), "problem") {
			fmt.Println("yes")
		} else {
			fmt.Println("no")
		}
	}
}
