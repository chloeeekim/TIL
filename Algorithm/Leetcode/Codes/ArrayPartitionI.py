"""

561. Array Partition I : https://leetcode.com/problems/array-partition-i/

2n개의 정수로 이루어진 리스트가 주어졌을 때, 두 개씩 나눈 각 쌍의 min 값의 최대합을 구하는 문제
- n은 [1, 10000] 범위의 양의 정수이다
- 리스트에 포함된 모든 정수는 [-10000, 10000] 범위이다

Example:
- Input : [1,4,3,2]
- Output : 4
- min(1, 2) + min(3, 4) = 4

Note:
각 쌍의 min 값이 고르게 분포하는 것이 최대합을 얻을 수 있음
정렬하여 순서대로 2개씩 잘라 쌍을 만드는 방식

"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums, res = sorted(nums), 0
        for i in range(0, len(nums), 2) :
            res += nums[i]
        return res