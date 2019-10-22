"""

217. Contains Duplicate : https://leetcode.com/problems/contains-duplicate/

숫자들이 포함된 리스트가 주어졌을 때, 해당 리스트에 중복된 값이 있는지를 구하는 문제
- 동일한 값이 두 번 이상 반복되는 것이 존재할 경우 true를 리턴
- 모든 값이 한 번씩만 등장하는 경우 false를 리턴

Example:
- Input : [1,2,3,1]
- Output : true

- Input : [1,2,3,4]
- Output : false

- Input : [1,1,1,3,3,4,3,2,4,2]
- Output : true

Note:
중복을 허용하지 않는 set을 생성 후, set과 기존의 list의 길이를 비교
만약 set과 길이가 다르다면(set이 더 짧다면) 중복이 존재

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        if len(nums) != len(setnums) :
            return True
        else :
            return False