"""

[PCCP 기출문제] 2번 / 석유 시추 : https://school.programmers.co.kr/learn/courses/30/lessons/250136

2차원 형태의 땅 속에 석유가 여러 덩어리로 나누어 묻혀 있을 때, 수직으로 단 하나의 시추관을 뚫어 뽑을 수 있는 가장 많은 석유량을 구하는 문제
- 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있다
- land[i][j]가 0이면 빈 땅을, 1이면 석유가 있는 땅을 의미한다

Example:
- Input : land=
[
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1]
]
- Output : 9

- Input : land=
[
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
]
- Output : 16

Note:
5의 양을 가진 석유 덩어리가 2부터 4까지 분포해 있다면 2, 3, 4 어디서 시추하던 5만큼을 추출 가능
bfs 방식으로 석유 덩어리의 총량과 분포해 있는 가로 범위를 구하는 방식

"""

def solution(land):
    n, m = len(land), len(land[0])
    total = [0] * m

    def bfs(i, j):
        queue = []
        queue.append([i, j])
        land[i][j] = -1
        size = 1
        min_j = max_j = j

        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                    land[nx][ny] = -1
                    queue.append([nx, ny])
                    size += 1
                    min_j = min(min_j, ny)
                    max_j = max(max_j, ny)
        return size, min_j, max_j

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                size, min_j, max_j = bfs(i, j)
                for k in range(min_j, max_j + 1):
                    total[k] += size

    return max(total)