#438. Find All Anagrams in a String
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s): return []
        pCount,sCount = {}, {}
        for i in range(len(p)):
            pCount [p[i]] = 1 + pCount. get (p[i],0)
            sCount [s[i]] = 1 + sCount. get(s[i],0)
        res = [0] if sCount == pCount else []
        1 = 0
        for r in range(len(p), len(s)):
            sCount [s[r]] = 1 + sCount -get(s[r], 0)
            sCount [s [1]] -= 1
            if sCount [s[1]] == 0: 
                sCount. pop (s [1])
            1 += 1
            if sCount == pCount:
                res. append (1) 
        