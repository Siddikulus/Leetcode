'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []
        highLen = len(str(high))
        lowLen = len(str(low))
        ini = ''

        for i in range(1, lowLen+1):
            ini += str(i)
        s = [int(ini)]

        for i in range(lowLen, highLen):
            s.append(int(str(s[-1]) + str(i+1)))

        i = 0
        j = 1
        for i in range(len(s)):
            size = len(str(s[i]))
            val = s[i]
            while str(val)[-1] != '0':
                if val >= low and val < high:
                    ans.append(val)
                val = val + int('1'*size)
        return ans

print(Solution().sequentialDigits(low = 10, high = 11))