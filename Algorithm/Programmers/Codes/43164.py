"""

여행경로 : https://school.programmers.co.kr/learn/courses/30/lessons/43164

항공권의 정보들이 주어졌을 때, 주어진 항공권을 모두 이용하는 공항 경로를 구하는 문제
- 항상 "ICN" 공항에서 출발한다
- 모든 공항은 알파벳 대문자 3글자로 이루어진다
- 주어진 공항 수는 3개 이상 10,000개 이하이다
- 항공권 정보가 담긴 2차원 배열 tickets의 원소는 [a, b] 형태로, a 공항에서 b 공항으로 가는 항공권이 있다는 의미이다
- 주어진 항공권은 모두 사용해야 한다
- 만약 가능한 경로가 2개 이상일 경우, 알파벳 순서가 앞서는 경로를 리턴한다
- 모든 도시를 방문할 수 없는 경우는 주어지지 않는다

Example:
- Input : tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
- Output : ["ICN", "JFK", "HND", "IAD"]

- Input : tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
- Output : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

Note:
queue를 사용하여 bfs 방식으로 해결
모든 항공권을 다 사용한 경우 answer 리스트에 추가하고, 최종적으로는 answer 리스트를 알파벳 순으로 정렬하여 첫 번째 경로를 리턴

"""

from collections import deque

def solution(tickets):
    answer = []
    l = len(tickets)
    queue = deque([("ICN", ["ICN"], [])])
    while queue:
        airport, route, used = queue.popleft()

        if len(used) == l:
            answer.append(route)
            continue

        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and idx not in used:
                queue.append((ticket[1], route + [ticket[1]], used + [idx]))

    return sorted(answer)[0]