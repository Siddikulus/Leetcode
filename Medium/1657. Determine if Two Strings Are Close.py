'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"


Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
'''


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        word1list = sorted(word1)
        word2list = sorted(word2)

        counterword1 = {}
        counterword2 = {}

        for i in range(len(word1list)):
            counterword1[word1list[i]] = 1 + counterword1.get(word1list[i], 0)
            counterword2[word2list[i]] = 1 + counterword2.get(word2list[i], 0)

        print(counterword1, counterword2)
        # print(set(counterword1.keys()), set(counterword2.keys()))
        if (len(set(counterword1.keys()) - set(counterword2.keys())) == 0) and (len(set(counterword2.keys()) - set(counterword1.keys())) == 0):
            val1 = list(counterword1.values())
            val2 = list(counterword2.values())
            for i in range(len(val1)):
                if val1.count(val1[i]) != val2.count(val1[i]):
                    return False
            return True
        return False

print(Solution().closeStrings(word1 = "yyyuxuyuxxxxxxxyyyyyxxyyxxxyyyxyx", word2 = "uxuxuuuuuuxuuyuuuuuuyuuuuuuuyyuuu"))


