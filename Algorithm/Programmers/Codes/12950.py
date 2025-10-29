"""

행렬의 덧셈 : https://school.programmers.co.kr/learn/courses/30/lessons/12950

행과 열의 크기가 같은 두 행렬이 주어졌을 때, 같은 행, 같은 열의 값을 서로 더한 결과를 구하는 문제
- 행렬 arr1과 arr2의 행과 열의 길이는 500을 넘지 않는다

Example:
- Input : arr1=[[1,2],[2,3]], arr2=[[3,4],[5,6]]
- Output : [[4,6],[7,9]]

- Input : arr1=[[1],[2]], arr2=[[3],[4]]
- Output : [[4],[6]]

Note:
결과 배열을 arr1과 동일한 크기로 0으로 채워 놓은 다음
이중 반복문을 통해 arr1과 arr2의 값을 더해 결과에 넣는 방식

"""

def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer