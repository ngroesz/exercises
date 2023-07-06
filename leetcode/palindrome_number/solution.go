/*
https://leetcode.com/problems/palindrome-number/

I wanted to try doing this without converting to string
*/

package main

import (
	"fmt"
	"math"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	var length = numberLength(x)

	for index := 0; index < int(math.Ceil(float64(length)/2)); index++ {
		if place_value(x, index+1) != place_value(x, length-index) {
			return false
		}
	}

	return true
}

func numberLength(number int) int {
	if number == 0 {
		return 1
	} else {
		return int(math.Log10(float64(number)) + 1)
	}
}

func place_value(number int, place int) int {
	return int(number/int(math.Pow(10, float64(place-1)))) % 10
}

func main() {
	fmt.Println(isPalindrome(1024201))
	fmt.Println(isPalindrome(10244201))
	fmt.Println(isPalindrome(10243201))
}
