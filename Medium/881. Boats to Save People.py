'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)


Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
'''


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        if len(people) <= 1:
            return 1

        i,j = 0,1
        count = 0
        prefix_sum = [people[0]]

        # for k in range(1, len(people)):
        #     prefix_sum.append(prefix_sum[k-1] + people[k])

        print(i, j, prefix_sum, count)
        while i < j and j<len(people):
            prefix_sum.insert(j, people[j] + prefix_sum[i])
            if prefix_sum[i] <= limit and prefix_sum[j] > limit:
                count +=1
                prefix_sum[j] = prefix_sum[j] - people[i]
                i += 1
                j += 1
            elif prefix_sum[i] <= limit and prefix_sum[j] > limit:
                i+=1
                j+=1
            else:
                i+=1
                j+=1
            print(i,j,prefix_sum, count)
        return count

print(Solution().numRescueBoats([3,5,3,4], 5))
