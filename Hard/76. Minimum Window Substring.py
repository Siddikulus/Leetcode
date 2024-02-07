'''
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        ans = ""
        mapT = {}  # frequency of t
        for ch in t:
            mapT[ch] = mapT.get(ch, 0) + 1

        mct = 0  # match count
        dmct = len(t)  # desired match count
        mapS = {}
        i = -1
        j = -1

        while True:
            f1 = False
            f2 = False

            # Acquire the character
            while i < len(s) - 1 and mct < dmct:
                i += 1
                ch = s[i]
                mapS[ch] = mapS.get(ch, 0) + 1

                if mapS.get(ch, 0) <= mapT.get(ch, 0):
                    mct += 1
                f1 = True

            # Collect answers and release
            while j < i and mct == dmct:
                j += 1
                pans = s[j:i + 1]  # pans = potential answer
                if not ans or len(pans) < len(ans):
                    ans = pans

                ch = s[j]
                if mapS[ch] == 1:
                    del mapS[ch]
                else:
                    mapS[ch] -= 1

                if mapS.get(ch, 0) < mapT.get(ch, 0):
                    mct -= 1
                f2 = True

            if not f1 and not f2:
                break
        return ans

#Full referenced