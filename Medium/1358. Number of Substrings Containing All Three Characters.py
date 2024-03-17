'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        total = 0
        count = {'a':0, 'b':0, 'c':0}
        while right < len(s):
            count[s[right]] = 1 + count[s[right]]
            while count['a'] and count['b'] and count['c']:
                total += len(s) - right
                count[s[left]] = count[s[left]] - 1
                left+=1
            right+=1
        return total


print(Solution().numberOfSubstrings(s = "abcabc"))

