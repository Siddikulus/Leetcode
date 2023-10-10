'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



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
'''

from collections import Counter
class Solution:
    # def findAnagrams(self, s: str, p: str) -> list[int]:
    #     division = len(p)
    #     p_sorted = sorted(p)
    #     index_list = []
    #     for i in range(len(s)):
    #         if p_sorted == sorted(s[i:i+division]) and len(s[i:i+division]) == division:
    #             index_list.append(i)
    #     return index_list


    def findAnagrams(self, s: str, p: str) -> list[int]:
        counted_dict = dict(Counter(p))
        p_length = len(p)
        index_list = []
        for i in range(len(s)):
            sub_list = s[i:i+p_length]
            subset_dict = dict(Counter(sub_list))
            if counted_dict == subset_dict and len(sub_list) == p_length:
                index_list.append(i)

        return index_list


print(Solution().findAnagrams('cbaebabacd', 'abc'))
