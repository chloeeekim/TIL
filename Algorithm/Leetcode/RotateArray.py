"""

189. Rotate Array : https://leetcode.com/problems/rotate-array/

배열(리스트)이 하나 주어졌을 때, 이 배열을 오른쪽으로 k번 회전한 결과를 구하는 문제
- k는 음수가 아니다

Example:
- Input : [1,2,3,4,5,6,7], k = 3
- Output : [5,6,7,1,2,3,4]

- Input : [-1,-100,3,99], k = 2
- Output : [3,99,-1,-100]

Note:
리스트를 두 부분으로 나누어 합치는 방법 사용

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k > length :
            k %= length
        nums[:] = nums[length - k : length] + nums[:length - k]