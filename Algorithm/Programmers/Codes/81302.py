"""

거리두기 확인하기 : https://school.programmers.co.kr/learn/courses/30/lessons/81302

5개의 대기실의 구조와 자리에 앉아있는 응시자들의 정보가 주어졌을 때, 각 대기실별로 거리두기를 지키고 있는지 확인하는 문제
- 대기실은 총 5개이며, 각 대기실은 5x5 크기이다
- 응시자들끼리는 맨해튼 거리가 2 이하로 앉은 경우 거리두기를 지키지 않은 것으로 간주한다
    - 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용한다
- 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않은 경우 0을 배열에 담아 리턴한다
- places의 행 길이는 5(대기실의 개수)이며, 각 행은 하나의 대기실 구조를 나타낸다
- places의 원소는 P, O, X로 이루어진 문자열이다
    - P는 응시자가 앉아있는 자리를 의미한다
    - O는 빈 테이블을 의미한다
    - X는 파티션을 의미한다

Example:
- Input : places=[
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]
- Output : [1, 0, 1, 1, 1]

Note:
각 응시자들의 위치로부터 시작하여 dfs를 사용하여 해결

"""

from collections import deque

def solution(places):
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(plcae):
        start = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    start.append((i, j))

        for s in start:
            queue = deque([(s[0], s[1], 0)])
            visited = [[0] * 5 for _ in range(5)]
            visited[s[0]][s[1]] = 1

            while queue:
                x, y, distance = queue.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                        if place[nx][ny] == "O":
                            queue.append((nx, ny, distance + 1))
                            visited[nx][ny] = 1
                        if place[nx][ny] == "P" and distance <= 1:
                            return 0
        return 1

    res = []
    for place in places:
        res.append(dfs(place))
    return res