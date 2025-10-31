"""

바탕화면 정리 : https://school.programmers.co.kr/learn/courses/30/lessons/161990

컴퓨터 바탕화면의 상태가 주어졌을 때, 모든 파일을 선택해서 한 번에 지울 수 있는 최소한의 이동거리를 갖는 드래그의 시작점과 끝점을 구하는 문제
- 드래그로 파일을 선택하는 방법은 다음과 같다
    - 바탕화면의 격자점 S(lux, luy)를 클릭한 상태로 격자점 E(rdx, rdy)로 이동한다.
        - 이때, "점 S에서 점 E로 드래그한다"고 표현하고, 점 S와 점 E를 각각 드래그의 시작점, 끝점이라고 표현한다
    - 점 S(lux, luy)에서 점 E(rdx, rdy)로 드래그를 할 때, 드래그한 거리는 |rdx - lux| + |rdy - luy|로 정의한다
    - 점 S에서 점 E로 드래그를 하면 바탕화면에서 두 격자점을 각각 왼쪽 위, 오른쪽 아래로 하는 직사각형 내부에 있는 모든 파일이 선택된다
- 컴퓨터 바탕화면의 상태를 나타내는 문자열 배열 wallpaper의 길이는 1 이상 50 이하이다
    - wallpaper[i]의 길이는 1 이상 50 이하이다
    - wallpaper의 모든 원소의 길이는 동일하다
    - wallpaper[i][j]는 바탕화면에서 i+1행 j+1열에 해당하는 칸의 상태를 나타낸다
    - wallpaper[i][j]는 "#" 또는 "."의 값만 가진다
        - "#"는 파일이 있는 칸을, "."는 빈칸을 의미한다
- 드래그의 시작점(lux, luy)과 끝점(rdx, rdy)을 정수 배열([lux, luy, rdx, rdy])에 넣어 리턴한다
    - lux < rdx, luy < rdy를 만족해야 한다

Example:
- Input : wallpaper=[".#...", "..#..", "...#."]
- Output : [0, 1, 3, 4]

- Input : wallpaper=["..........", ".....#....", "......##..", "...##.....", "....#....."]
- Output : [1, 3, 5, 8]

- Input : wallpaper=[".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
- Output : [0, 0, 7, 9]

- Input : wallpaper=["..", "#."]
- Output : [1, 0, 2, 1]

Note:
모든 파일의 좌상단 좌표에서 최소, 최대를 계산
좌상단 좌표 기준이므로 시작점은 최솟값을 그대로 사용하고, 최댓값은 1을 더한다

"""

def solution(wallpaper):
    files = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                files.append((i, j))

    x_list, y_list = zip(*files)
    x_range = [min(x_list), max(x_list)]
    y_range = [min(y_list), max(y_list)]

    return [x_range[0], y_range[0], x_range[1] + 1, y_range[1] + 1]