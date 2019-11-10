"""

566. Reshape the Matrix : https://leetcode.com/problems/reshape-the-matrix/

2차원 리스트(matrix)가 주어졌을 때, 이를 r * c matrix로 변환하는 문제
- 변환된 matrix는 원본 matrix와 동일한 row-traversing order를 지녀야 한다
- 만약 r * c matrix로 변환이 불가능한 경우 원본 matrix를 리턴한다
- 주어지는 matrix의 길이와 너비는 [1,100] 범위에 존재한다
- 주어지는 r(row)과 c(column)은 모두 양의 정수이다

Example:
- Input : [[1,2],[3,4]], r = 1, c = 4
- Output : [[1,2,3,4]]

- Input : [[1,2],[3,4]], r = 2, c = 4
- Output : [[1,2],[3,4]]
- 2*2 matrix를 2*4 matrix로 변환할 수 없으므로 원본을 리턴

Note:
원본 matrix의 size를 계산하여 변환이 불가능한 경우 원본을 리턴
변환이 가능한 경우, 1차원 리스트로 flatten하고, 해당 리스트를 사이즈에 맞게 잘라서 붙이는 방법으로 구현
참고) runtime 100% / memory 100%

"""

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(nums) * len(nums[0])
        if r * c != size :
            return nums
        flatten = []
        for i in range(len(nums)) :
            flatten += nums[i]
        idx, res = 0, []
        while idx < size :
            res.append(flatten[idx:idx+c])
            idx += c
        return res