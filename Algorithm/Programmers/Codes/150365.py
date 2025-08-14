"""

미로 탈출 명령어 : https://school.programmers.co.kr/learn/courses/30/lessons/150365

n x m 크기의 격자 미로가 주어졌을 때, k만큼 이동하여 탈출하는 경로를 구하는 문제
- (x, y)에서 시작하여 (r, c)까지 이동하여야 한다
- (x, y)와 (r, c)를 포함하여 같은 위치를 두 번 이상 방문할 수 있다
- 미로에서 탈출한 경로를 문자열로 나타냈을 때, 사전 순으로 가장 빠른 경로로 탈출해야 한다
    - l: 왼쪽으로 한 칸 이동 / r: 오른쪽으로 한 칸 이동 / u: 위쪽으로 한 칸 이동 / d: 아래쪽으로 한 칸 이동
- 조건대로 미로를 탈출할 수 없는 경우 "impossible"을 리턴한다
- (x, y)와 (r, c)는 서로 다른 위치로 주어진다

Example:
- Input : n=3, m=4, x=2, y=3, r=3, c=1, k=5
- Output : "dllrl"

- Input : n=2, m=2, x=1, y=1, r=2, c=2, k=2
- Output : "dr"

- Input : n=3, m=3, x=1, y=2, r=3, c=3, k=4
- Output : "impossible"

Note:
시작점과 도착점의 최단 거리가 k보다 크다면 impossible
bfs 방식으로, 사전순으로 빠른 d, l, r, u 순서로 탐색
도착지점에 도달했는데 아직 k만큼 움직이지 않은 경우, 남은 거리가 2의 배수여야 다시 돌아올 수 있다

"""

def solution(n, m, x, y, r, c, k):
    direction = {(1, 0): "d", (0, -1): "l", (0, 1): "r", (-1, 0): "u"}

    def distance(i, j):
        return abs(i - (r-1)) + abs(j - (c-1))

    if distance(x-1, y-1) > k or (distance(x-1, y-1) - k) % 2 == 1:
        return "impossible"

    queue = [[x-1, y-1, 0, ""]]

    while queue:
        i, j, d, temp = queue.pop(0)

        if i == r-1 and j == c-1:
            if d == k:
                return temp
            elif (k - d) % 2 == 1:
                return "impossible"

        for di, dj in direction:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m:
                if distance(ni, nj) + d + 1 > k:
                    continue

                queue.append([ni, nj, d + 1, temp + direction[(di, dj)]])
                break

    return "impossible"