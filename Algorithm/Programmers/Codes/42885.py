"""

구명보트 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

사람들의 몸무게와 구명보트의 무게 제한이 주어졌을 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 구하는 문제
- 구명보트는 최대 2명 밖에 탈 수 없다
- 사람들의 몸무게를 담은 배열 people의 길이는 1 이상 50,000 이하이다
    - 각 사람의 몸무게는 40 이상 240 이하이다
- 구명보트의 무게 제한 limit은 40 이상 240 이하이다
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로, 사람들을 구출할 수 없는 경우는 없다

Example:
- Input : people=[70, 50, 80, 50], limit=100
- Output : 3

- Input : people=[70, 80, 50], limit=100
- Output : 3

Note:
남은 사람 중 몸무게가 가장 많이 나가는 사람을 먼저 태우고, 빈 자리에 몸무게가 가장 적게 나가는 사람을 태울 수 있는지 확인

"""

def solution(people, limit):
    answer = 0
    speople = sorted(people, reverse=True)
    left, right = 0, len(people) - 1

    while left <= right:
        if speople[left] + speople[right] <= limit:
            right -= 1
        left += 1
        answer += 1

    return answer
