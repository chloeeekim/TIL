"""

약수의 개수와 덧셈 : https://school.programmers.co.kr/learn/courses/30/lessons/77884

left부터 right까지의 모든 수들 중에서 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 구하는 문제
- left와 right는 정수이다
- 1 <= left <= right <= 1,000 이다

Example:
- Input : left=13, right=17
- Output : 43
- 16만 약수의 개수가 홀수(5개)이고, 나머지는 약수의 개수가 짝수이다

- Input : left=24, right=27
- Output : 52
- 25만 약수의 개수가 홀수(3개)이고, 나머지는 약수의 개수가 짝수이다

Note:
어떤 숫자의 제곱인 숫자만 약수의 개수가 홀수이다
숫자의 제곱근이 정수라면 약수의 개수가 홀수, 정수가 아니라면 약수의 개수가 짝수

"""

def solution(left, right):
    res = 0
    for i in range(left, right+1):
        if (i ** 0.5).is_integer():
            res -= i
        else:
            res += i
    return res