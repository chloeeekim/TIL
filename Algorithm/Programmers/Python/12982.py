"""

예산 : https://school.programmers.co.kr/learn/courses/30/lessons/12982

부서별로 신청한 금액과 예산이 주어졌을 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 구하는 문제
- 특정 부서에 예산을 지원하는 경우, 신청한 금액만큼을 모두 지원해 주어야 한다
- 부서별로 신청한 금액이 들어있는 배열 d의 길이는 1 이상 100 이하이다
    - d의 원소는 1 이상 100,000 이하의 자연수이다
- 예산을 나타내는 budget은 1 이상 10,000,000 이하의 자연수이다

Example:
- Input : d=[1,3,2,5,4], budget=9
- Output : 3

- Input : d=[2,2,3,3], budget=10
- Output : 4

Note:
최대한 많은 부서에 지원해야 하므로, 신청 금액이 작은 부서부터 포함하는 방식으로 greedy하게 해결

"""

def solution(d, budget):
    count, tsum = 0, 0
    for price in sorted(d):
        if tsum + price <= budget:
            count += 1
            tsum += price
        else:
            break
    return count