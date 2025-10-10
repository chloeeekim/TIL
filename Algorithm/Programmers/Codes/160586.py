"""

대충 만든 자판 : https://school.programmers.co.kr/learn/courses/30/lessons/160586

자판의 특정 키를 눌렀을 때 입력되는 문자들의 정보가 주어졌을 때, 특정 문자열을 작성할 때 최소 몇 번의 키를 눌러야 작성할 수 있는지 구하는 문제
- 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면, 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 입력된다
- 주어진 휴대폰 자판은 다음과 같은 특징을 지닌다
    - 특정 키를 눌렀을 때 입력되는 문자들은 무작위로 배열되어 있다
    - 같은 문자가 자판 전체에 여러 번 할당될 수 있다
    - 키 하나에 같은 문자가 여러 번 할당될 수 있다
    - 특정 문자가 아예 할당되지 않을 수 있다 (즉, 어떤 문자열은 작성할 수 없다)
- 자판에 할당된 문자들이 순서대로 담긴 문자열 배열 keymap의 길이는 1 이상 100 이하이다
    - keymap의 원소의 길이는 1 이상 100 이하이다
    - keymap[i]는 i+1번 키를 눌렀을 때 순서대로 바뀌는 문자를 의미한다
    - keymap의 원소의 길이는 서로 다를 수 있다
    - keymap의 원소는 알파벳 대문자로만 이루어져 있다
- 입력하려는 문자열들이 담긴 문자열 배열 targets의 길이는 1 이상 100 이하이다
    - targets의 원소의 길이는 1 이상 100 이하이다
    - targets의 원소는 알파벳 대문자로만 이루어져 있다
- 각 문자열을 작성하기 위해 필요한 최소한의 입력 횟수를 순서대로 배열에 담아 리턴한다
    - 단, 문자열을 작성할 수 없는 경우 -1을 리턴한다

Example:
- Input : keymap=["ABACD", "BCEFD"], targets=["ABCD","AABB"]
- Output : [9, 4]

- Input : keymap=["AA"], targets=["B"]
- Output : [-1]

- Input : keymap=["AGZ", "BSSS"], targets=["ASA","BGZ"]
- Output : [4, 6]

Note:
defaultdict를 사용하여 각 문자별 입력에 필요한 최소 횟수를 저장
문자열을 입력하는 데 필요한 최소 입력 횟수는 각 문자의 최소 입력 횟수의 합
만약 dict에 문자가 없다면 입력할 수 없으므로 -1

"""

from collections import defaultdict

def solution(keymap, targets):
    key_counts = defaultdict(lambda: 999999)
    for keys in keymap:
        for i in range(len(keys)):
            key_counts[keys[i]] = min(key_counts[keys[i]], i + 1)

    answer = []
    for target in targets:
        temp = 0
        for ch in target:
            if ch in key_counts:
                temp += key_counts[ch]
            else:
                temp = -1
                break
        answer.append(temp)

    return answer