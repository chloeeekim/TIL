"""

등굣길 : https://school.programmers.co.kr/learn/courses/30/lessons/42898

집에서 학교까지 가는 길을 의미하는 격자의 크기와 물이 잠긴 지역의 좌표가 주어졌을 때, 학교까지 갈 수 있는 최단경로의 개수를 구하는 문제
- 집에서 학교까지 가는 길은 m x n 크기의 격자 모양으로 나타낼 수 있다
    - 집이 있는 곳의 좌표는 (1, 1)이고, 학교가 있는 곳의 좌표는 (m, n)이다
- 오른쪽과 아래쪽으로만 움직여서 학교까지 도달할 수 있다
- 격자의 크기 m, n은 1 이상 100 이하의 자연수이다
    - m과 n이 모두 1인 경우는 입력으로 주어지지 않는다
- 물에 잠긴 지역의 좌표를 담은 2차원 배열 puddles의 길이는 0 이상 10 이하이다
    - 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않는다
- 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 리턴한다

Example:
- Input : m=4, n=3, puddles=[[2, 2]]
- Output : 4

Note:
dp로 해결
(i, j) 좌표까지 올 수 있는 최단경로의 개수는 왼쪽과 위쪽에서 오는 방법을 더한 값으로, (i-1, j)와 (i, j-1) 좌표의 최단경로의 개수의 합이다
물에 잠긴 지역은 지나갈 수 없으므로 해당 좌표를 지나가는 최단 경로의 개수는 0이다

"""

def solution(m, n, puddles):
    MAXNUM = 1000000007
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MAXNUM

    return dp[n][m]