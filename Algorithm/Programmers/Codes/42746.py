"""

가장 큰 수 : https://school.programmers.co.kr/learn/courses/30/lessons/42746

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 구하는 문제
- 0 또는 양의 정수가 담긴 배열 numbers의 길이는 1 이상 100,000 이하이다
    - numbers의 원소는 0 이상 1,000 이하이다
- 정답은 문자열로 리턴한다

Example:
- Input : numbers=[6, 10, 2]
- Output : "6210"

- Input : numbers=[3, 30, 34, 5, 9]
- Output : "9534330"

Note:
숫자를 문자열로 바꾸어 내림차순으로 정렬하여 붙이는 방법
예시에 있는 것처럼 [3, 30, 34]가 있을 때, 정렬 시 [34, 3, 30]이 되어야 하므로
세 번 반복한 결과를 기준으로 정렬하면 원하는 순서로 정렬이 가능하다 (numbers의 원소가 1000 이하이므로 세 번 반복하여 가능)
테스트 케이스 중 numbers가 여러 개의 0으로만 이루어져 있는 경우에 실패하는 듯 하여 결과를 int로 변환 후 다시 str로 바꿔 리턴

"""

def solution(numbers):
    numstrs = list(map(str, numbers))
    numstrs = sorted(numstrs, key=lambda x: x*3, reverse=True)

    return str(int("".join(numstrs)))