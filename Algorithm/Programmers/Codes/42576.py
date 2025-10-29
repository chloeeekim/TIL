"""

완주하지 못한 선수 : https://school.programmers.co.kr/learn/courses/30/lessons/42576

선수들의 이름과 완주한 선수들의 이름이 주어졌을 때, 완주하지 못한 선수의 이름을 구하는 문제
- 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였다
- 마라톤 경기에 참여한 선수는 1명 이상 100,000명 이하이다
- 완주한 선수들의 이름이 담긴 배열 completion의 길이는 마라톤에 참여한 선수들의 이름이 담긴 배열 participant의 길이보다 1 작다
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있다
- 참가자 중에는 동명이인이 있을 수 있다

Example:
- Input : participant=["leo", "kiki", "eden"], completion=["eden", "kiki"]
- Output : "leo"

- Input : participant=["marina", "josipa", "nikola", "vinko", "filipa"], completion=["josipa", "filipa", "marina", "nikola"]
- Output : "vinko"

- Input : participant=["mislav", "stanko", "mislav", "ana"], completion=["stanko", "ana", "mislav"]
- Output : "mislav"
- "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없으므로 한 명은 완주하지 못한 것으로 판단

Note:
참가자의 이름이 중복될 수 있으므로 Counter를 사용하여 특정 이름이 몇 번 등장했는지를 카운트
participant에 포함된 횟수와 completion에 포함된 횟수가 다르다면 해당 이름을 가진 선수가 한 명 완주하지 못한 것으로 판단

"""

from collections import Counter

def solution(participant, completion):
    pcounter = Counter(participant)
    ccounter = Counter(completion)

    for name, count in pcounter.items():
        if ccounter[name] != count:
            return name
    return ""