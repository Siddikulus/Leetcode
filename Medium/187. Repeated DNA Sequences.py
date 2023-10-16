'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        split_list = []
        for i in range(len(s)):
            if len(s[i:i+10]) == 10:
                split_list.append(s[i:i+10])
        count_dict = {}
        for element in split_list:
            count_dict[element] = 1 + count_dict.get(element,0)
        return [k for k,v in count_dict.items() if v >= 2]

print(Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))