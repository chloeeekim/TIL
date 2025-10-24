"""

베스트앨범 : https://school.programmers.co.kr/learn/courses/30/lessons/42579

노래의 장르와 재생 횟수가 주어졌을 때, 특정 기준으로 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 구하는 문제
- 장르별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범에 수록한다
- 노래를 수록하는 기준은 다음과 같다
    - 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다
    - 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다
    - 3. 장르 내에서 재생 횟수가 같은 노래들 중에서는 고유 번호가 낮은 노래를 먼저 수록한다
- 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays는 다음과 같다
    - genres[i]는 고유번호가 i인 노래의 장르이다
    - plays[i]는 고유번호가 i인 노래가 재생된 횟수이다
    - genres와 plays의 길이는 같으며, 길이는 1 이상 10,000 이하이다
    - 장르 종류는 100개 미만이다
    - 모든 장르는 재생된 횟수가 다르다
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택한다

Example:
- Input : genres=["classic", "pop", "classic", "classic", "pop"], plays=[500, 600, 150, 800, 2500]
- Output : [4, 1, 3, 0]

Note:
장르의 전체 재생 횟수를 계산하는 total dict와 각 장르에 속한 노래별 재생 횟수를 저장하는 songs dict를 두고
전체 재생 횟수가 많은 장르부터 해당 장르의 노래별 재생 횟수를 기준에 맞게 정렬하여 최대 2개씩 선택

"""

from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    songs = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        total[g] += p
        songs[g].append([p, i])

    answer = []
    for g, p in sorted(total.items(), key=lambda x: -x[1]):
        temp = sorted(songs[g], key=lambda x: (-x[0], x[1]))[:2]
        answer.extend(idx for _, idx in temp)

    return answer