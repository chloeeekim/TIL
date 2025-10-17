"""

귤 고르기 : https://school.programmers.co.kr/learn/courses/30/lessons/138476

한 상자에 담으려는 귤의 개수와 귤들의 크기가 주어졌을 때, 크기가 서로 다른 종류의 수의 최솟값을 구하는 문제
- 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine은 다음과 같다
    - 1 <= k <= tangerine의 길이 <= 100,000
    - tangerine의 원소는 1 이상 10,000,000 이하이다

Example:
- Input : k=6, tangerine=[1, 3, 2, 5, 4, 5, 2, 3]
- Output : 3

- Input : k=4, tangerine=[1, 3, 2, 5, 4, 5, 2, 3]
- Output : 2

- Input : k=2, tangerine=[1, 1, 1, 1, 2, 2, 2, 3]
- Output : 1

Note:
Counter를 사용하여 동일한 무게를 지닌 귤들의 개수를 카운트
k가 1이라면 어떤 귤을 담더라도 크기가 모두 같으므로, 1을 리턴
counter를 귤의 개수에 대해 내림차순으로 정렬하여 많은 것부터 더해가는 방식으로, greedy하게 해결

"""

from collections import Counter

def solution(k, tangerine):
    if k == 1:
        return 1

    counter = Counter(tangerine)
    scounter = sorted(counter.items(), key=lambda x: -x[1])

    answer, total = 0, 0
    for key, value in scounter:
        total += value
        answer += 1

        if total >= k:
            break

    return answer