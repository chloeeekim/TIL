"""

442. Find All Duplicates in an Array : https://leetcode.com/problems/find-all-duplicates-in-an-array/

숫자로 이루어진 리스트가 주어졌을 때, 중복된 숫자를 찾는 문제
- 중복된 숫자들은 2번씩 등장하고, 나머지 숫자는 1번씩만 등장한다

Example:
- Input : [4,3,2,7,8,2,3,1]
- Output : [2,3]

Note:
dict를 사용하여 이전에 나타난 값을 확인
만약 dict에 존재하는 경우 2번째로 나타난 경우이므로 결과 리스트에 append

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []
        for num in nums :
            if num in seen :
                res.append(num)
            else :
                seen[num] = 1
        return res