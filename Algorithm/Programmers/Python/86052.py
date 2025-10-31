"""

빛의 경로 사이클 : https://school.programmers.co.kr/learn/courses/30/lessons/86052

각 칸마다 S, L, 또는 R이 써져 있는 격자가 주어졌을 때, 만들어지는 빛의 경로 사이클의 모든 길이를 구하는 문제
- 격자의 각 칸에는 다음과 같은 성질이 있다
    - 빛이 S가 써진 칸에 도달한 경우, 직진한다
    - 빛이 L이 써진 칸에 도달한 경우, 좌회전한다
    - 빛이 R이 써진 칸에 도달한 경우, 우회전한다
    - 빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아온다
- 빛의 경로 사이클이란 빛이 이동하는 순환 경로를 의미한다
- 주어진 격자를 통해 만들어지는 빛의 경로 사이클의 모든 길이들을 배열에 담아 오름차순으로 정렬하여 리턴한다
- grid의 길이는 1 이상 500 이하이며, grid의 각 문자열의 길이 또한 1 이상 500 이하이다
    - grid의 모든 문자열의 길이는 서로 같다
    - grid의 모든 문자열은 'L', 'R', 'S'로 이루어져 있다

Example:
- Input : grid=["SL","LR"]
- Output : [16]

- Input : grid=["S"]
- Output : [1,1,1,1]

- Input : grid=["R","R"]
- Output : [4,4]

Note:
각 격자에서 시작하는 가능한 모든 경우의 수를 구한다
각 격자마다 4가지 방향(위로, 아래로, 왼쪽으로, 오른쪽으로)이 가능하므로, 각 방향에 대해서 모두 고려

"""

def solution(grid):
    height, width = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(width)] for _ in range(height)]
    res = []
    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    for y in range(height):
        for x in range(width):
            for d in range(4):
                if visited[y][x][d]:
                    continue
                count = 0
                ny, nx = y, x
                while not visited[ny][nx][d]:
                    count += 1
                    visited[ny][nx][d] = True
                    if grid[ny][nx] == "S":
                        pass
                    elif grid[ny][nx] == "L":
                        d = (d - 1) % 4
                    elif grid[ny][nx] == "R":
                        d = (d + 1) % 4

                    ny = (ny + dxy[d][0]) % height
                    nx = (nx + dxy[d][1]) % width

                res.append(count)
    return sorted(res)