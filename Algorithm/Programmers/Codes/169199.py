"""

리코쳇 로봇 : https://school.programmers.co.kr/learn/courses/30/lessons/169199

보드게임판의 정보가 주어졌을 때, 말이 목표위치에 도달하는 데 최소 몇 번 이동해야 하는지 구하는 문제
- 리코쳇 로봇이라는 보드게임은 다음과 같이 진행된다
    - 말은 시작위치에서 출발한다
    - 현재 위치에서 상, 하, 좌, 우 중 한 방향으로 게임판 위의 장애물이나 게임판 가장자리까지 부딪힐 때까지 미끄러져 움직이는 것을 한 번의 이동으로 정의한다
    - 목표 위치에 정확하게 멈추는 것을 목표로 한다
- 게임판의 상태를 나타내는 문자열 배열 board의 길이는 3 이상 100 이하이다
    - board의 원소의 길이는 3 이상 100 이하이다
    - board의 원소의 길이는 모두 동일하다
    - 문자열은 ".", "D", "R", "G"로만 구성되어 있다
        - "."는 빈 공간, "D"는 장애물, "R"은 시작 위치, "G"는 목표 위치를 의미한다
    - "R"과 "G"는 한 번씩만 등장한다
- 만약 목표위치에 도달할 수 없다면 -1을 리턴한다

Example:
- Input : board=["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
- Output : 7

- Input : board=[".D.R", "....", ".G..", "...D"]
- Output : -1

Note:
queue를 사용하여 BFS 방식으로 탐색
count 배열에 해당 위치에 도달하기 위한 최소 횟수를 저장

"""

from collections import deque

def solution(board):
    queue = deque()
    width, height = len(board[0]), len(board)
    count = [[999999999 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if board[i][j] == "R":
                queue.append((j, i, 0))
        if queue:
            break

    d = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

    while queue:
        x, y, dist = queue.popleft()

        if board[y][x] == "G":
            return dist

        for di in ["U", "D", "L", "R"]:
            nx, ny = x, y
            while 0 <= nx + d[di][0] < width and 0 <= ny + d[di][1] < height and board[ny+d[di][1]][nx+d[di][0]] != "D":
                nx += d[di][0]
                ny += d[di][1]

            if count[ny][nx] > dist + 1:
                count[ny][nx] = dist + 1
                queue.append((nx, ny, dist + 1))

    return -1