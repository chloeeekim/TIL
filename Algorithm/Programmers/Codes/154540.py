"""

무인도 여행 : https://school.programmers.co.kr/learn/courses/30/lessons/154540

바다와 무인도에 대한 정보가 표시된 지도가 주어졌을 때, 각 섬에서 최대 며칠씩 머무를 수 있는지를 구하는 문제
- 지도는 1x1 크기의 사각형들로 이루어진 직사각형 격자 형태이다
    - 격자의 각 칸에는 "X" 또는 1부터 9 사이의 자연수가 적혀 있다
    - 지도의 "X"는 바다를 의미하며, 숫자는 무인도를 의미한다
    - 이때, 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룬다
- 지도의 각 칸에 적힌 숫자는 식량으로, 하나의 무인도 내에 적힌 숫자를 모두 합한 값은 해당 무인도에서 머무를 수 있는 최대 일수를 의미한다
- 지도를 나타내는 문자열 배열 maps와 maps[i]의 길이는 3 이상 100 이하이다
    - maps[i]는 "X" 또는 1과 9 사이의 자연수로 이루어진 문자열이다
- 각 섬에서 최대 며칠씩 머무를 수 있는지 구하여 배열에 오름차순으로 정렬하여 리턴한다
    - 만약 지낼 수 있는 무인도가 없는 경우, -1을 배열에 담아 리턴한다

Example:
- Input : maps=["X591X","X1X5X","X231X", "1XXX1"]
- Output : [1, 1, 27]

- Input : maps=["XXX","XXX","XXX"]
- Output : [-1]

Note:
queue를 사용하여 bfs 방식으로 하나의 무인도 내의 숫자의 합을 구하는 방식
visited set을 사용하여 방문한 좌표를 중복으로 계산하는 것을 방지

"""

from collections import deque

def bfs(maps, x, y, visited):
    queue = deque([(x, y)])
    total = int(maps[y][x])
    visited.add((x, y))
    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    width, height = len(maps[0]), len(maps)

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and maps[ny][nx] != "X" and (nx, ny) not in visited:
                total += int(maps[ny][nx])
                queue.append((nx, ny))
                visited.add((nx, ny))

    return total

def solution(maps):
    answer = []
    width, height = len(maps[0]), len(maps)
    visited = set()

    for i in range(height):
        for j in range(width):
            if maps[i][j] != "X" and (j, i) not in visited:
                answer.append(bfs(maps, j, i, visited))

    return sorted(answer) if answer else [-1]