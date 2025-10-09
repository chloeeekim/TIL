"""

방문 길이 : https://school.programmers.co.kr/learn/courses/30/lessons/49994

명령어들이 주어졌을 때, 캐릭터가 처음 걸어본 길의 길이를 구하는 문제
- 명령어는 다음과 같다
    - U: 위쪽으로 한 칸 이동
    - D: 아래쪽으로 한 칸 이동
    - R: 오른쪽으로 한 칸 이동
    - L: 왼쪽으로 한 칸 이동
- 캐릭터는 좌표평면의 (0, 0) 위치에서 시작한다
- 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있다
    - 좌표평면의 경계를 넘어가는 명령어는 무시한다
- dirs는 문자열로 주어지며, 'U', 'D', 'R', 'L' 이외의 문자는 주어지지 않는다
- dirs의 길이는 500 이하의 자연수이다

Example:
- Input : dirs="ULURRDLLU"
- Output : 7

- Input : dirs="LULLLLLLU"
- Output : 7

Note:
set을 사용하여 중복 제거
시작 좌표와 도착 좌표를 set에 추가하는데, 방향에 상관없이 계산하기 위해 반대로도 추가 후 결과는 절반으로 나누는 방식

"""

def solution(dirs):
    visited = set()
    x, y = 0, 0
    directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    for d in dirs:
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(((x, y), (nx, ny)))
            visited.add(((nx, ny), (x, y)))
            x, y = nx, ny
    return len(visited) // 2