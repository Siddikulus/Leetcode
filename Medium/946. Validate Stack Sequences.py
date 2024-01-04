'''
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
'''


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        pop_ptr = 0
        stack = []
        for push_ptr in range(len(pushed)):
            stack.append(pushed[push_ptr])
            while len(stack)>0 and stack[-1] == popped[pop_ptr]:
                pop_ptr+=1
                stack.pop()
        return len(stack) == 0


print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))

