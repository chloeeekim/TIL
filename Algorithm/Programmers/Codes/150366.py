"""

표 병합 : https://school.programmers.co.kr/learn/courses/30/lessons/150366

50x50 크기의 표와 명령어들이 주어졌을 때, PRINT 명령어에 대한 실행 결과를 구하는 문제
- UPDATE r c value
    - (r, c) 위치의 셀의 값을 value로 바꾼다
- UPDATE value1 value2
    - value1을 값으로 가지고 있는 모든 셀을 value2로 바꾼다
- MERGE r1 c1 r2 c2
    - (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합한다
    - 두 위치의 셀이 같은 셀일 경우 무시한다
    - 두 셀이 인접하지 않은 경우, 사이에 위치한 셀들은 영향을 받지 않는다
    - 두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가지게 된다
    - 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀의 값을 가진다
    - 이후 (r1, c1)과 (r2, c2) 중 어느 위치를 선택하더라도 병합된 셀로 접근한다
- UNMERGE r c
    - (r, c) 위치의 셀의 모든 병합을 해제한다
    - 선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기의 상태로 돌아간다
    - 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가진다
- PRINT r c
    - (r, c) 위치의 셀의 값을 출력한다
    - 선택한 셀이 비어있을 경우 "EMPTY"를 출력한다
- 주어지는 r, c는 1 이상 50 이하의 정수이다
- 주어지는 value는 알파벳 소문자와 숫자로 구성된 길이 1 이상 10 이하의 문자열이다
- commands는 1개 이상의 PRINT 명령어를 포함한다

Example:
- Input : commands=["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
- Output : ["EMPTY", "group"]

- Input : commands=["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
- Output : ["d", "EMPTY"]

Note:
각 명령어들을 별도의 함수로 구분하여 구현
각 셀(r, c)는 r * 50 + c의 값으로 초기화하며, 해당 값으로 group을 구분
gvalues dict에 group i의 value를 저장

"""

def solution(commands):
    group = {}
    gvalues = {i: "EMPTY" for i in range(50 * 50)}
    result = []

    for i in range(50):
        for j in range(50):
            group[(i, j)] = (i * 50) + j

    def update1(r, c, value):
        group_num = group[(r, c)]
        gvalues[group_num] = value

    def update2(value1, value2):
        for key, value in gvalues.items():
            if value == value1:
                gvalues[key] = value2

    def merge(r1, c1, r2, c2):
        group1 = group[(r1, c1)]
        group2 = group[(r2, c2)]

        gvalues[group1] = gvalues[group2] if gvalues[group1] == "EMPTY" else gvalues[group1]

        for key, value in group.items():
            if value == group2:
                group[key] = group1

    def unmerge(r, c):
        group_num = group[(r, c)]
        value = gvalues[group_num]

        for (i, j), gnum in group.items():
            if gnum == group_num:
                group[(i, j)] = i * 50 + j
                gvalues[i * 50 + j] = "EMPTY"
        gvalues[r * 50 + c] = value

    def pprint(r, c):
        result.append(gvalues[group[(r, c)]])

    for comm in commands:
        control, *values = comm.split()

        if control == "UPDATE":
            if len(values) == 3:
                update1(int(values[0])-1, int(values[1])-1, values[2])
            elif len(values) == 2:
                update2(values[0], values[1])
        elif control == "MERGE":
            merge(int(values[0])-1, int(values[1])-1, int(values[2])-1, int(values[3])-1)
        elif control == "UNMERGE":
            unmerge(int(values[0])-1, int(values[1])-1)
        elif control == "PRINT":
            pprint(int(values[0])-1, int(values[1])-1)

    return result