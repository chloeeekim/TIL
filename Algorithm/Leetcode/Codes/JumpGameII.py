"""

45. Jump Game II : https://leetcode.com/problems/jump-game-ii/

음수가 아닌 정수로 이루어진 리스트 nums가 주어졌을 때, 마지막 위치까지 도달할 수 있는 가장 적은 점프 수를 구하는 문제
- 각 원소는 해당 위치에서 뛸 수 있는 가장 긴 거리를 의미한다
- 항상 마지막 위치까지 도달할 수 있다는 것이 보장된다

Example:
- Input : nums = [2,3,1,1,4]
- Output : 2
- 1칸을 뛰어서 3이 있는 위치로 이동한 다음 3칸을 뛰어서 마지막 인덱스로 이동

- Input : nums = [2,3,0,1,4]
- Output : 2

Note:
dp를 이용하여 해결
참고) 더 효율적인 방법?

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize] * (len(nums))
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(nums[i]+1):
                if i+j >= len(nums):
                    break
                dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1]