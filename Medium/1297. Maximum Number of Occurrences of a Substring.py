'''
Given a string s, return the maximum number of occurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.


Constraints:

1 <= s.length <= 105
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s consists of only lowercase English letters.
'''


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        freq = {}

        for right in range(len(s)):
            while right-left+1 >=minSize and right-left+1 <= maxSize:
                if len(set(s[left:right+1])) <= maxLetters:
                    freq[s[left:right+1]] = 1+freq.get(s[left:right+1], 0)
                print(s[left:right+1], freq)
                left+=1

        return max(freq.values())
print(Solution().maxFreq('aaaa', 1,3,3))

