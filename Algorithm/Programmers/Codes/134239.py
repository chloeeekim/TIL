"""

우박수열 정적분 : https://school.programmers.co.kr/learn/courses/30/lessons/134239

우박수의 초항 k와 정적분을 구하는 구간들의 목록이 주어졌을 때, 정적분의 결과 목록을 구하는 문제
- 우박수열을 구하는 방법은 다음과 같다
    - 1-1. 입력된 수가 짝수라면 2로 나눈다
    - 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다
    - 2. 결과로 나온 수가 1보다 크다면 1번 작업을 반복한다
- 초항이 k인 우박수열이 있다면, x = 0일 때 y = k이고, 다음 우박수는 x = 1에 표시한다
    - 우박수가 1이 될 때까지 점을 찍고, 인접한 점들끼리 직선으로 연결하여 꺾은선 그래프를 만들 수 있다
- x에 대한 범위 [a, b]의 정적분 결과는 꺾은선 그래프와 x = a, x = b, y = 0으로 둘러 쌓인 공간의 면적과 같다
- 0 이상의 수 b에 대해 [a, -b]에 대한 정적분 결과는 x = a, x = n - b, y = 0으로 둘러 싸인 공간의 면적과 같다
    - 이때 n은 k가 초항인 우박수열이 1이 될 때까지의 횟수를 의미한다
- 우박수의 초항 k는 2 이상 10,000 이하의 정수이다
- 정적분을 구하는 구간들의 목록 ranges의 길이는 1 이상 10,000 이하이다
    - ranges의 원소는 [a, b] 형식이며, 0 <= a < 200, -200 < b <= 0을 만족한다
- 주어진 모든 입력에 대해 정적분의 결과는 2^27을 넘지 않는다
- 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어지는 경우, 정적분의 결과는 -1로 정의한다

Example:
- Input : k=5, ranges=[[0,0],[0,-1],[2,-3],[3,-3]]
- Output : [33.0,31.5,0.0,-1.0]
- 5로 시작하는 우박수열은 5 -> 16 -> 8 -> 4 -> 2 -> 1이다

- Input : k=3, ranges=[[0,0], [1,-2], [3,-3]]
- Output : [47.0,36.0,12.0]
- 3으로 시작하는 우박수열은 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1이다

Note:
getSequence 함수를 통해 k로 시작하는 우박수열을 구한다
구해진 우박수열에 대해 x의 너비가 1인 구간마다 정적분을 구하면, (윗변의 길이(i번째 우박수) + 아랫변의 길이(i+1번째 우박수)) / 2가 된다
[a, b] 구간의 정적분은 [a, a+1], [a+1, a+2], ... , [b-1, b] 구간의 정적분의 합이 된다

"""

def getSequence(k):
    res = [k]
    while k > 1:
        if k % 2 == 1:
            k = k * 3 + 1
        else:
            k //= 2
        res.append(k)
    return res

def solution(k, ranges):
    sequence = getSequence(k)

    n = len(sequence) - 1
    ssum = []
    for i in range(n):
        ssum.append((sequence[i] + sequence[i+1]) / 2)

    answer = []
    for a, b in ranges:
        start, end = a, n + b
        if start > end:
            answer.append(-1)
            continue

        temp = 0
        for i in range(start, end):
            temp += ssum[i]
        answer.append(temp)

    return answer