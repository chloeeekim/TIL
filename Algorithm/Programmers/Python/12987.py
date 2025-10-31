"""

숫자 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/12987

A팀이 부여 받은 숫자와 출전 순서, B팀이 부여 받은 숫자가 주어졌을 때, B팀이 얻을 수 있는 최대 승점을 구하는 문제
- A, B팀은 각각 N명으로 구성된다
- 숫자 게임의 규칙은 다음과 같다
    - 모든 사원이 무작위로 자연수를 하나씩 부여받는다
    - 각 사원은 딱 한 번씩 경기를 한다
    - 각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개한다
    - 숫자가 큰 쪽이 승리하고, 승리한 사원이 속한 팀은 승점을 1점 얻는다
        - 만약 숫자가 같다면 둘 다 승점을 얻지 못한다
- A와 B의 길이는 1 이상 100,000 이하이며, 둘의 길이는 같다
    - A와 B의 원소는 1 이상 1,000,000,000 이하의 자연수이다

Example:
- Input : A=[5,1,3,7], B=[2,2,6,8]
- Output : 3

- Input : A=[2,2,2,2], B=[1,1,1,1]
- Output : 0

Note:
순서가 중요하지 않고, 언제 이길 수 있느냐가 중요하므로 A와 B 모두 내림차순으로 정렬하여 계산
B가 이길 수 있는 경우에는 무조건 이기고, B의 숫자가 A보다 작거나 같은 경우에는 다음으로 작은 A의 숫자와 비교

"""

def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)

    A_idx, B_idx = 0, 0
    res = 0
    while A_idx < len(A):
        if A[A_idx] < B[B_idx]:
            res += 1
            A_idx += 1
            B_idx += 1
        else:
            A_idx += 1
    return res