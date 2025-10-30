"""

압축 : https://school.programmers.co.kr/learn/courses/30/lessons/17684

문자열이 주어졌을 때, LZW(Lempel–Ziv–Welch) 압축을 진행한 후의 사전 색인 번호를 구하는 문제
- LZW 압축은 다음과 같이 진행된다
    - 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다
    - 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다
    - 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다
    - 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다
    - 5. 2단계로 돌아간다
    - 6. 마지막으로 처리되지 않은 글자에 해당하는 색인 번호를 출력한다
- 문자열 msg는 영문 대문자로만 이루어져 있으며, 길이는 1 이상 1,000 이하이다

Example:
- Input : msg="KAKAO"
- Output : 	[11, 1, 27, 15]

- Input : msg="TOBEORNOTTOBEORTOBEORNOT"
- Output : [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]

- Input : msg="ABABABABABABABAB"
- Output : [1, 2, 27, 29, 28, 31, 30]

Note:
주어진 압축 과정대로 구현
dict를 초기화할 때 간편하게 하기 위해 chr(ord('A') + i)와 같이 ascii 값을 사용

"""

def solution(msg):
    answer = []
    dictionary = {chr(ord('A') + i): i+1 for i in range(26)}
    dlen = 26

    idx = 0
    temp = ""
    while idx < len(msg):
        temp += msg[idx]
        idx += 1
        if temp not in dictionary:
            answer.append(dictionary[temp[:-1]])
            dlen += 1
            dictionary[temp] = dlen
            temp = temp[-1]
    answer.append(dictionary[temp])

    return answer