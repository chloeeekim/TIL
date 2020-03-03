"""

137. Single Number II : https://leetcode.com/problems/single-number-ii/

비어 있지 않은, 숫자로 이루어진 리스트가 주어졌을 때
해당 리스트 안에 한 번만 등장하는 원소를 찾는 문제
- 단 하나의 원소를 제외하고는 모두 세 번씩 등장한다

Example:
- Input : [2,2,3,2]
- Output : 3

- Input : [0,1,0,1,0,1,99]
- Output : 99

Note:
set : 원소의 유일성을 보장하는 자료형
원소가 모두 세 번씩 등장한다고 가정했을 때의 총합은 3 * sum(set(nums))
이 중에서 하나의 원소만 한 번 등장하므로, 뺀 값을 2로 나누어 구할 수 있다

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3 * sum(set(nums)) - sum(nums)) / 2)