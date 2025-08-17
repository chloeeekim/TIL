"""

주사위 고르기 : https://school.programmers.co.kr/learn/courses/30/lessons/258709

n개의 주사위가 주어지고, A와 B가 각각 n/2개의 주사위를 가져가서 승부를 할 때, A가 승리할 확률이 가장 높아지도록 주사위를 가져가는 방법을 구하는 문제
- 각 주사위는 1 ~ n의 번호를 가지고 있으며, 주사위에 쓰인 수의 구성은 모두 다르다
- 각각 가져간 주사위를 모두 굴린 뒤, 나온 수들을 모두 합해 점수를 계산하여 큰 쪽이 승리하며, 점수가 같다면 무승부로 처리한다
- dice의 길이는 2 이상 10 이하로 2의 배수로 주어진다
- dice[i]는 i+1번 주사위에 쓰인 6개의 수를 담고 있다
- dice[i]의 원소는 1 이상 100 이하이다
- 승리할 확률이 가장 높아지기 위해 A가 골라야 하는 주사위 번호를 오름차순으로 1차원 정수 배열에 담아 리턴한다

Example:
- Input : dice=[[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
- Output : [1, 4]

- Input : dice=[[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
- Output : [2]

- Input : dice=[[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
- Output : [1, 3]

Note:
itertools의 combinations와 product를 사용하여 선택할 수 있는 주사위의 조합과 선택한 주사위들로 만들 수 있는 합의 경우의 수를 구한다
A가 특정 조합의 주사위를 가져갔을 때의 승리 횟수는 B가 특정 조합의 주사위를 가져갔을 때의 패배 횟수이다 (대칭 관계)
bisect_left를 사용한 이분탐색으로 성능 개선

"""

from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    combs = list(combinations(range(len(dice)), len(dice)//2))
    Asum = []
    for comb in combs:
        dices = [dice[c] for c in comb]
        nums = sorted([sum(i) for i in product(*dices)])
        Asum.append(nums)
    maximum, res, length = 0, [], len(Asum)
    for i in range(length):
        Bsum = Asum[length - i - 1]
        temp = 0
        for a in Asum[i]:
            temp += bisect_left(Bsum, a)
        if maximum < temp:
            maximum = temp
            res = [x+1 for x in combs[i]]
    return res