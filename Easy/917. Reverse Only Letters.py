'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        #Solution 1
        # letters = []
        #
        # for i in range(len(s)):
        #     if s[i].isalpha():
        #         letters.append(s[i])
        #
        # letters.reverse()
        # final = []
        # for i in range(len(s)):
        #     if s[i].isalpha():
        #         final.append(letters[0])
        #         letters.pop(0)
        #     else:
        #         final.append(s[i])
        #
        # return ''.join(final)


        #Solution 2
        left, right = 0, len(s)-1
        s_list = list(s)
        while left < right:
            if not s_list[left].isalpha():
                left+=1
            if not s_list[right].isalpha():
                right-=1

            if s_list[left].isalpha() and s_list[right].isalpha():
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left+=1
                right-=1

            print(left, right, s_list)
        return ''.join(s_list)


print(Solution().reverseOnlyLetters('Test1ng-Leet=code-Q!'))

