"""

[PCCP 기출문제] 4번 / 수레 움직이기 : https://school.programmers.co.kr/learn/courses/30/lessons/250134

2차원 격자 위에서 빨간색과 파란색 수레를 각자의 시작 칸에서 도착 칸까지 이동시킬 때, 퍼즐을 푸는 데 필요한 턴의 최솟값을 구하는 문제
- 각 턴마다 반드시 모든 수레를 상하좌우로 인접한 칸 중 한 칸으로 움직여야 한다
- 수레는 벽이나 격자 밖으로 움직일 수 없다
- 수레는 자신이 방문했던 칸으로 움직일 수 없다
- 자신의 도착 칸에 위치한 수레는 움직이지 않는다. 즉 해당 칸에 계속 고정된다
- 동시에 두 수레를 같은 칸으로 움직일 수 없다
- 수레끼리 자리를 바꾸며 움직일 수 없다
- 퍼즐을 풀 수 없는 경우 0을 리턴한다
- maze[i][j]는 0, 1, 2, 3, 4, 5 중 하나의 값을 갖는다
    - 0: 빈칸 / 1: 빨간 수레의 시작 칸 / 2: 파란 수레의 시작 칸 / 3: 빨간 수레의 도착 칸 / 4: 파란 수레의 도착 칸 / 5: 벽

Example:
- Input : maze=[[1, 4], [0, 0], [2, 3]]
- Output : 3

- Input : maze=[[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
- Output : 7

- Input : maze=[[1, 5], [2, 5], [4, 5], [3, 5]]
- Output : 0
- 파란 수레가 도착칸에 위치한 후 고정되어 빨간 수레가 도착 칸에 도착할 수 없다

- Input : maze=[[4, 1, 2, 3]]
- Output : 0
- 수레는 서로 자리를 바꾸며 움직일 수 없으므로 퍼즐 해결이 불가능하다

Note:
dfs 방식으로 해결
visited 배열을 이용하여 이전에 방문했던 칸인지 확인

"""

import sys

def solution(maze):
    n, m = len(maze), len(maze[0])
    red_visited = [[False] * m for _ in range(n)]
    blue_visited = [[False] * m for _ in range(n)]
    red_start, red_end, blue_start, blue_end = [], [], [], []
    min_time = sys.maxsize

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = [i, j]
            elif maze[i][j] == 2:
                blue_start = [i, j]
            elif maze[i][j] == 3:
                red_end = [i, j]
            elif maze[i][j] == 4:
                blue_end = [i, j]
            else:
                continue

    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def dfs(red, blue, time, red_visited, blue_visited):
        nonlocal min_time

        if time > min_time:
            return

        red_finished = red[0] == red_end[0] and red[1] == red_end[1]
        blue_finished = blue[0] == blue_end[0] and blue[1] == blue_end[1]

        if red_finished and blue_finished:
            min_time = min(min_time, time)
            return

        red_visited[red[0]][red[1]] = True
        blue_visited[blue[0]][blue[1]] = True

        red_range = 4 if not red_finished else 1
        blue_range = 4 if not blue_finished else 1

        for i in range(red_range):
            if red_finished:
                red_x, red_y = red[0], red[1]
            else:
                red_x, red_y = red[0] + move[i][0], red[1] + move[i][1]

                if red_x < 0 or red_x > n-1 or red_y < 0 or red_y > m-1:
                    continue
                if red_visited[red_x][red_y]:
                    continue
                if maze[red_x][red_y] == 5:
                    continue

            for j in range(blue_range):
                if blue_finished:
                    blue_x, blue_y = blue[0], blue[1]
                else:
                    blue_x, blue_y = blue[0] + move[j][0], blue[1] + move[j][1]

                    if blue_x < 0 or blue_x > n-1 or blue_y < 0 or blue_y > m-1:
                        continue
                    if blue_visited[blue_x][blue_y]:
                        continue
                    if maze[blue_x][blue_y] == 5:
                        continue

                if red == [blue_x, blue_y] and blue == [red_x, red_y]:
                    continue
                if red_x == blue_x and red_y == blue_y:
                    continue

                dfs([red_x, red_y], [blue_x, blue_y], time+1, red_visited, blue_visited)

        red_visited[red[0]][red[1]] = False
        blue_visited[blue[0]][blue[1]] = False

    dfs(red_start, blue_start, 0, red_visited, blue_visited)

    if min_time == sys.maxsize:
        return 0
    else:
        return min_time