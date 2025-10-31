"""

내적 : https://school.programmers.co.kr/learn/courses/30/lessons/70128

길이가 같은 두 1차원 정수 배열 a, b가 주어졌을 때, a와 b의 내적을 구하는 문제
- a와 b의 내적은 다음과 같다 (n은 a, b의 길이)
    - a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] + a[n]*b[n]
- a, b의 길이는 1 이상 1,000 이하이며, a, b의 모든 수는 -1,000 이상 1,000 이하이다

Example:
- Input : a=[1,2,3,4], b=[-3,-1,0,2]
- Output : 3

- Input : a=[-1,0,1], b=[1,0,-1]
- Output : -2

Note:
a와 b의 원소들을 순서대로 곱한 다음 answer에 더해 내적을 계산

"""

def solution(a, b):
    answer = 0
    for anum, bnum in zip(a, b):
        answer += anum * bnum
    return answer