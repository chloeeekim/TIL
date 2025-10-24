"""

이중우선순위큐 : https://school.programmers.co.kr/learn/courses/30/lessons/42628

이중우선순위큐가 처리할 연산들이 주어졌을 때, 모든 연산을 처리한 후 남아있는 최댓값과 최솟값을 구하는 문제
- 다음 연산들이 주어진다
    - "I 숫자": 큐에 주어진 숫자를 삽입한다
    - "D 1": 큐에서 최댓값을 삭제한다
    - "D -1": 큐에서 최솟값을 삭제한다
- 모든 연산을 처리한 후 [최댓값, 최솟값] 배열을 리턴한다
    - 큐가 비어있는 경우 [0, 0]을 리턴한다
- operations는 길이 1 이상 1,000,000 이하인 문자열 배열이다
    - operations의 원소는 큐가 수행할 연산을 나타낸다
    - 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제한다
    - 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시한다

Example:
- Input : operations=["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
- Output : [0, 0]

- Input : operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
- Output : [333, -45]

Note:
heapq를 사용하여 max heap과 min heap을 둘 다 정의하여 해결
heapq는 기본적으로 최소힙으로 동작하기 때문에 음수로 변경하여 push함으로써 최대힙 구현
하나의 heap에서 pop하게 되면 다른 heap에서도 해당 데이터를 삭제

"""

import heapq

def solution(operations):
    minheap, maxheap = [], []
    for operation in operations:
        op, num = operation.split(" ")
        if op == "I":
            heapq.heappush(minheap, int(num))
            heapq.heappush(maxheap, -int(num))
        elif op == "D":
            num = int(num)
            if not minheap:
                continue

            if num == 1:
                maxnum = -heapq.heappop(maxheap)
                minheap.remove(maxnum)
            elif num == -1:
                minimum = heapq.heappop(minheap)
                maxheap.remove(-minimum)

    return [-maxheap[0], minheap[0]] if minheap else [0, 0]