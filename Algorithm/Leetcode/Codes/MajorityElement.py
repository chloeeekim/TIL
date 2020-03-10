"""

169. Majority Element : https://leetcode.com/problems/majority-element/

숫자들로 이루어진 리스트가 주어졌을 때, 해당 리스트에서 가장 많이 등장하는 숫자를 찾는 문제
- majority element는 리스트의 사이즈가 n일 때, n/2번보다 많이 등장한다
- 리스트는 비어있지 않고, majority element는 항상 존재한다

Example:
- Input : [3,2,3]
- Output : 3

- Input : [2,2,1,1,1,2,2]
- Output : 2

Note:
- Solution 1
dict를 사용하여 특정 숫자가 몇 번 나타났는지를 관리
- Solution 2
중복을 허용하지 않는 set을 이용
Solution 1과 실제 속도 면에서 큰 차이가 없음

"""

# Solution 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lower = len(nums) / 2
        count = dict()
        for num in nums :
            if num in count :
                count[num] += 1
            else :
                count[num] = 1
            if count[num] > lower :
                return num

# Solution 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lower = len(nums) / 2
        snums = set(nums)
        for num in snums :
            if nums.count(num) > lower :
                return num