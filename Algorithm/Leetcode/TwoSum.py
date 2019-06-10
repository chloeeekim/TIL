"""

1. Two Sum : https://leetcode.com/problems/two-sum/

주어진 정수 배열에서 두 값의 합이 찾고자 하는 값(target)일 경우,
두 인덱스를 반환하는 문제
- 정확히 하나의 솔루션이 존재
- 동일한 값은 두 번 사용할 수 없다

Example:
- Input : nums = [2, 7, 11, 15], target = 9
- Output : [0, 1]
- nums[0] + nums[1] = 2 + 7 = 9

Note:
dict 사용 (key : 확인한 정수값 / value : 인덱스)

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
    
        for i, num in enumerate(nums) :
            temp = target - num
            if temp in seen :
                return [seen[temp], i]
            else :
                seen[num] = i

        return []