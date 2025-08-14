"""

[PCCE 기출문제] 10번 / 공원 : https://school.programmers.co.kr/learn/courses/30/lessons/340198

공원의 빈 공간에 놓을 수 있는 가장 큰 돗자리를 구하는 문제
- park[i][j]에 돗자리를 깐 사람이 없다면 "-1", 사람이 있다면 알파벳 한 글자로 된 값을 갖는다
- 돗자리는 정사각형 모양이며, 보유하고 있는 돗자리의 크기는 mats 리스트로 주어진다

Example:
- Input : mats=[5,3,2], park=
[
    ["A", "A", "-1", "B", "B", "B", "B", "-1"],
    ["A", "A", "-1", "B", "B", "B", "B", "-1"],
    ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
    ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
    ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
    ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]
]
- Output : 3

Note:
set을 사용하여 범위 내에 "-1"만 있다면 놓을 수 있는 것으로 판단

"""

def solution(mats, park):
    answer = 0
    mats = sorted(mats, reverse=True)
    M, N = len(park), len(park[0])
    for size in mats:
        for i in range(M-size+1):
            for j in range(N-size+1):
                sub = set()
                for k in range(i, i+size):
                    for l in range(j, j+size):
                        sub.add(park[k][l])
                if (sub == {"-1"}):
                    return size
    return -1