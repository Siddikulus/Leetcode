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

        #Correct but time complexity can be reduced by taking count of all remaining substrings once we hit abc

        # i = 0
        # j = 0
        # count = 0
        # temp = ''
        # while i<len(s):
        #     if j<len(s):
        #         temp += s[j]
        #         if 'a' in temp and 'b' in temp and 'c' in temp:
        #             count += 1
        #         j+=1
        #     else:
        #         i+=1
        #         temp = ''
        #         j=i
        #     # print(i,j,temp, count)
        # return count

        i = 0
        j = 0
        count = 0
        countDict = {'a':0, 'b':0, 'c':0}
        while i<len(s) and j<len(s):
            countDict[s[j]] = 1 + countDict.get(s[j], 0)
            while (countDict['a'] and countDict['b'] and countDict['c']):
                count += len(s)-j
                countDict[s[i]] -= 1
                i+=1
            j+=1
        return count

print(Solution().numberOfSubstrings('aaacb'))

