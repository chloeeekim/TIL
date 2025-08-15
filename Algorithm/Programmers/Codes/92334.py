"""

신고 결과 받기 : https://school.programmers.co.kr/learn/courses/30/lessons/92334

유저간의 신고 내용과 정지 기준이 되는 신고 횟수가 주어졌을 때, 각 유저별로 처리 결과 메일을 받은 횟수를 구하는 문제
- 각 유저는 한 번에 한 명의 유저를 신고할 수 있다
- 신고 횟수에 제한은 없으므로, 서로 다른 유저를 계속 신고할 수 있다
- 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리된다
- k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송한다
- id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있고, 중복은 없다
- report의 원소는 "이용자id 신고한id" 형태의 문자열이며, 각 id는 공백으로 구분된다
- 자기 자신을 신고하는 경우는 존재하지 않는다

Example:
- Input : id_list=["muzi", "frodo", "apeach", "neo"], report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], k=2
- Output : [2, 1, 1, 0]

- Input : id_list=["con", "ryan"], report=["ryan con", "ryan con", "ryan con", "ryan con"], k=3
- Output : [0, 0]
- ryan이 con을 4번 신고했으나 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리하므로 3번 이상 신고당한 유저는 없다

Note:
set을 사용하여 중복을 제거

"""

def solution(id_list, report, k):
    result = [0] * len(id_list)
    rep = {i: 0 for i in id_list}

    for r in set(report):
        rep[r.split()[1]] += 1

    for r in set(report):
        if rep[r.split()[1]] >= k:
            result[id_list.index(r.split()[0])] += 1

    return result