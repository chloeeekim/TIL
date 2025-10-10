"""

가장 가까운 같은 글자 : https://school.programmers.co.kr/learn/courses/30/lessons/142086

문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서 자신과 가장 가까운 곳에 있는 같은 글자의 위치를 구하는 문제
- 다음과 같이 진행한다
    - 처음 등장한 글자의 경우, 자신의 앞에 같은 글자가 없으므로 -1로 표현한다
    - 앞에 같은 글자가 있는 경우, 몇 칸 앞에 있는지로 표현한다
- s의 길이는 1 이상 10,000 이하이다
    - s는 영어 소문자로만 이루어져 있다

Example:
- Input : s="banana"
- Output : [-1, -1, -1, 2, 2, 2]

- Input : s="foobar"
- Output : [-1, -1, 1, -1, -1, -1]

Note:
등장한 글자의 마지막 인덱스를 dict에 저장
같은 글자가 등장하면 차이를 계산하고, 현재 인덱스로 업데이트

"""

def solution(s):
    answer = []

    seen = {}
    for i in range(len(s)):
        ch = s[i]
        if ch in seen:
            answer.append(i - seen[ch])
        else:
            answer.append(-1)
        seen[ch] = i

    return answer