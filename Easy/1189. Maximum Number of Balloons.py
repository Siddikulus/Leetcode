'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCount = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        textBalloonCount = {}
        for char, count in balloonCount.items():
            if char in text:
                print(char, text.count(char), text.count(char)//balloonCount[char])
                textBalloonCount[char] = text.count(char)//balloonCount[char]
            else:
                return 0
        return min(textBalloonCount.values())


s = Solution()
print(s.maxNumberOfBalloons('balon'))