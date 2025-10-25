"""

거스름돈 : https://school.programmers.co.kr/learn/courses/30/lessons/12907

거스름돈과 화폐의 종류가 주어졌을 때, 거슬러 줄 수 있는 방법의 수를 구하는 문제
- 거슬러 주어야 하는 금액 n은 100,000 이하의 자연수이다
- 보유하고 있는 화폐의 종류 money의 길이는 100 이하이다
- 모든 화폐는 무한하게 있다고 가정한다
- 정답은 1,000,000,007로 나눈 나머지를 리턴한다

Example:
- Input : n=5, money=[1, 2, 5]
- Output : 4

Note:
i원을 거슬러 줄 수 있는 방법의 수는 i - [화폐 단위]원을 거슬러 줄 수 있는 방법의 수의 합이 된다

"""

def solution(n, money):
    arr = [1] + [0] * n
    for m in money:
        for i in range(m, n + 1):
            arr[i] += arr[i - m] % 1000000007

    return arr[-1]