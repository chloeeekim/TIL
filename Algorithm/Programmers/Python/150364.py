"""

1,2,3 떨어트리기 : https://school.programmers.co.kr/learn/courses/30/lessons/150364

트리와 각각의 노드에 쌓인 숫자의 합 target이 주어졌을 때, target대로 리프 노드에 숫자가 쌓이게 하기 위해 숫자를 떨어뜨리는 경우의 수를 구하는 문제
- 트리의 모든 간선은 부모 노드가 자식 노드를 가리키는 단방향 간선이다
- 모든 부모 노드는 자식 노드와 연결된 간선 중 하나를 길로 설정한다
    - 자식 노드 중 가장 번호가 작은 노드를 가리키는 간선을 초기 길로 설정한다
- 게임은 다음과 같이 진행된다
    - 1. 1번 노드(루트 노드)에 숫자 1, 2, 3 중 하나를 떨어트린다
    - 2. 숫자는 길인 간선을 따라 리프 노드까지 이동한다
    - 3. 숫자가 리프 노드에 도착하면, 숫자가 지나간 각 노드는 현재 길로 연결된 자식 노드 다음으로 번호가 큰 자식 노드를 가리키는 간선을 새로운 길로 설정한다
    - 3-1. 만약 현재 길로 연결된 노드의 번호가 가장 크면, 번호가 가장 작은 노드를 가리키는 간선을 길로 설정한다
    - 3-2. 노드의 간선이 하나라면 계속 하나의 간선을 길로 설정한다
    - 4. 원하는 만큼 계속해서 루트 노드에 숫자를 떨어트릴 수 있다
    - 4-1. 단, 앞서 떨어트린 숫자가 리프 노드까지 떨어진 후에 새로운 숫자를 떨어트려야 한다
- target 대로 리프 노드에 쌓인 숫자의 합을 맞추기 위해 숫자를 떨어트리는 모든 경우 중 가장 적은 숫자를 사용하며, 그 중 사전 순으로 빠른 경우를 리턴한다
- 만약 target 대로 숫자의 합을 만들 수 없는 경우 [-1]을 리턴한다
- edges의 길이는 1 이상 100 이하이며, edges[i]는 [부모 노드 번호, 자식 노드 번호] 형태이다
- edges에는 중복이 존재하지 않으며, 항상 하나의 트리 형태로 입력이 주어진다
- 1번 노드는 항상 루트 노드이다
- target의 길이는 edges의 길이 + 1이다
- target[i]는 i+1번 노드에 쌓인 숫자의 합으로 만들어야 하는 수를 나타내며, 0 이상 100 이하의 값이다
- 리프 노드를 제외한 노드의 target 값은 항상 0이다
- target의 원소의 합은 1 이상이다

Example:
- Input : edges=[[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], target=[0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
- Output : [1, 1, 2, 2, 2, 3, 3]

- Input : edges=[[1, 2], [1, 3]], target=[0, 7, 3]
- Output : [1, 1, 3, 2, 3]

- Input : edges=[[1, 3], [1, 2]], target=[0, 7, 1]
- Output : [-1]

Note:
collection의 defaultdict를 사용하여 각 노드(key)의 자식 노드들(value)을 리스트로 저장
route[i]는 i+1번째 노드의 자식 노드로 향하는 길의 인덱스를 저장
루트 노드에서 시작하여 리프 노드까지 떨어지는 구간에서 길의 인덱스를 변경해주고, 도달한 리프 노드 번호를 order에 순서대로 저장하고, 방문 횟수를 visited 리스트에 저장
떨어트릴 수 있는 숫자는 1, 2, 3 세 종류이므로, 방문 횟수 <= target <= 방문 횟수 * 3 이어야 유효
모든 노드에 대해 target과 방문 횟수 사이의 범위가 유효하다면, 가장 적은 숫자를 사용한 것이므로 더 이상 확인할 필요는 없다
결과는 사전 순으로 가장 빠른 경우이므로, 우선 1로 채운 다음 뒤에서부터 +2, +1 하는 방식으로 결과 리스트 계산

"""

from collections import defaultdict

def solution(edges, target):
    tree, route = defaultdict(list), [0] * len(target)
    for parent, child in edges:
        tree[parent - 1].append(child - 1)
    for children in tree.values():
        children.sort()

    def check():
        count = 0
        for i, value in enumerate(target):
            if visited[i] <= value <= visited[i] * 3:
                count += 1
        return True if count == len(target) else False

    order, visited = [], [0] * len(target)
    is_continue = True
    while is_continue:
        curr = 0
        while True:
            if not tree[curr]:
                order.append(curr)
                visited[curr] += 1
                if visited[curr] > target[curr] * 3:
                    return [-1]
                if target[curr] == 0:
                    return [-1]
                if check():
                    is_continue = False
                break

            child = tree[curr][route[curr]]
            route[curr] = (route[curr] + 1) % len(tree[curr])
            curr = child
    result = [1] * len(order)
    for idx in order:
        target[idx] -= 1

    for i in range(len(order) - 1, -1, -1):
        if target[order[i]] >= 2:
            result[i] += 2
            target[order[i]] -= 2
        elif target[order[i]] == 1:
            result[i] += 1
            target[order[i]] -= 1
        else:
            continue
    return result