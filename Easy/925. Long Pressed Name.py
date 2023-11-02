'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.


Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = name+'0'
        typed = typed+'0'

        count_list_name,namecount = [], 1
        for i in range(len(name)-1):
            if name[i] != name[i+1]:
                count_list_name.append((name[i], namecount))
                namecount = 1
            else:
                namecount+=1
        # print(count_list_name, name)

        count_list_typed,typedcount = [], 1
        for i in range(len(typed)-1):
            if typed[i] != typed[i+1]:
                count_list_typed.append((typed[i], typedcount))
                typedcount = 1
            else:
                typedcount+=1

        # print(count_list_name,count_list_typed)

        if len(count_list_name) != len(count_list_typed):
            return False

        for i in range(len(count_list_typed)):
            # print(count_list_typed[i][0], count_list_name[i][0])
            if count_list_typed[i][0] != count_list_name[i][0]:
                return False
            # print(count_list_typed[i][1], count_list_name[i][1])
            if count_list_typed[i][1] < count_list_name[i][1]:
                return False
        return True

print(Solution().isLongPressedName('a',
                                   'b'))