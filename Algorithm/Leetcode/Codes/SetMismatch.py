"""

645. Set Mismatch : https://leetcode.com/problems/set-mismatch/

1부터 n까지의 정수로 구성되어야 하는 list에 하나의 숫자가 사라지고, 하나의 숫자가 중복되어 있을 때 없어진 숫자와 중복된 숫자를 찾는 문제
- list의 길이는 2 이상 10,000 이하이다
- 숫자들은 정렬되어 있지 않다
- 결과는 [중복된 숫자, 사라진 숫자]의 형태로 리턴

Example:
- Input : nums = [1,2,2,4]
- Output : [2,3]

Note:
해당 리스트에서 중복을 제거한 합을 사용하여 간단하게 구할 수 있다
중복을 제거한 합을 구하기 위해서 set을 사용

"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total, setnum = sum([i for i in range(1, len(nums)+1)]), sum(set(nums))
        return [sum(nums)-setnum, total-setnum]