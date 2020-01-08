"""

832. Flipping an Image : https://leetcode.com/problems/flipping-an-image/

binary matrix가 주어졌을 때, 세로축을 기준으로 뒤집고, invert한 결과를 구하는 문제
- matrix에는 0과 1만이 포함된다

Example:
- Input : [[1,1,0],[1,0,1],[0,0,0]]
- Output : [[1,0,0],[0,1,0],[1,1,1]]
- flip하면 [[0,1,1],[1,0,1],[0,0,0]]이 되고 이를 invert하면 [[1,0,0],[0,1,0],[1,1,1]]이 된다

- Input : [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
- Output : [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Note:
0과 1을 invert하는 것에 1^cell 과 같이 xor 연산을 사용했으나 속도가 느려 조건문으로 작성

"""

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A :
            flip = row[::-1]
            invert = []
            for cell in flip :
                invert.append(0 if cell == 1 else 1)
            res.append(invert)
        return res