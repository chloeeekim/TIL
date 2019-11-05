"""

448. Find All Numbers Disappeared in an Array : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

숫자로 이루어진 리스트가 주어졌을 때, 해당 리스트에서 제외된 숫자를 모두 찾는 문제
- 1부터 주어진 리스트의 길이(n)까지의 숫자가 포함된다
- 중복된 숫자들은 2번씩 등장하고, 나머지 숫자는 1번씩만 등장한다
- [1,n]까지의 숫자 중 리스트에 포함되지 않은 숫자를 모두 찾아 리스트의 형태로 리턴

Example:
- Input : [4,3,2,7,8,2,3,1]
- Output : [5,6]

Note:
중복을 허용하지 않는 set으로 변경
1부터 n까지 숫자를 확인하면서 set 안에 존재하지 않는 경우 결과 리스트에 append

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []
        for num in range(1, len(nums) + 1) :
            if num not in s :
                res.append(num)
        return res