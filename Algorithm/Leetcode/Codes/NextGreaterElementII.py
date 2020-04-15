"""

503. Next Greater Element II : https://leetcode.com/problems/next-greater-element-ii/

숫자로 이루어진 array가 주어졌을 때, 각 숫자 다음으로 큰 숫자를 찾는 문제
- 주어진 array는 circular하다 (마지막 element의 다음 element는 첫 번째 element이다)
- NGE가 존재하지 않을 경우, -1

Example:
- Input : [1,2,1]
- Output : [2,-1,2]
- 마지막 1의 경우 array가 circular하므로 NGE는 2가 된다

Note:
stack을 사용하여 해결
circular array이기 때문에 전체 리스트를 한 번만 순회해서는 구할 수 없어서 2번을 순회

"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1 for _ in nums]
        for _ in range(2):
            for i in range(len(nums)-1, -1, -1):
                while stack and stack[-1] <= nums[i]:
                    stack.pop(-1)
                if stack:
                    res[i] = stack[-1]
                stack.append(nums[i])
        return res