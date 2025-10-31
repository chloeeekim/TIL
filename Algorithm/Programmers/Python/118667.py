"""

두 큐 합 같게 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

길이가 같은 두 개의 큐가 주어졌을 때, 원소를 옮겨 각 큐의 원소 합이 같도록 만드는 최소 횟수를 구하는 문제
- 하나의 큐에서 pop하고, 다른 큐에 insert 하는 작업을 합쳐 1회 수행한 것으로 간주한다
- 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 리턴한다

Example:
- Input : queue1=[3, 2, 7, 2], queue2=[4, 6, 5, 1]
- Output : 2

- Input : queue1=[1, 2, 1, 2], queue2=[1, 10, 1, 2]
- Output : 7

- Input : queue1=[1, 1], queue2=[1, 5]
- Output : -1

Note:
pop 및 append 연산의 속도 개선을 위해 collections의 deque 사용
두 큐의 합이 짝수가 아니라면 같게 만들 수 없으므로 -1을 리턴
greedy한 방법으로 합이 큰 큐에서 pop, 합이 작은 큐에 append

"""

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    limit = len(queue1) * 4
    if (sum1 + sum2) % 2 == 1:
        return -1
    if sum1 == sum2:
        return 0

    for i in range(limit):
        if sum1 > sum2:
            elem = queue1.popleft()
            queue2.append(elem)
            sum1 -= elem
            sum2 += elem
        elif sum1 < sum2:
            elem = queue2.popleft()
            queue1.append(elem)
            sum1 += elem
            sum2 -= elem
        else:
            return i

    return -1