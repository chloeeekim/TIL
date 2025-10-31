"""

2개 이하로 다른 비트 : https://school.programmers.co.kr/learn/courses/30/lessons/77885

정수 배열이 주어졌을 때, 각 정수에 대해서 f(x)를 구하는 문제
- 양의 정수 x에 대한 함수 f(x)는 다음과 같이 정의한다
    - x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
- numbers의 길이는 1 이상 100,000 이하이며, numbers의 원소는 0 이상 10^15 이하이다

Example:
- Input : numbers=[2, 7]
- Output : [3, 11]
- 2의 경우 0010이므로, 0011인 3이 1개의 비트가 다르면서 가장 작은 수이다
- 7의 경우 0111이므로, 1011인 11이 2개의 비트가 다르면서 가장 작은 수이다

Note:
주어진 정수가 짝수라면 가장 오른쪽 비트가 무조건 0이고, 이 경우 마지막 비트를 1로 변경하는 경우가 답이 된다
주어진 정수가 홀수라면 가장 오른쪽에 있는 0 비트를 1로 변경하고, 그 오른쪽 비트를 0으로 변경하는 경우가 답이 된다

"""

def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bits = list('0' + bin(number)[2:])
            idx = ''.join(bits).rfind('0')
            bits[idx] = '1'
            bits[idx+1] = '0'
            answer.append(int(''.join(bits), 2))

    return answer