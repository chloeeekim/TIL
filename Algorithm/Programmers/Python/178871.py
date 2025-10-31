"""

달리기 경주 : https://school.programmers.co.kr/learn/courses/30/lessons/178871

선수들의 순서와 추월한 선수의 이름 목록이 주어졌을 때, 최종 결과를 구하는 문제
- 선수가 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름이 불린다
- 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players의 길이는 5 이상 50,000 이하이다
    - players[i]는 i번째 선수의 이름을 의미한다
    - players의 원소는 알파벳 소문자로만 이루어져 있다
    - players에는 중복된 값이 들어있지 않다
    - players[i]의 길이는 3 이상 10 이하이다
- 추월한 선수의 이름이 담긴 문자열 배열 callings의 길이는 2 이상 1,000,000 이하이다
    - callings는 players의 원소들로만 이루어져 있다
    - 경주 진행 중 1등인 선수의 이름은 불리지 않는다

Example:
- Input : players=["mumu", "soe", "poe", "kai", "mine"], callings=["kai", "kai", "mine", "mine"]
- Output : ["mumu", "kai", "mine", "soe", "poe"]

Note:
이름을 불린 선수는 바로 앞에 위치한 선수와 변경
index 함수 등으로 위치를 찾는 것은 비효율적이므로 dict를 사용하여 위치 저장

"""

def solution(players, callings):
    pdict = {name: idx for idx, name in enumerate(players)}

    for calling in callings:
        idx = pdict[calling]
        pdict[calling] -= 1
        pdict[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players