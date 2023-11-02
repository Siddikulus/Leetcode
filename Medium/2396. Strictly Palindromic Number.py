'''
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.



Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
Example 2:

Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.



Constraints:

4 <= n <= 105
'''


class Solution:
    def get_string_by_base(self,decimal_number, base):
        s = ''
        while decimal_number > 1:
            decimal_number, rem = decimal_number // base, decimal_number % base
            s += str(rem)
        s += str(decimal_number)
        return s[::-1]


    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n+1):
            # print(i, self.get_string_by_base(n, i))
            if (self.get_string_by_base(n, i)) != (self.get_string_by_base(n, i))[::-1]:
                return False
        return True

print(Solution().isStrictlyPalindromic(15))




