"""

정수 삼각형 : https://school.programmers.co.kr/learn/courses/30/lessons/43105

삼각형의 정보가 담긴 배열이 주어졌을 때, 특정 규칙을 통해 거쳐간 숫자의 최댓값을 구하는 문제
- 삼각형의 경로는 다음과 같이 구한다
    - 경로는 삼각형의 꼭대기에서 바닥까지 이어진다
    - 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능하다
- 삼각형의 높이는 1 이상 500 이하이다
- 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수이다

Example:
- Input : triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
- Output : 30

Note:
dp로 해결
아래에서 위쪽 방향으로 확인하면서 아래에 있는 두 개의 가능한 숫자 중 큰 값을 현재의 수에 더하는 방식

"""

def solution(triangle):
    height = len(triangle)

    for i in range(height - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]