"""

최소직사각형 : https://school.programmers.co.kr/learn/courses/30/lessons/86491

명함들의 크기가 주어졌을 때, 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 구하는 문제
- 명함은 회전시켜 수납할 수 있다
- 모든 명함의 크기를 나타내는 2차원 배열 sizes의 길이는 1 이상 10,000 이하이다
    - sizes의 원소는 [w, h] 형식으로, w는 명함의 가로 길이를, h는 명함의 세로 길이를 나타낸다
    - w와 h는 1 이상 1,000 이하인 자연수이다

Example:
- Input : sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
- Output : 4000

- Input : sizes=[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
- Output : 120

- Input : sizes=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
- Output : 133

Note:
명함의 가로 길이가 무조건 세로 길이보다 길거나 같도록 하기 위해 map을 사용
가로 길이 중에서 가장 긴 길이와 세로 길이 중에서 가장 긴 길이가 지갑의 크기가 된다

"""

def rotate(l):
    if l[0] < l[1]:
        return [l[1], l[0]]
    return l

def solution(sizes):
    rotated = list(zip(*map(rotate, sizes)))
    return max(rotated[0]) * max(rotated[1])