'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_freq = dict(Counter(s1))

        freq = {}
        left = 0
        k = len(s1)
        for right in range(len(s2)):
            freq[s2[right]] = 1 + freq.get(s2[right], 0)

            if right-left+1 > k:
                if freq[s2[left]] == 1:
                    del freq[s2[left]]
                else:
                    freq[s2[left]] -= 1
                left+=1

            # print(s1_freq, freq)
            if freq == s1_freq:
                return True

        return  False


print(Solution().checkInclusion('ab', 'eidboaoo'))