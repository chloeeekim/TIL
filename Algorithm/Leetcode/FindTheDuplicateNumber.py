"""

287. Find the Duplicate Number : https://leetcode.com/problems/find-the-duplicate-number/

숫자들로 이루어진 리스트 nums가 주어졌을 때, 중복되는 숫자를 찾는 문제
- nums에는 1부터 n까지의 숫자 n+1개가 포함된다
- 중복되는 숫자는 반드시 하나가 존재한다
- 중복되는 숫자는 두 번 이상 등장할 수 있다

Example:
- Input : [1,3,4,2,2]
- Output : 2

- Input : [3,1,3,4,2]
- Output : 3

Note:
dict를 써서 이전에 나온 값인지 확인하는 방법

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for num in nums :
            if num in seen :
                return num
            else :
                seen[num] = 1