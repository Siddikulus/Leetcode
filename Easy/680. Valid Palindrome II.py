'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        count = 1
        while i<=j:
            if s[i] != s[j] and count > 0:
                tempi = s[i+1:j+1] #Check if i is char to remove
                tempj = s[i:j] #Check if j is char to remove
                return (tempi == tempi[::-1] or tempj == tempj[::-1])
            i,j = i+1, j-1
        return True


print(Solution().validPalindrome('abbcca'))