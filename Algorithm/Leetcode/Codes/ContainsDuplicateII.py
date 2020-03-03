"""

219. Contains Duplicate II : https://leetcode.com/problems/contains-duplicate-ii/

숫자들이 포함된 리스트와 숫자 k가 주어졌을 때,
해당 리스트에 최대 k만큼의 거리가 차이나는 중복된 값이 있는지를 구하는 문제

Example:
- Input : [1,2,3,1], k = 3
- Output : true

- Input : [1,0,1,1], k = 1
- Output : true

- Input : [1,2,3,1,2,3], k = 2
- Output : false

Note:
dict를 이용하여 특정 숫자가 나타난 최신의 인덱스를 관리
인덱스의 차이가 k보다 작거나 같다면 중복이 존재

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)) :
            if nums[i] in seen :
                before = seen[nums[i]]
                if i - before <= k :
                    return True
            seen[nums[i]] = i
        return False