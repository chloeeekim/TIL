"""

81. Search in Rotated Sorted Array II : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

정렬된 리스트와 정수 하나가 주어졌을 때, target이 포함되어 있는지 확인하는 문제
- 리스트는 증가하는 방향으로 정렬되어 있지만 rotate 되어 있다
- ex) [0,1,2,4,5,6,7]은 [4,5,6,7,0,1,2]가 될 수 있다
- 리스트 내에 중복이 존재할 수 있다

Example:
- Input : nums = [2,5,6,0,0,1,2], target = 0
- Output : true

- Input : nums = [2,5,6,0,0,1,2], target = 3
- Output : false

Note:
target과 동일한 값이 있는 경우 true
리스트가 정렬되어 있기 때문에 이전 값이 target보다 작은데 다음 값이 target보다 큰 경우 target은 존재하지 않는다

"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        issmall = False
        for num in nums :
            if num == target :
                return True
            elif num < target :
                issmall = True
            else :
                if issmall :
                    return False
        return False