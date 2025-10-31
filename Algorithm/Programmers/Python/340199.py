"""

[PCCE 기출문제] 9번 / 지폐 접기 : https://school.programmers.co.kr/learn/courses/30/lessons/340199

지폐와 지갑의 가로, 세로 크기가 주어졌을 때, 지폐를 최소 몇 번 접어야 지갑에 넣을 수 있는지 구하는 문제
- 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접는다
- 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버린다
- 접힌 지폐는 그대로 혹은 90도 돌려서 지갑에 넣을 수 있다

Example:
- Input : wallet=[30,15], bill=[26,17]
- Output : 1

- Input : wallet=[50,50], bill=[100,241]
- Output : 4
- [100,241] -> [100,120] -> [100,60] -> [50,60] -> [50,30]

Note:
문제 지문에 주어진 과정을 그대로 구현

"""

def solution(wallet, bill):
    answer = 0
    while (min(bill) > min(wallet) or max(bill) > max(wallet)):
        if (bill[0] > bill[1]):
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer