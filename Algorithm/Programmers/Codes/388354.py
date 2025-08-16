"""

홀짝트리 : https://school.programmers.co.kr/learn/courses/30/lessons/388354

루트 노드가 설정되지 않은 포레스트가 주어졌을 때, 홀짝 트리와 역홀짝 트리가 될 수 있는 트리의 개수를 구하는 문제
- 모든 노드들은 서로 다른 번호가 주어진다
- 각 노드의 정의는 다음과 같다
    - 홀수 노드: 노드의 번호가 홀수이며, 자식 노드의 개수가 홀수인 노드
    - 짝수 노드: 노드의 번호가 짝수이며, 자식 노드의 개수가 짝수인 노드
    - 역홀수 노드: 노드의 번호가 홀수이며, 자식 노드의 개수가 짝수인 노드
    - 역짝수 노드: 노드의 번호가 짝수이며, 자식 노드의 개수가 홀수인 노드
    - 0은 짝수이다
- 각 트리의 정의는 다음과 같다
    - 홀짝 트리: 홀수 노드와 짝수 노드로만 이루어진 트리
    - 역홀짝 트리: 역홀수 노드와 역짝수 노드로만 이루어진 트리
- 하나의 트리가 홀짝 트리와 역홀짝 트리 두 가지 모두 될 수 있거나 두 가지 모두 될 수 없을 수도 있다
- nodes의 길이는 1 이상 400,000 이하이며, nodes의 원소는 1 이상 1,000,000 이하인 정수로 중복되지 않는다
- edges의 길이는 1 이상 1,000,000 이하이다
- edges의 원소는 [a, b] 형태의 정수 배열이며, a번 노드와 b번 노드 사이에 무방향 간선이 존재한다는 것을 의미한다
    - a, b는 nodes에 존재하는 원소이며, 서로 다른 값이다
- 포레스트인 경우만 입력으로 주어진다

Example:
- Input : nodes=[11, 9, 3, 2, 4, 6], edges=[[9, 11], [2, 3], [6, 3], [3, 4]]
- Output : [1, 0]

- Input : nodes=[9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10], edges=[[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]]
- Output : [2, 1]

Note:
첫 시도로 bfs 방식으로 모든 노드를 루트 노드로 설정해보고 트리가 홀짝 트리인지 역홀짝 트리인지 확인하였으나, 시간 초과 발생
어떤 노드가 루트일 때 홀수 노드라면 자식이 되면 역홀수 노드가 되고, 짝수 노드라면 자식이 되면 역짝수 노드가 된다
반대로 역홀수 노드는 홀수 노드로, 역짝수 노드는 짝수 노드가 된다
따라서 자식 노드인지 여부에 상관없이 홀짝 노드와 역홀짝 노드의 개수를 세어 계산할 수 있다
1개만 역홀짝 노드라면, 해당 노드를 루트로 했을 때 역홀짝 트리가 되고,
1개만 홀짝 노드라면, 해당 노드를 루트로 했을 때 홀짝 트리가 된다

"""

from collections import defaultdict, deque

def solution(nodes, edges):
    forests = defaultdict(list)
    for a, b in edges:
        forests[a].append(b)
        forests[b].append(a)

    result = [0, 0]
    visited = [False] * 1000001
    for node in nodes:
        if visited[node]:
            continue

        queue = deque([node])
        normal, reverse = 0, 0
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            c_mod = len(forests[curr]) % 2

            if curr % 2 == c_mod:
                normal += 1
            else:
                reverse += 1

            queue.extend(child for child in forests[curr] if not visited[child])

        if normal == 1:
            result[0] += 1
        if reverse == 1:
            result[1] += 1

    return result