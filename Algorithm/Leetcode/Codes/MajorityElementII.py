"""

229. Majority Element II : https://leetcode.com/problems/majority-element-ii/

숫자들로 이루어진 리스트가 주어졌을 때, 해당 리스트에서 n/3보다 많이 등장하는 숫자들을 찾는 문제

Example:
- Input : [3,2,3]
- Output : [3]

- Input : [2,2,1,1,1,2,2]
- Output : [1,2]

Note:
Majority Element의 Solution 2 방법
중복을 허용하지 않는 set을 이용

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        bound = len(nums) / 3
        snums = set(nums)
        res = []
        for num in snums :
            if nums.count(num) > bound :
                res.append(num)
        return res