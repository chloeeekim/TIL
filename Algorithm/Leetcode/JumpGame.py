"""

55. Jump Game : https://leetcode.com/problems/jump-game/

양의 정수로 이루어진 리스트가 주어졌을 때,
최대 각 칸의 값만큼 점프할 수 있다고 할 때 마지막 인덱스에 도달할 수 있는지 확인하는 문제
- 값이 3이라면 1칸, 2칸, 3칸 다음으로 이동할 수 있다

Example:
- Input : [2,3,1,1,4]
- Output : True
- 인덱스 0에서 1칸 이동 -> 인덱스 1에서 3칸 이동

- Input : [3,2,1,0,4]
- Output : False
- 어떤 경우에도 무조건 인덱스 3에 도달할 수밖에 없고, 인덱스 3의 값은 0

Note:
문제를 잘 읽자.
처음에는 각 칸의 값만큼만 점프할 수 있고, 정확히 마지막 인덱스에 도달할 수 있는지를 확인하는 문제로 이해하고 풀었으나
단순히 최대로 이동할 수 있는 길이가 리스트의 길이보다 긴 지 확인하면 되는 문제였다.

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        far, i = 0, 0
        while i <= far :
            far = max(far, i + nums[i])
            if far >= length - 1 :
                return True
            i += 1
        return False