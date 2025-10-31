"""

방금그곡 : https://school.programmers.co.kr/learn/courses/30/lessons/17683

들었던 멜로디와 라디오에서 방송된 곡의 정보가 주어졌을 때, 찾으려는 음악의 제목을 구하는 문제
- 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다
- 들었던(기억한) 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다
- 각 음은 1분에 1개씩 재생된다
    - 음악은 반드시 처음부터 재생된다
    - 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다
    - 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다
- 음악이 00:00을 넘겨서까지 재생되는 일은 없다
- 조건이 일치하는 음악이 여러 개일 경우, 재생된 시간이 제일 긴 음악 제목을 리턴한다
    - 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 리턴한다
- 조건에 일치하는 음악이 없을 경우 "(None)"을 리턴한다
- 기억한 멜로디를 담은 문자열 m의 음은 1개 이상 1439개 이하이다
- 방속된 곡의 정보를 담은 배열 musicinfos는 100개 이하의 곡 정보를 담고 있다
    - musicinfos의 원소는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다
    - 음악의 시작 시각과 끝난 시각은 HH:MM 형식으로, 24시간 기준이다
    - 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다
    - 악보 정보의 음은 1개 이상 1439개 이하이다

Example:
- Input : m="ABCDEFG", musicinfos=["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
- Output : "HELLO"

- Input : m="CC#BCC#BCC#BCC#B", musicinfos=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
- Output : "FOO"

- Input : m="ABC", musicinfos=["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
- Output : "WORLD"

Note:
문자열로 비교할 경우, m이 "ABC"이고 악보 정보가 "ABC#"일 때 일치한다고 판단하는 문제가 발생
따라서 re.findall(r"[A-G]#?", m)과 같이 각각의 음을 구분하여 리스트 형태로 비교

"""

import re

def calcDuration(start, end):
    start, end = list(map(int, start.split(":"))), list(map(int, end.split(":")))
    return end[0] * 60 + end[1] - start[0] * 60 - start[1]

def isSublist(m, notes):
    lm, ln = len(m), len(notes)
    if lm > ln:
        return False
    for i in range(ln - lm + 1):
        if notes[i:i + lm] == m:
            return True
    return False

def solution(m, musicinfos):
    answer = ""
    playtime = 0
    m = re.findall(r"[A-G]#?", m)
    for info in musicinfos:
        start, end, title, notes = info.split(",")
        duration = calcDuration(start, end)
        notes = re.findall(r"[A-G]#?", notes)
        notes = (notes * (duration // len(notes) + 1))[:duration]

        if isSublist(m, notes) and playtime < duration:
            answer = title
            playtime = duration

    return answer if answer else "(None)"