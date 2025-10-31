"""

n^2 배열 자르기 : https://school.programmers.co.kr/learn/courses/30/lessons/87390

정수 n, left, right를 사용해서 주어진 과정대로 1차원 배열을 만드는 문제
- 1차원 배열을 만드는 과정은 다음과 같다
    - n행 n열 크기의 비어있는 2차원 배열을 만든다
    - i = 1, 2, 3, ..., n에 대해서 다음 과정을 반복한다
        - 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채운다
    - 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만든다
    - 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지운다
- n은 1 이상 10^7 이하의 정수이다
- left와 right는 0 <= left <= right < n^2을 만족하는 정수이다
- right - left는 10^5 미만이다

Example:
- Input : n=3, left=2, right=5
- Output : [3,2,2,3]

- Input : n=4, left=7, right=14
- Output : [4,3,3,3,4,4,4,4]

Note:
(i, j) 위치일 때 값은 i와 j 중 큰 값 + 1이 된다
1차원 배열일 때 i, j는 인덱스를 n으로 나눈 몫과 나머지이다

"""

def solution(n, left, right):
    res = []
    for i in range(left, right + 1):
        div, mod = divmod(i, n)
        res.append(max(div, mod) + 1)
    return res