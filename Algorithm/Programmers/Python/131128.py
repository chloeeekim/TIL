"""

숫자 짝꿍 : https://school.programmers.co.kr/learn/courses/30/lessons/131128

두 정수 X, Y가 주어졌을 때, 두 수의 짝꿍을 구하는 문제
- 숫자 짝꿍이란 두 정수의 임의의 자리에서 공통으로 나타나는 정수들을 이용하여 만들 수 있는 가장 큰 정수를 의미한다
    - 짝꿍이 존재하지 않는 경우, 짝꿍은 -1이다
    - 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0이다
- 두 정수 X, Y의 길이(자릿수)는 각각 3 이상 3,000,000 이하이다
    - X, Y는 0으로 시작하지 않는다
- X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환한다

Example:
- Input : X="100", Y="2345"
- Output : "-1"

- Input : X="100", Y="203045"
- Output : "0"

- Input : X="100", Y="123450"
- Output : "10"

- Input : X="12321", Y="42531"
- Output : "321"

- Input : X="5525", Y="1255"
- Output : "552"

Note:
collections의 Counter를 사용하여 각 정수에 나타나는 숫자들의 개수를 카운트
가장 큰 정수를 만들기 위해서는 큰 수가 앞에 나타나야 하므로, 9부터 0까지 확인하며 공통으로 나타나는 횟수(min)만큼 문자열에 더한다

"""

from collections import Counter

def solution(X, Y):
    answer = ""
    Xcount, Ycount = Counter(X), Counter(Y)

    for i in range(9, -1, -1):
        i = str(i)
        common = min(Xcount[i], Ycount[i])
        answer += i * common

    if not answer:
        answer = "-1"
    return answer if answer[0] != "0" else "0"