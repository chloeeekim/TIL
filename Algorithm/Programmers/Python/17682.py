"""

1차 / 다트 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/17682

3번의 기회로 구성된 다트 게임의 결과 문자열이 주어졌을 때, 총점수를 구하는 문제
- 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다
- 점수와 함께 Single(S), Double(D), Triple(T) 영역의 보너스가 존재하며, 각각 점수에서 1제곱, 2제곱, 3제곱으로 계산된다
- 옵션으로 스타상(*)과 아차상(#)이 존재한다
    - 스타상(*)은 해당 점수와 바로 전에 얻은 점수를 각각 2배로 만들며, 첫 번째 기회에서 나온 경우 해당 점수만 2배가 된다
    - 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있으며, 이 경우 중첩된 점수는 4배가 된다
    - 아차상(#)은 해당 점수를 마이너스로 만든다
    - 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있으며, 이 경우 중첩된 점수는 -2배가 된다
    - 스타상(*)과 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다
- 문자열은 "점수|보너스|[옵션]"의 형태가 세 번 반복된다

Example:
- Input : dartResult="1S2D*3T"
- Output : 37

- Input : dartResult="1D2S#10S"
- Output : 9

- Input : dartResult="1D2S0T"
- Output : 3

- Input : dartResult="1S*2T*3S"
- Output : 23

- Input : dartResult="1D#2S*3S"
- Output : 5

- Input : dartResult="1T2D3D#"
- Output : -4

- Input : dartResult="1D2S3T*"
- Output : 59

Note:
점수와 보너스까지 계산 후 scores 리스트에 추가
옵션이 있는 경우 scores 리스트 내의 해당하는 점수 값 변경

"""

def solution(dartResult):
    scores = []
    score, tries = 0, 0
    for ch in dartResult:
        if ch.isdigit():
            score = score * 10 + int(ch)
        elif ch.isalpha():
            if ch == "D":
                score **= 2
            elif ch == "T":
                score **= 3
            scores.append(score)
            tries += 1
            score = 0
        elif ch == "*":
            for i in range(max(tries - 2, 0), tries):
                scores[i] *= 2
        elif ch == "#":
            scores[tries - 1] *= -1
    return sum(scores)