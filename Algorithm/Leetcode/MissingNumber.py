"""

268. Missing Number : https://leetcode.com/problems/missing-number/

0부터 n까지의 서로 다른 숫자가 포함되어야 하는 리스트가 주어졌을 때,
해당 리스트에서 빠져 있는 숫자를 찾는 문제

Example:
- Input : [3,0,1]
- Output : 2

- Input : [9,6,4,2,3,5,7,0,1]
- Output : 8

Note:
- Solution 1
리스트를 정렬한 다음, 0부터 시작하는 리스트이므로 인덱스와 다른 값이 나오면 해당 값이 missing number
다 확인했음에도 missing number가 없다면 다음 값이 missing number가 된다
- Solution 2
길이가 n인 리스트의 예상되는 합에서 실제 합을 빼면 missing number의 값이 된다

"""

# Solution 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)) :
            if nums[i] != i :
                return i
        return i + 1

# Solution 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        exsum = length * (length + 1) // 2
        realsum = sum(nums)
        return exsum - realsum