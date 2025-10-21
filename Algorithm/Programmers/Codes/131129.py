"""

카운트 다운 : https://school.programmers.co.kr/learn/courses/30/lessons/131129

목표 점수가 주어졌을 때, 최선의 경우 던질 다트 수와 그 때의 싱글 또는 불을 맞춘 횟수의 합을 구하는 문제
- 다트 게임의 룰은 다음과 같다
    - 게임이 시작되면 무작위로 점수가 정해진다
    - 다트를 던지면서 점수를 깎아서 정확히 0점으로 만들어야 한다
    - 남은 점수보다 큰 점수로 득점하면 버스트가 되며 실격한다
- 다트 과녁에는 1부터 20까지의 수가 하나씩 있고, 각 수마다 "싱글", "더블", "트리플"이 있다
    - 싱글을 맞히면 해당 수만큼, 더블을 맞히면 해당 수의 두 배만큼, 트리플을 맞히면 해당 수의 세 배만큼 점수를 얻는다
    - 가운데에는 "불"과 "아우터 불"이 있는데, 본 게임에서는 구분 없이 50점을 얻는다
- 대회에서 이기는 방법은 다음과 같다
    - 두 선수가 교대로 한 번씩 던지는 라운드 방식에서, 가장 먼저 0점을 만든 선수가 승리한다
    - 만약 두 선수가 같은 라운드에 0점을 만들면 두 선수 중 "싱글" 또는 "불"을 더 많이 던진 선수가 승리한다
    - 그마저도 같다면 선공인 선수가 승리한다
    - 따라서 최소한의 다트로 0점을 만드는 것이 가장 중요하고, 그 방법이 여러 가지가 있다면 싱글 또는 불을 최대한 많이 던지는 방법을 선택해야 한다
- 목표 점수 target은 1 이상 100,000 이하의 정수이다

Example:
- Input : target=21
- Output : [1, 0]
- 7 트리플로 한 번에 21점을 만들 수 있다

- Input : target=58
- Output : [2, 2]
- 불 (50점) + 8 싱글로 두 번만에 58점을 만들 수 있다

Note:
issorb dict에는 다트를 던져서 나올 수 있는 모든 점수에 대해 싱글이거나 불로 가능한 점수라면 1을, 아니라면 0을 저장
dp 방식으로, 각 점수별로 최선의 경우를 구하여 target까지의 점수를 만든다

"""

def solution(target):
    issorb = {}
    for i in range(1, 21):
        issorb[i * 2] = 0
        issorb[i * 3] = 0
    for i in range(1, 21):
        issorb[i] = 1
    issorb[50] = 1

    dmin = [999999] * 100001
    sorbmax = [0] * 100001

    for i, sorb in issorb.items():
        dmin[i] = 1
        sorbmax[i] = sorb

    for t in range(1, target + 1):
        if dmin[t] != 999999:
            continue

        tdmin, tsbmax = 999999, 0
        for score, sorb in issorb.items():
            temp = t - score
            if temp < 0:
                continue

            if (dmin[temp] + 1 < tdmin) or (dmin[temp] + 1 == tdmin and sorbmax[temp] + sorb > tsbmax):
                tdmin = dmin[temp] + 1
                tsbmax = sorbmax[temp] + sorb

        dmin[t] = tdmin
        sorbmax[t] = tsbmax

    return [dmin[target], sorbmax[target]]
