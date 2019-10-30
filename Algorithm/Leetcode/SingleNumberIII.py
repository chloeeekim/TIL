"""

260. Single Number III : https://leetcode.com/problems/single-number-iii/

비어 있지 않은, 숫자로 이루어진 리스트가 주어졌을 때
해당 리스트 안에 한 번만 등장하는 원소를 찾는 문제
- 단 두 개의 원소를 제외하고는 모두 두 번씩 등장한다

Example:
- Input : [1,2,1,3,2,5]
- Output : [3,5]

Note:
dict를 사용하여 해당 원소가 몇 번 등장했는지를 관리

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []
        for i in nums :
            if i not in seen :
                seen[i] = 1
            else :
                seen[i] += 1
        for i in seen :
            if seen[i] == 1 :
                res.append(i)
        return res