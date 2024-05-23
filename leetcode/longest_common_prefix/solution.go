// https://leetcode.com/problems/longest-common-prefix/
package main

import (
	"fmt"
)

func longestCommonPrefix(strs []string) string {
	var common_prefix string = ""

	out:
	for char_index := 0; char_index < len(strs[0]); char_index++ {
		for string_index := 1; string_index < len(strs); string_index++ {
			if char_index == len(strs[string_index]) {
				break out 
			}

			if strs[string_index] != strs[string_index - 1] {
				break out
			}
		}
		fmt.Println(strs[0][char_index])
		//common_prefix[char_index] = string(strs[0][char_index])
	}

	return common_prefix
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower","flow","flight"}))
	fmt.Println(longestCommonPrefix([]string{"dog","racecar","car"}))
}

