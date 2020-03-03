"""

88. Merge Sorted Array : https://leetcode.com/problems/merge-sorted-array/

두 개의 정렬된 list가 주어졌을 때, 하나의 정렬된 list로 만드는 문제
- nums2를 nums1 리스트에 merge
- nums1과 nums2에 포함된 element의 개수는 m과 n이다
- nums1에는 m+n과 같거나 큰 공간이 생성되어 있다

Example:
- Input : nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Output : [1,2,2,3,5,6]

Note:
앞에서부터 추가하면 리스트를 뒤로 밀어야 한다는 문제점
따라서 뒤에서부터 비교하여 뒤에서부터 채우는 방법으로 해결
참고) 더 깔끔한 코드가 가능하지 않을까?

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr, i, j = m + n - 1, m - 1, n - 1
        while i >= 0 and j >= 0 :
            if nums1[i] > nums2[j] :
                nums1[ptr] = nums1[i]
                i -= 1
            else :
                nums1[ptr] = nums2[j]
                j -= 1
            ptr -= 1
        while j >= 0 :
            nums1[ptr] = nums2[j]
            j -= 1
            ptr -= 1