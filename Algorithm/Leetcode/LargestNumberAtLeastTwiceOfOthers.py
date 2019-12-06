"""

747. Largest Number At Least Twice of Others : https://leetcode.com/problems/largest-number-at-least-twice-of-others/

정수로 이루어진 리스트 nums가 주어졌을 때, 가장 큰 값이 다른 값들의 최소 두 배 이상이 되는지 확인하는 문제
- 가장 큰 값은 정확히 하나가 존재한다
- 나머지 값들의 최소 두 배 이상이 되는 가장 큰 값이 존재하는 경우, 해당 값의 인덱스를 리턴
- 해당 조건을 만족하는 값이 없는 경우, -1을 리턴
- nums의 길이는 [1,50] 범위이다
- 모든 nums[i]의 값은 [0, 99] 범위이다

Example:
- Input : [3,6,1,0]
- Output : 1
- 6은 다른 모든 값들의 2배 이상 조건을 만족

- Input : [1,2,3,4]
- Output : -1
- 4는 3의 2배 이상 조건을 만족하지 않으므로 -1을 리턴

Note:
가장 큰 값이 두 번째로 큰 값의 2배 이상인 경우 나머지 값들도 조건을 모두 만족하게 된다

"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxnum = max(nums)
        idx = nums.index(maxnum)
        del nums[idx]
        nmax = max(nums) if nums else -1
        if maxnum >= nmax * 2 :
            return idx
        return -1