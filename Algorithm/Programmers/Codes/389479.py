"""

서버 증설 횟수 : https://school.programmers.co.kr/learn/courses/30/lessons/389479

시간대에 따른 게임 이용자 수가 주어졌을 때, 모든 게임 이용자를 감당하기 위한 최소 서버 증설 횟수를 구하는 문제
- 같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가로 필요하다
    - 이용자가 n x m명 이상 (n + 1) x m명 미만이라면 n대의 증설된 서버가 운영 중이어야 한다
- 한 번 증설한 서버는 k 시간 동안 운영하고, 그 이후에는 반납한다

Example:
- Input : players=[0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], m=3, k=5
- Output : 7

- Input : players=[0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], m=5, k=1
- Output : 11

- Input : players=[0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], m=1, k=1
- Output : 12

Note:
시간대 별로 몇 개의 서버가 증설되었는지 저장하는 배열을 사용
서버 증설이 필요한 경우 해당 시간대부터 k시간 동안 증설된 서버 유지

"""

def solution(players, m, k):
    total = 0
    servers = [0 for _ in range(24)]
    for i, player in enumerate(players):
        if player // m > servers[i]:
            add = player // m - servers[i]
            for j in range(i, i+k):
                if j >= 24:
                    break
                servers[j] += add
            total += add
    return total