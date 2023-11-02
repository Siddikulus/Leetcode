'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.



Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        final_s = ''
        i = 0
        if len(s) <= 1: return s

        while i < len(s):
            temp = s[i:i+2*k]
            if len(s) - i < k:
                final_s += temp[::-1]
            else:
                second_temp = temp[:k][::-1] + temp[k:]
                final_s += second_temp
            i += 2*k
            # print(final_s, i, temp)
        return final_s

print(Solution().reverseStr('abcdefg', 3))