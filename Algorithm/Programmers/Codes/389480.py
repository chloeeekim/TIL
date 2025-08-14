"""

완전범죄 : https://school.programmers.co.kr/learn/courses/30/lessons/389480

A 도둑과 B 도둑이 모두 경찰에 붙잡히지 않도록 모든 물건을 훔쳤을 때, A 도둑이 남긴 흔적의 누적 개수의 최솟값을 구하는 문제
- 물건 i를 훔칠 때, A 도둑이 훔치거나 B 도둑이 훔칠 수 있으며, 각각 info[i][0], info[i][1] 개의 흔적이 남는다
- 각 물건에 대한 흔적의 개수는 1 이상 3 이하이다
- A 도둑이 n개 이상의 흔적을 남기거나 B 도둑이 m개 이상의 흔적을 남기면 경찰에 붙잡힌다
- 어떠한 방법으로도 두 도둑 모두 경찰에 붙잡히지 않게 할 수 없다면 -1을 리턴한다

Example:
- Input : info=[[1, 2], [2, 3], [2, 1]], n=4, m=4
- Output : 2
- 첫 번째와 세 번째 물건을 B 도둑이 훔치고, 두 번째 물건을 A 도둑이 훔치는 경우

- Input : info=[[1, 2], [2, 3], [2, 1]], n=1, m=7
- Output : 0
- 모든 물건을 B 도둑이 훔치는 경우

- Input : info=[[3, 3], [3, 3]], n=7, m=1
- Output : 6
- 모든 물건을 A 도둑이 훔치는 경우

- Input : info=[[3, 3], [3, 3]], n=6, m=1
- Output : -1

Note:
dp로 해결
훔치는 물건과 B 도둑이 남긴 흔적에 대해 A 도둑이 남긴 흔적을 2차원 배열 형태로 구성
모든 물건을 다 훔친 경우, A 도둑이 남길 수 있는 흔적의 최솟값을 구하여 n보다 크면 -1을 리턴

"""

def solution(info, n, m):
    size = len(info)
    arr = [[99999] * m for _ in range(size + 1)]
    arr[0][0] = 0

    for i in range(1, size + 1):
        a, b = info[i-1]

        for j in range(m):
            arr[i][j] = min(arr[i][j], arr[i-1][j] + a)

            if (b + j < m):
                arr[i][j + b] = min(arr[i][j + b], arr[i-1][j])

    res = 99999
    for i in range(m):
        res = min(res, arr[size][i])
    return res if res < n else -1