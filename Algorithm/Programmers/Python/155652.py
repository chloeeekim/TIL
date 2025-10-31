"""

둘만의 암호 : https://school.programmers.co.kr/learn/courses/30/lessons/155652

두 문자열 s와 skip, 자연수 index가 주어졌을 때, 특정 규칙에 따라 문자열을 만드는 문제
- 문자열은 다음과 같은 규칙에 따라 생성한다
    - 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 변경한다
    - index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다
    - skip에 있는 알파벳은 제외하고 건너뛴다
- s의 길이는 5 이상 50 이하이며, skip의 길이는 1 이상 10 이하이다
    - s와 skip은 알파벳 소문자로만 이루어져 있다
    - skip에 포함되는 알파벳은 s에 포함되지 않는다
- index는 1 이상 20 이하의 정수이다

Example:
- Input : cards1=["i", "drink", "water"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"]
- Output : "Yes"

- Input : cards1=["i", "water", "drink"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"]
- Output : "No"

Note:
skip을 제외한 나머지 알파벳들을 모은 리스트(alpha)와 해당 리스트의 위치 정보를 담은 dict(idxs)를 생성하여 해결

"""

def solution(s, skip, index):
    idxs = {}
    alpha = []

    idx = 0
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in skip:
            idxs[chr(i)] = idx
            alpha.append(chr(i))
            idx += 1

    res = ""
    length = len(alpha)
    for ch in s:
        change = (idxs[ch] + index) % length
        res += alpha[change]

    return res