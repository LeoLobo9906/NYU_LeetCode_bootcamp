#Decode String
"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution(object):
    def decodeString(self, s):
        def decode(i):
            result = ''
            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    result += s[i]
                    i += 1
                else:
                    num = 0
                    while s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    i += 1  
                    sub, i = decode(i)
                    i += 1  
                    result += sub * num
            return result, i

        return decode(0)[0]