"""

852. Peak Index in a Mountain Array : https://leetcode.com/problems/peak-index-in-a-mountain-array/

주어진 리스트 A가 mountain의 조건을 만족할 때, peak의 인덱스를 구하는 문제
- A[0] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]을 만족하는 0 < i < A.length-1가 있다

Example:
- Input : [0,1,0]
- Output : 1

- Input : [0,2,1,0]
- Output : 1

Note:
리스트 내의 max 값이 mountain의 조건을 만족하는 peak

"""

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))