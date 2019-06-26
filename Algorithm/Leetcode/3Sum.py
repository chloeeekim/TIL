"""

15. 3Sum : https://leetcode.com/problems/3sum/

주어진 정수 배열에서 세 개의 합이 0이 되는 모든 unique triplet을 찾는 문제
- 동일한 triplet이 포함되어서는 안 된다 (중복 X)
- 세 값의 합이 0이 되는 triplet이 존재하지 않을 경우, 빈 리스트([])를 리턴

Example:
- Input : [-1, 0, 1, 2, -1, -4]
- Output : [[-1, 0, 1], [-1, -1, 2]]

- Input : [0, 0, 0]
- Output : [0, 0, 0]

Note:
TwoSum 변형
set을 사용하여 중복되는 값 처리
시간을 더 줄일 수 있는 방법?

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 :
            return []
        nums.sort()
        res = set()
        l = len(nums)
        for i in range(l) :            
            if nums[i] > 0 :
                break
            target = -nums[i]
            j, k = i + 1, l - 1
            while j < k :
                temp = nums[j] + nums[k]
                if temp < target :
                    j += 1
                elif temp > target : 
                    k -= 1
                else :
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return list(res)