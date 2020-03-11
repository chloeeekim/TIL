"""

33. Search in Rotated Sorted Array : https://leetcode.com/problems/search-in-rotated-sorted-array/

정렬된 리스트와 정수 하나가 주어졌을 때, 주어진 정수(target)의 인덱스를 찾는 문제
- 리스트는 증가하는 방향으로 정렬되어 있지만 rotate 되어 있다
- ex) [0,1,2,4,5,6,7]은 [4,5,6,7,0,1,2]가 될 수 있다
- 리스트 내에 정수가 존재하지 않는 경우 -1을 리턴

Example:
- Input : nums = [4,5,6,7,0,1,2], target = 0
- Output : 4

- Input : nums = [4,5,6,7,0,1,2], target = 3
- Output : -1

Note:
- Solution 1
python 내장함수 사용
참고)nums[0] 값을 target과 비교하여 앞에서부터, 혹은 뒤에서부터 탐색할 지 결정하는 방법 가능
- Solution 2
Search in Rotated Sorted Array II와 동일한 방법
target과 동일한 값이 있는 경우 해당 인덱스를 리턴
리스트가 정렬되어 있기 때문에 이전 값이 target보다 작은데 다음 값이 target보다 큰 경우 target은 존재하지 않는다

"""

# Solution 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums.count(target) == 0 :
            return -1
        return nums.index(target)

# Solution 2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        issmall = False
        for i in range(len(nums)) :
            if nums[i] == target :
                return i
            elif nums[i] < target :
                issmall = True
            elif nums[i] > target and issmall :
                return -1
        return -1