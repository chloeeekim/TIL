"""

k진수에서 소수 개수 구하기 : https://school.programmers.co.kr/learn/courses/30/lessons/92335

양의 정수 n을 k진수로 바꿨을 때, 변환된 수 안에 특정 조건을 만족하는 소수가 몇 개인지 확인하는 문제
- 다음 조건을 만족하는 소수(Prime number)의 개수를 리턴한다
    - 0P0처럼 소수 양쪽에 0이 있는 경우
    - P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    - 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
    - P처럼 소수 양쪽에 아무것도 없는 경우
    - 단, P는 각 자릿수에 0을 포함하지 않는 소수이다

Example:
- Input : n=437674, k=3
- Output : 3
- 437674를 3진법으로 바꾸면 211020101011 이고, 소수는 211, 2, 11 세 개가 존재한다

- Input : n=110011, k=10
- Output : 2

Note:
change 함수를 작성하여 숫자 n을 k진법으로 변경
check_is_prime 함수를 작성하여 숫자가 소수인지 판별

"""

import math

def solution(n, k):
    def change(n, k):
        res = ''
        while n > 0:
            n, mod = divmod(n, k)
            res += str(mod)
        return res[::-1]

    def check_is_prime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    sp = change(n, k).split('0')
    res = 0
    for n in sp:
        if n == '' or n == '1':
            continue
        if check_is_prime(int(n)):
            res += 1

    return res