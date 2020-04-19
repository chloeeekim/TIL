"""

540. Single Element in a Sorted Array : https://leetcode.com/problems/single-element-in-a-sorted-array/

숫자로 이루어진 리스트가 주어졌을 때, 해당 리스트 안에 한 번만 등장하는 원소를 찾는 문제
- 하나의 원소를 제외하고는 모두 두 번씩 등장한다

Example:
- Input : [1,1,2,3,3,4,4,8,8]
- Output : 2

- Input : [3,3,7,7,10,11,11]
- Output : 10

Note:
set : 원소의 유일성을 보장하는 자료형
원소가 모두 두 번씩 등장한다고 가정했을 때의 총합은 2*sum(set(nums))이고,
이 중에서 하나의 원소만 한 번 등장하므로 간단하게 구할 수 있다
참고) O(log n) time과 O(1) space로 해결해 볼 것

"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2 - sum(nums)