"""

주식가격 : https://school.programmers.co.kr/learn/courses/30/lessons/42584

초 단위로 기록된 주식가격이 주어졌을 때, 가격이 떨어지지 않은 기간은 몇 초인지 구하는 문제
- 주식가격이 담긴 배열 prices의 길이는 2 이상 100,000 이하이다
- prices의 각 가격은 1 이상 10,000 이하인 자연수이다

Example:
- Input : prices=[1, 2, 3, 2, 3]
- Output : [4, 3, 1, 1, 0]

Note:
stack을 사용하여 해결
인덱스가 시간을 의미하므로, 스택에 (인덱스, 가격) 형태로 추가하여 몇 초간 유지되었는지 확인
마지막까지 스택에 남아있는 경우에는 가격이 떨어지지 않은 것이므로 최종 시간과 비교하여 계산

"""

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            sidx, sp = stack.pop()
            answer[sidx] = idx - sidx
        stack.append((idx, price))

    for idx, _ in stack:
        answer[idx] = len(prices) - idx - 1

    return answer