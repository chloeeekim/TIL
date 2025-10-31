"""

나머지가 1이 되는 수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/87389

자연수 n이 주어졌을 때, n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 구하는 문제
- 답은 항상 존재한다
- n은 3 이상 1,000,000 이하의 자연수이다

Example:
- Input : n=10
- Output : 3

- Input : n=12
- Output : 11

Note:
2부터 n-1까지의 숫자를 모두 확인

"""

def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i