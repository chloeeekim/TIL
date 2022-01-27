"""

976. Largest Perimeter Triangle : https://leetcode.com/problems/largest-perimeter-triangle/

정수로 이루어진 리스트 nums가 주어졌을 때, 만들어지는 삼각형의 최대 둘레를 구하는 문제
- 삼각형이 만들어지지 않는 경우 0을 리턴한다
- nums의 길이는 3 이상 10^4 이하이다

Example:
- Input : nums = [2,1,2]
- Output : 5

- Input : nums = [1,2,1]
- Output : 0

Note:
정렬하여 가장 큰 값부터 확인하는 방식

"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if nums[i]+nums[i+1] > nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0