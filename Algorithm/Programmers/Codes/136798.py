"""

기사단원의 무기 : https://school.programmers.co.kr/learn/courses/30/lessons/136798

기사들의 수와 공격력의 제한 수치 등이 주어졌을 때, 무기를 모두 만들기 위해 필요한 철의 무게를 구하는 문제
- 기사단의 각 기사에게는 1번부터 number까지의 번호가 지정된다
- 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매한다
    - 단, 공격력의 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 경우, 협약에 정해진 공격력을 가지는 무기를 구매해야 한다
- 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요하다
- 기사단원의 수 number는 1 이상 10,000 이하의 정수이다
- 공격력의 제한수치 limit은 2 이상 100 이하의 정수이다
- 제한수치를 초과한 기사가 사용할 무기의 공격력 power는 1 이상 limit 이하의 정수이다

Example:
- Input : number=5, limit=3, power=2
- Output : 10
- 1부터 5까지의 약수의 개수는 순서대로 [1, 2, 2, 3, 2]이므로 모두 limit을 초과하지 않는다

- Input : number=10, limit=3, power=2
- Output : 21
- 1부터 10까지의 약수의 개수는 순서대로 [1, 2, 2, 3, 2, 4, 2, 4, 3, 4]이므로 6, 8, 10번 기사는 공격력이 2인 무기를 구매해야 한다

Note:
약수의 개수를 구하는 getFactor 메서드를 구현
약수의 개수가 limit 이하인 경우 그대로 답에 더하고, 초과하는 경우 power를 더한다

"""

import math

def getFactor(num):
    count = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count.update([i, num // i])
    return len(count)

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        factor = getFactor(i)
        answer += factor if factor <= limit else power
    return answer