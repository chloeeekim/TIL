"""

718. Maximum Length of Repeated Subarray : https://leetcode.com/problems/maximum-length-of-repeated-subarray/

숫자로 이루어진 두 리스트 A, B가 주어졌을 때, 두 list 모두에서 발견되는 subarray의 최대 길이를 구하는 문제
- A와 B의 길이는 1000을 넘지 않는다
- A와 B에 속하는 원소들의 값은 0 이상 100 미만이다

Example:
- Input : A = [1,2,3,2,1], B = [3,2,1,4,7]
- Output : 3
- [3,2,1]이 최대 길이의 repeated subarray

Note:
dp로 해결
arr[i][j]에는 A[i:]와 B[j:]로 시작하여 만들 수 있는 subarray의 길이를 저장

"""

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        alen, blen = len(A), len(B)
        arr = [[0 for _ in range(blen+1)] for _ in range(alen+1)]
        for i in range(alen-1, -1, -1):
            for j in range(blen-1, -1, -1):
                if A[i] == B[j]:
                    arr[i][j] = arr[i+1][j+1]+1
        return max(max(row) for row in arr)