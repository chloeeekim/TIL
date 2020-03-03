"""

704. Binary Search : https://leetcode.com/problems/binary-search/

오름차순으로 정렬된 정수로 이루어진 리스트 nums가 주어졌을 때, target을 찾는 문제
- target이 존재하는 경우 해당 인덱스를 리턴
- target이 존재하지 않는 경우 -1을 리턴
- nums에 포함되는 각 숫자들은 unique하다
- nums의 크기는 [1, 10000] 범위이다
- nums에 포함되는 각 숫자의 크기는 [-9999, 9999] 범위이다

Example:
- Input : nums = [-1,0,3,5,9,12], target = 9
- Output : 4

- Input : nums = [-1,0,3,5,9,12], target = 2
- Output : -1

Note:
target이 존재할 수 있는 범위가 [bottom, top]이 된다
해당 범위의 가운데에 위치하는 값이 target보다 작으면 그 아래 범위를 확인하고, 크면 그 위의 범위를 확인하는 방식

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums) - 1
        while bottom <= top :            
            idx = int((bottom + top) / 2)
            num = nums[idx]
            if num == target :
                return idx
            elif num > target :
                top = idx - 1
            else :
                bottom = idx + 1
        return -1