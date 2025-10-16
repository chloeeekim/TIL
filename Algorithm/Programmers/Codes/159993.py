"""

미로 탈출 : https://school.programmers.co.kr/learn/courses/30/lessons/159993

1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하는 데 필요한 최소 시간을 구하는 문제
- 각 칸은 통로 또는 벽으로 이루어져 있다
- 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있다
- 레버 또한 통로들 중 한 칸에 있다
- 출발 지점에서 레버가 있는 칸으로 이동하여 레버를 당긴 후, 미로를 빠져나가는 문이 있는 칸으로 이동하여 탈출할 수 있다
- 미로에서 한 칸을 이동하는데 1초가 소요된다
- 미로를 나타낸 문자열 배열 maps와 maps[i]의 길이는 5 이상 100 이하이다
    - maps[i]는 다음 다섯 개의 문자들로만 이루어져 있다
        - S: 시작 지점
        - E: 출구
        - L: 레버
        - O: 통로
        - X: 벽
    - 시작 지점과 출구, 레버는 항상 다른 곳에 존재하며, 한 개씩만 존재한다
    - 출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있다
- 미로를 탈출할 수 없는 경우 -1을 리턴한다

Example:
- Input : maps=["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
- Output : 16

- Input : maps=["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
- Output : -1

Note:
어떤 시작지점에서 특정 문자가 있는 위치까지 이동하는 데 필요한 최소 시간을 구하는 calcMin 함수 작성
calcMin에서는 queue를 사용하여 BFS로 최소 거리를 구하는 방식
시작 지점에서 레버까지, 레버에서 출구까지 각각 최소 거리를 구한 다음 더하여 답을 계산
만약 둘 중 한 경우라도 종료 지점까지 도달할 수 없는 경우 -1을 리턴

"""

from collections import deque

def calcMin(maps, start_x, start_y, end):
    width, height = len(maps[0]), len(maps)
    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[9999999 for _ in range(width)] for _ in range(height)]
    visited[start_y][start_x] = 0

    queue = deque([(start_x, start_y, 0)])
    while queue:
        x, y, dist = queue.popleft()

        if maps[y][x] == end:
            return dist

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maps[ny][nx] != "X":
                if visited[ny][nx] > dist + 1:
                    visited[ny][nx] = dist + 1
                    queue.append((nx, ny, dist + 1))

    return -1

def solution(maps):
    spoint, lpoint = [], []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                spoint = [i, j]
            elif maps[i][j] == "L":
                lpoint = [i, j]

    answer = []
    answer.append(calcMin(maps, spoint[1], spoint[0], "L"))
    answer.append(calcMin(maps, lpoint[1], lpoint[0], "E"))

    return -1 if -1 in answer else sum(answer)