"""

사라지는 발판 : https://school.programmers.co.kr/learn/courses/30/lessons/92345

이차원 행렬 형태의 게임 보드와 플레이어의 시작 위치가 주어졌을 때, 양 플레이어가 최적의 플레이를 했을 때 두 캐릭터가 움직인 횟수의 합을 구하는 문제
- 보드는 1x1 크기 정사각 격자로 이루어져 있으며, 발판이 있는 부분과 없는 부분이 존재한다
- 발판이 있는 곳에만 캐릭터가 서 있을 수 있으며, 처음 캐릭터를 올려놓는 곳은 항상 발판이 있는 곳이다
- 캐릭터는 상하좌우로 인접한 4개의 칸 중에서 발판이 있는 곳으로만 이동할 수 있으며, 보드 밖으로는 이동할 수 없다
- 밟고 있던 발판은 그 위에 있던 캐릭터가 다른 곳으로 이동하면 사라진다
- 다음 상황에서 게임이 종료된다
    - 움직일 차례인데 캐릭터의 상하좌우 인접한 4칸으로 이동할 수 없는 경우, 해당 차례 플레이어는 패배한다
    - 두 캐릭터가 같은 발판 위에 있을 때, 상대 플레이어의 캐릭터가 다른 발판으로 이동하여 자신의 캐릭터가 서 있던 발판이 사라지게 되면 패배한다
- 게임은 항상 플레이어 A가 먼저 시작하며, 양 플레이어는 최적의 플레이를 한다
    - 이길 수 있는 플레이어는 최대한 빨리 승리하도록 플레이한다
    - 질 수밖에 없는 플레이어는 최대한 오래 버티도록 플레이한다
- board의 세로 및 가로 길이는 1 이상 5 이하이며, 0은 발판이 없음을, 1은 발판이 있음을 나타낸다
- aloc과 bloc은 플레이어 A와 플레이어 B의 캐릭터 초기 위치를 나타내는 좌표값이며, [r, c] 형태이다
    - 초기 보드의 aloc과 bloc 위치는 항상 발판이 있는 곳이다
    - aloc과 bloc이 같을 수 있다
- 상대 플레이어의 캐릭터가 있는 칸으로 이동할 수 있다

Example:
- Input : board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], aloc=[1, 0], bloc=[1, 2]
- Output : 5

- Input : board=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], aloc=[1, 0], bloc=[1, 2]
- Output : 4

- Input : board=[[1, 1, 1, 1, 1]], aloc=[0, 0], bloc=[0, 4]
- Output : 4

- Input : board=[[1]], aloc=[0, 0], bloc=[0, 0]
- Output : 0
- 게임을 시작하는 플레이어 A가 처음부터 어디로도 이동할 수 없으므로, A가 패배한다

Note:
MiniMax 알고리즘을 이용하여 해결
dfs 방식으로 완전 탐색하여 가능한 경우의 수를 모두 찾고, 이를 바탕으로 MiniMax 알고리즘 적용

"""

def solution(board, aloc, bloc):
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    h, w = len(board), len(board[0])

    def solve(ax, ay, bx, by):
        if board[ax][ay] == 0:
            return 0
        res = 0

        for dx, dy in move:
            nx, ny = ax + dx, ay + dy

            if nx < 0 or ny < 0 or nx >= h or ny >= w or board[nx][ny] == 0:
                continue

            board[ax][ay] = 0
            temp = solve(bx, by, nx, ny) + 1
            board[ax][ay] = 1

            if temp % 2 == 1 and res % 2 == 0:
                res = temp
            elif temp % 2 == 0 and res % 2 == 0:
                res = max(res, temp)
            elif temp % 2 == 1 and res % 2 == 1:
                res = min(res, temp)

        return res

    return solve(aloc[0], aloc[1], bloc[0], bloc[1])