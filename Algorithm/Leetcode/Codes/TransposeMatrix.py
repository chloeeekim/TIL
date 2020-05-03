"""

867. Transpose Matrix : https://leetcode.com/problems/transpose-matrix/

matrix A가 주어졌을 때, 이를 transpose한 결과를 구하는 문제

Example:
- Input : [[1,2,3],[4,5,6],[7,8,9]]
- Output : [[1,4,7],[2,5,8],[3,6,9]]

- Input : [[1,2,3],[4,5,6]]
- Output : [[1,4],[2,5],[3,6]]

Note:
A[x][y]를 A[y][x]로 변환하면 되므로 이중 for문으로 해결

"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[x][y] for x in range(len(A))] for y in range(len(A[0]))]