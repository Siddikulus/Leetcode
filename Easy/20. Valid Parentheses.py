'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in '{[(':
                stack.append(s[i])

            elif len(stack)>0 and s[i] in '}])':
                if s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
            # print(s[i], stack)
        return len(stack) == 0
print(Solution().isValid('()'))
