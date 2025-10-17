"""

테이블 해시 함수 : https://school.programmers.co.kr/learn/courses/30/lessons/147354

테이블의 데이터와 해시 함수에 대한 입력이 주어졌을 때, 테이블의 해시 값을 구하는 문제
- 테이블은 모두 정수 타입인 컬럼들로 이루어져 있다
    - 첫 번째 컬럼은 기본키로서 모든 튜플에 대해 그 값이 중복되지 않음을 보장한다
- 해시 함수는 다음과 같이 정의한다
    - 해시 함수는 col, row_begin, row_end를 입력으로 받는다
    - 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬한다
    - 정렬된 데이터에서 S_i를 i번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의한다
    - row_begin <= i <= row_end인 모든 S_i를 누적하여 bitwise XOR한 값을 해시 값으로 한다
- 테이블의 데이터 data의 길이는 1 이상 2500 이하이다
    - data의 원소의 길이는 1 이상 500 이하이다
    - data[i][j]는 1 이상 1,000,000 이하인 정수로, i+1번째 튜플의 j+1번째 컬럼의 값을 의미한다
- col은 1 이상 data의 원소의 길이 이하이다
- row_begin, row_end는 1 이상 data의 길이 이하이며, row_begin은 row_end보다 작거나 같다

Example:
- Input : data=[[2,2,6],[1,5,10],[4,2,9],[3,8,3]], col=2, row_begin=2, row_end=3
- Output : 4

Note:
문제에 제시된 해시 함수를 그대로 구현

"""

def getMod(row, num):
    return sum(row[i] % num for i in range(len(row)))

def solution(data, col, row_begin, row_end):
    sdata = sorted(data, key=lambda x: (x[col-1], -x[0]))
    answer = 0

    for i in range(row_begin-1, row_end):
        mod = getMod(sdata[i], i+1)
        answer = answer ^ mod

    return answer