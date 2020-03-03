"""

62. Unique Paths : https://leetcode.com/problems/unique-paths/

두 정수 m, n이 주어졌을 때, m x n 사이즈의 그리드의 왼쪽 위에서 오른쪽 아래까지 도달하는 방법의 수를 구하는 문제
- 한 번에 한 칸만 아래 혹은 오른쪽으로 이동할 수 있다
- m과 n은 최대 100 이하의 정수이다

Example:
- Input : m = 3, n = 2
- Output : 3
- (right-right-down), (right-down-right), (down-right-right) 세 가지 방법 존재

- Input : m = 7, n = 3
- Output : 28

Note:
특정 칸에 도달하기 위한 방법의 수 : 위쪽 칸에 도달하기 위한 방법의 수 + 왼쪽 칸에 도달하기 위한 방법의 수
list를 특정 값(value)로 초기화 : lst = [value for i in range(size)]

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cal = [[0 for i in range(m)] for i in range(n)]
        for i in range(n) :
            for j in range(m) :
                if i == 0 or j == 0 :
                    cal[i][j] = 1
                else :
                    cal[i][j] = cal[i-1][j] + cal[i][j-1]
        return cal[-1][-1]