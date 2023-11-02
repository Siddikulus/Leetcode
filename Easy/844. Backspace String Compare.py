'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = s[0]
        t_final = t[0]

        for i in range(1, len(s)):
            if s[i] != '#':
                s_final += s[i]
            else:
                s_final = s_final[:-1]

        for j in range(1, len(t)):
            if t[j] != '#':
                t_final += t[j]
            else:
                t_final = t_final[:-1]

        return s_final == t_final

print(Solution().backspaceCompare('a#c', 'b##'))