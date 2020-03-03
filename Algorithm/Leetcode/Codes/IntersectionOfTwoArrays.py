"""

349. Intersection of Two Arrays : https://leetcode.com/problems/intersection-of-two-arrays/

두 개의 숫자가 포함된 리스트가 주어졌을 때, 교집합을 구하는 문제
- 결과 리스트에 포함되는 각 숫자는 단 한 번만 포함되어야 한다
- 결과는 어떠한 순서로 표시되건 상관 없다

Example:
- Input : nums1 = [1,2,2,1], nums2 = [2,2]
- Output : [2]

- Input : nums1 = [4,9,5], nums2 = [9,4,9,8,4]
- Output : [9,4]

Note:
중복을 허용하지 않는 set으로 변경
두 set의 교집합을 찾는 방법 : set1 & set2 / set1.intersection(set2)

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1, snums2 = set(nums1), set(nums2)
        return list(snums1 & snums2)