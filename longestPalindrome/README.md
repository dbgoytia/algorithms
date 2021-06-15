# algorithms

Longest Palindrome implements a set of test cases using Go,
including how to use strings in Go and a general overview of
how runes and bytes work in the Go Programming Language.

I implemented two solutions, one using a brute force algorithm
to find the longest possible Palindrome.

## Brute Force

The brute force approach will consist of creating all possible substrings out of a given string, and finding if each of this substrings is in fact a palindrome.

	Pseudo-code:
		
	longestPalindrome = ""
	substringsMap := allSubstrings(input)
	for every substring in substringsMap:
		if substring isPalindrome():
			if len(substring) > len(longestPalindrome):
				longestPalindrome = substring
				
	return longestPalindrome
	
	Performance
	
		○ We need to convert every byte to rune 
		○ There is an inner loop that gets all possible substrings usign slice syntax.
		○ We need to loop in each of the results of substrings
		○ We need to reverse the string to test for palindrome
		○ 3 nested loops aprox

Time complexity: O(n^3) performance approximately

## Manachar algorithm

A second solution implements Manachar's algorithm, a solution found by a mathematitian that solves the problem in a linear time.


## References

* https://en.wikipedia.org/wiki/Longest_palindromic_substring