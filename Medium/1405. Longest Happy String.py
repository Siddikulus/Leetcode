'''
1405. Longest Happy String
Medium
Topics
Companies
Hint
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.


Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []

        if a > 0:
            pq.append((-a, 'a'))
        if b > 0:
            pq.append((-b, 'b'))
        if c > 0:
            pq.append((-c, 'c'))

        heapq.heapify(pq)
        s = ''

        while pq:
            first_count, first_char = heapq.heappop(pq)
            if len(s) > 1 and (first_char == s[-1] and first_char == s[-2]):
                if not pq: break
                second_count, second_char = heapq.heappop(pq)
                s += second_char
                if second_count + 1 != 0:
                    heapq.heappush(pq, (second_count + 1, second_char))
                heapq.heappush(pq, (first_count, first_char))

            else:
                s += first_char
                if first_count + 1 != 0:
                    heapq.heappush(pq, (first_count + 1, first_char))

        return s

print(Solution().longestDiverseString(a = 1, b = 1, c = 7))

