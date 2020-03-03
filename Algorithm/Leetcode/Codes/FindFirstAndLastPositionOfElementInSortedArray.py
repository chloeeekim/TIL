"""

34. Find First and Last Position of Element in Sorted Array : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

하나의 정렬된 리스트와 정수가 주어졌을 때,
주어진 정수(target)가 등장하는 처음과 끝의 인덱스를 찾는 문제
- 리스트 내에 target이 없는 경우, [-1, -1]을 리턴

Example:
- Input : nums = [5,7,7,8,8,10], target = 8
- Output : [3,4]

- Input : nums = [5,7,7,8,8,10], target = 6
- Output : [-1,-1]

Note:
index : 리스트 내에서 처음 등장하는 인덱스를 리턴

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c = nums.count(target)
        if c == 0 :
            return [-1, -1]
        i = nums.index(target)
        res = [i, i + c - 1]
        return res