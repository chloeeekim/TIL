"""

교점에 별 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/87377

Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 직선의 교점 중 정수 좌표에 별을 그리는 문제
- 별이 그려진 부분은 '*', 빈 공간(격자선이 교차하는 지점)은 '.'으로 표현한다
- 모든 별을 포함하는 최소한의 사각형으로 나타낸다
- line의 행 길이는 2 이상 1,000 이하인 자연수이다
    - line의 원소는 [A, B, C]의 형태이다
    - A, B, C는 -100,000 이상 100,000 이하인 정수이다
    - 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않는다
    - A = 0 이면서 B = 0 인 경우는 주어지지 않는다
- 정답은 1,000 * 1,000 크기 이내에서 표현된다
- 별이 한 개 이상 그려지는 입력만 주어진다
- 참고) Ax + By + E = 0과 Cx + Dy + F = 0 이라는 두 직선의 교점이 유일하게 존재할 경우, 그 교점은 다음과 같다
    - x = (BF - ED) / (AD - BC)
    - y = (EC - AF) / (AD - BC)
    - 또, AD - BC = 0인 경우, 두 직선은 평행 또는 일치한다

Example:
- Input : price=3, money=20, count=4
- Output : 10

Note:
참고 사항에 따라 직선들이 교차하는 지점을 구하고, 정수 좌표인 경우에만 points에 추가
points는 set으로 하여 중복 제거
최소 사각형을 그려야 하므로, 주어진 points들의 x, y 좌표의 min, max를 범위로 한다

"""

def solution(line):
    points = set()
    for i in range(len(line)):
        A, B, E = line[i]
        for j in range(i+1, len(line)):
            C, D, F = line[j]
            if A * D - B * C == 0:
                continue
            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)
            if x.is_integer() and y.is_integer():
                points.add((int(x), int(y)))

    x_list, y_list = zip(*points)
    x_range = [min(x_list), max(x_list)]
    y_range = [min(y_list), max(y_list)]

    res = []
    for i in range(y_range[1], y_range[0] - 1, -1):
        row = ""
        for j in range(x_range[0], x_range[1] + 1):
            if (j, i) in points:
                row += "*"
            else:
                row += "."
        res.append(row)

    return res