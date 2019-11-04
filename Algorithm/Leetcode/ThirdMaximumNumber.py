"""

414. Third Maximum Number : https://leetcode.com/problems/third-maximum-number/

비어 있지 않은 정수로 이루어진 리스트가 주어졌을 때, 세 번째로 큰 값을 구하는 문제
- 만약 세 번째로 큰 값이 존재하지 않는 경우, 가장 큰 값을 리턴한다

Example:
- Input : [3,2,1]
- Output : 1

- Input : [1,2]
- Output : 2
- 세 번째로 큰 값이 존재하지 않으므로 가장 큰 값을 리턴

- Input : [2,2,3,1]
- Output : 1
- 2가 두 번 등장하지만 2는 두 번째로 큰 값이므로 1이 세 번째로 큰 값이 된다

Note:
중복을 제거하기 위하여 set으로 바꾸는 방식으로 구현
리스트를 정렬하여 가장 큰 값 혹은 세 번째로 큰 값을 구한다

"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        slist = list(set(nums))
        slist.sort()
        if len(slist) < 3 :
            return slist[-1]
        return slist[-3]