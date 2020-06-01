"""

941. Valid Mountain Array : https://leetcode.com/problems/valid-mountain-array/

정수로 이루어진 리스트 A가 주어졌을 때, 아래의 조건을 만족하는 mountain array인지 확인하는 문제
- A의 길이는 3 이상이어야 하며, 0 < i < A.length - 1인 i에 대해 A[0] < A[1] < ... < A[i], A[i] > A[i+1] > ... > A[A.length - 1]을 만족하는 경우 mountain array이다
- 주어지는 A의 길이는 0 이상 10000 이하이다
- A에 포함된 원소 값의 범위는 0 이상 10000 이하이다

Example:
- Input : [2,1]
- Output : false

- Input : [3,5,5]
- Output : false

- Input : [0,3,2,1]
- Output : true

Note:
최대값의 인덱스를 찾아 리스트의 양 끝이라면 조건을 만족하지 않으므로 무조건 false
최대값을 기준으로 양 옆으로 decreasing array여야 조건을 만족하므로, decreasing array인지 확인

"""

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        maxidx = A.index(max(A))
        if maxidx == 0 or maxidx == len(A)-1:
            return False
        for i in range(maxidx):
            if A[i] >= A[i+1]:
                return False
        for i in range(maxidx, len(A)-1):
            if A[i] <= A[i+1]:
                return False
        return True