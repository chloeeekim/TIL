"""

315. Count of Smaller Numbers After Self : https://leetcode.com/problems/count-of-smaller-numbers-after-self/

정수로 이루어진 리스트 nums가 주어졌을 때, 해당 인덱스 이후에 등장하는 작은 수의 개수를 구하는 문제

Example:
- Input : [5,2,6,1]
- Output : [2,1,1,0]
- 5 뒤에는 2개의 작은 수(2, 1)가 등장하는 식

Note:
특정 인덱스의 count 값은 오른쪽 subarray를 정렬했을 때 위치하게 되는 인덱스와 같다
별도로 sortarr을 생성하여 오른쪽에서부터 원소들을 하나씩 정렬된 상태의 리스트에 insert
삽입 위치를 찾기 위해 bisect 모듈 사용
구해진 counts 리스트는 순서가 뒤집혀 있으므로 reverse하여 리턴

"""

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortarr, counts = [], []
        for num in reversed(nums):
            idx = bisect.bisect_left(sortarr, num)
            sortarr.insert(idx, num)
            counts.append(idx)
        return reversed(counts)