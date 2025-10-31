"""

파괴되지 않은 건물 : https://school.programmers.co.kr/learn/courses/30/lessons/92344

이차원 행렬 형태의 건물들과 사용되는 스킬들의 정보가 주어졌을 때, 최종적으로 파괴되지 않은 건물의 개수를 구하는 문제
- 건물은 적의 공격을 받으면 내구도가 감소하고, 회복 스킬을 사용하여 내구도를 높일 수 있다
- 적의 공격과 아군의 회복 스킬은 항상 직사각형 범위에 적용된다
- 내구도가 0 이하가 된 건물도 공격을 받으면 계속해서 내구도가 하락한다
- 이미 파괴된 건물도 회복 스킬을 사용하여 복구될 수 있다
- board의 행과 열 길이는 1,000 이하이며, 내구도는 1 이상 1000 이하의 정수이다
- skill의 행 길이는 1 이상 250,000 이하이다
    - skill의 원소는 [type, r1, c1, r2, c2, degree] 형태이다
    - type은 1 혹은 2로, 1인 경우 적의 공격, 2인 경우 아군의 회복 스킬을 의미한다
    - (r1, c1)부터 (r2, c2)까지 직사각형 모양의 범위 안에 있는 건물의 내구도를 degree만큼 낮추거나 높인다
    - 0 <= r1 <= r2 < board의 행의 길이이며, 0 <= c1 <= c2 < board의 열의 길이이다
    - degree는 1 이상 500 이하의 정수이다
- 최종적으로 건물의 내구도가 1 이상이라면 파괴되지 않은 건물이다

Example:
- Input : board=[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], skill=[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
- Output : 10

- Input : board=[[1,2,3],[4,5,6],[7,8,9]], skill=[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
- Output : 6

Note:
단순하게 for문 중첩으로 해결할 수 있지만, 효율성 테스트에서 시간 초과 발생
누적합(prefix sum)을 이용하여 해결

"""

def solution(board, skill):
    n, m = len(board), len(board[0])
    result = 0
    sum_list = [[0] * (m+1) for _ in range(n+1)]

    for stype, r1, c1, r2, c2, degree in skill:
        sum_list[r1][c1] += degree if stype == 2 else -degree
        sum_list[r1][c2 + 1] -= degree if stype == 2 else -degree
        sum_list[r2 + 1][c1] -= degree if stype == 2 else -degree
        sum_list[r2 + 1][c2 + 1] += degree if stype == 2 else -degree

    for i in range(n):
        for j in range(m):
            sum_list[i][j + 1] += sum_list[i][j]
    for j in range(m):
        for i in range(n):
            sum_list[i + 1][j] += sum_list[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += sum_list[i][j]
            if board[i][j] > 0:
                result += 1
    return result