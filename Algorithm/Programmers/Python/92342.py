"""

양궁대회 : https://school.programmers.co.kr/learn/courses/30/lessons/92342

어피치가 맞힌 과녁 점수의 개수가 주어졌을 때, 라이언이 가장 큰 점수 차이로 우승하기 위한 과녁 점수의 개수를 구하는 문제
- 어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발을 쏜다
- 만약 k점을 어피치가 a발을 맞혔고 라이언이 b발을 맞혔을 경우, 더 많은 화살을 k점에 맞힌 선수가 k점을 가져간다
- 만약 a = b일 경우 어피치가 k점을 가져간다
- 만약 최종 점수가 같을 경우 어피치를 우승자로 결정한다
- 라이언이 우승할 수 없는 경우 [-1]을 리턴한다
- info의 i번째 원소는 과녁의 10-i점을 맞힌 화살의 개수이다 (i는 0 이상 10 이하의 정수이다)
- 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 리턴한다

Example:
- Input : n=5, info=[2,1,1,1,0,0,0,0,0,0,0]
- Output : [0,2,2,0,1,0,0,0,0,0,0]

- Input : n=1, info=[1,0,0,0,0,0,0,0,0,0,0]
- Output : [-1]

- Input : n=9, info=[0,0,1,2,0,1,1,1,1,1,1]
- Output : [1,1,2,0,1,2,2,0,0,0,0]

- Input : n=10, info=[0,0,0,0,0,0,0,0,3,4,3]
- Output : [1,1,1,1,1,1,1,1,0,0,2]

Note:
bfs 방식으로 해결
k점을 얻기 위해서는 어피치보다 1발 더 많이 맞히면 된다
우승 방법이 여러 가지일 경우, 가장 낮은 점수를 더 많이 맞힌 경우가 답이므로, 0점에 다 맞힌다

"""

from collections import deque

def solution(n, info):
    def calc_gap(ryan):
        rscore, ascore = 0, 0
        for i in range(11):
            if info[i] > 0 or ryan[i] > 0:
                if info[i] >= ryan[i]:
                    ascore += (10 - i)
                else:
                    rscore += (10 - i)
        return rscore - ascore

    queue = deque()
    queue.append([[0]*11, n, 0])
    max_score, res = -1, [-1]*11

    while queue:
        ryan, remain, idx = queue.popleft()
        if remain == 0 or idx == 11:
            gap = calc_gap(ryan)
            if gap > 0:
                if remain != 0:
                    ryan[-1] += remain
                if max_score < gap:
                    max_score = gap
                    res = ryan.copy()
                elif max_score == gap:
                    for i in range(10, -1, -1):
                        if res[i] > ryan[i]:
                            break
                        elif res[i] < ryan[i]:
                            res = ryan.copy()
                            break
        else:
            ryan[idx] = 0
            queue.append([ryan.copy(), remain, idx+1])
            if remain > info[idx]:
                ryan[idx] = info[idx] + 1
                queue.append([ryan.copy(), remain - (info[idx] + 1), idx+1])

    return res if max_score != -1 else [-1]