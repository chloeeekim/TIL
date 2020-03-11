"""

240. Search a 2D Matrix II : https://leetcode.com/problems/search-a-2d-matrix-ii/

m x n 사이즈의 2차원 리스트가 주어졌을 때, target이 존재하는지 찾는 문제
- 각 row에 있는 숫자들은 증가하는 순서로 정렬되어 있다
- 각 column에 있는 숫자들은 증가하는 순서로 정렬되어 있다

Example:
- Input : matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
- Output : true

- Input : matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
- Output : false

Note:
row에 target이 있으면 true
row는 정렬되어 있으므로 해당 row에 target보다 큰 값이 있다면 해당 row에는 target이 없다

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix :
            if not row :
                return False
            for num in row :
                if num == target :
                    return True
                elif num > target :
                    break
        return False