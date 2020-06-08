"""

350. Intersection of Two Arrays II : https://leetcode.com/problems/intersection-of-two-arrays-ii/

두 개의 숫자가 포함된 리스트가 주어졌을 때, 교집합을 구하는 문제
- 결과 리스트에 포함되는 각 숫자는 겹치는 만큼 포함되어야 한다
- 결과는 어떠한 순서로 표시되건 상관 없다

Example:
- Input : nums1 = [1,2,2,1], nums2 = [2,2]
- Output : [2,2]

- Input : nums1 = [4,9,5], nums2 = [9,4,9,8,4]
- Output : [9,4]

Note:
- Solution 1
중복을 허용하지 않는 set으로 변경
두 set의 교집합을 찾는 방법 : set1 & set2 / set1.intersection(set2)
교집합에 포함된 원소들의 갯수를 확인하여 결과 list에 append
- Solution 2
Counter를 이용하여 두 리스트에 포함된 원소의 개수를 카운트
& 연산을 이용하여 중복을 찾는 방식

"""

# Solution 1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1, snums2 = set(nums1), set(nums2)
        interlist = list(snums1 & snums2)
        res = []
        for i in interlist :
            r = min(nums1.count(i), nums2.count(i))
            res += [i] * r
        return res

# Solution 2
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnums1, cnums2 = Counter(nums1), Counter(nums2)
        res = []
        for num, count in (cnums1&cnums2).items():
            res += [num]*count
        return res