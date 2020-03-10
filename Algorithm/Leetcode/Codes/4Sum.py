"""

18. 4Sum : https://leetcode.com/problems/4sum/

주어진 정수 배열에서 네 개의 합이 target이 되는 모든 unique quadruplet을 찾는 문제
- 동일한 quadruplet이 포함되어서는 안 된다 (중복 X)
- 네 값의 합이 target이 되는 quadruplet이 존재하지 않을 경우, 빈 리스트([])를 리턴

Example:
- Input : [1, 0, -1, 0, -2, 2], target = 0
- Output : [[-1,  0, 0, 1],[-2, -1, 1, 2],[-2,  0, 0, 2]]

- Input : [1,-2,-5,-4,-3,3,3,5], target = -11
- Output : [[-5,-4,-3,1]]

Note:
3Sum 변형
set을 사용하여 중복되는 값 처리
3Sum과는 달리 target이 음수가 될 수 있으므로 첫번째나 두 번째 값들이 target보다 큰 값이라고 하더라도 배제할 수 없음
참고) 더 효율적인 방법?

"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4 :
            return []
        nums.sort()
        res = set()
        l = len(nums)
        for i in range(l - 3) :
            for j in range(i + 1, l - 2) :
                m, n, tmptarget = j + 1, l - 1, target - nums[i] - nums[j]
                while m < n :
                    tmp = nums[m] + nums[n]
                    if tmp < tmptarget :
                        m += 1
                    elif tmp > tmptarget :
                        n -= 1
                    else :
                        res.add((nums[i], nums[j], nums[m], nums[n]))
                        m += 1
                        n -= 1
        return list(res)