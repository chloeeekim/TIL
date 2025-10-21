"""

네트워크 : https://school.programmers.co.kr/learn/courses/30/lessons/43162

컴퓨터의 개수와 연결에 대한 정보가 주어졌을 때, 네트워크의 개수를 구하는 문제
- 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미한다
    - 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어 있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있다면, 컴퓨터 B와 컴퓨터 C도 간접적으로 연결되어 있다
    - 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다
- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수이다
    - 각 컴퓨터는 0번부터 n-1인 정수로 표현된다
- 연결에 대한 정보가 담긴 2차원 배열 computers는 다음과 같다
    - i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현한다
    - computers[i][i]는 항상 1이다

Example:
- Input : n=3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
- Output : 2

- Input : n=3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
- Output : 1

Note:
queue를 사용하여 bfs 방식으로 해결
이전에 확인하지 않은 컴퓨터(다른 네트워크에 속하지 않은 컴퓨터)를 기준으로 bfs 방식으로 네트워크에 속한 컴퓨터를 찾는다

"""

from collections import deque

def solution(n, computers):
    visited = set()
    count = 0
    for i in range(n):
        if i in visited:
            continue

        queue = deque([i])
        count += 1
        while queue:
            now = queue.popleft()
            visited.add(now)
            for idx, conn in enumerate(computers[now]):
                if idx != now and idx not in visited and conn == 1:
                    queue.append(idx)

    return count