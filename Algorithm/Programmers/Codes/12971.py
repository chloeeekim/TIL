"""

스티커 모으기(2) : https://school.programmers.co.kr/learn/courses/30/lessons/12971

N개의 원형으로 연결된 스티커가 주어졌을 때, 뜯어낸 스티커들의 합의 최댓값을 구하는 문제
- 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없다
- sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이는 1 이상 100,000 이하이다
    - sticker의 각 원소는 1 이상 100 이하의 자연수이다
    - sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주한다

Example:
- Input : sticker=[14, 6, 5, 11, 3, 9, 2, 10]
- Output : 36

- Input : sticker=[1, 3, 2, 5, 4]
- Output : 8

Note:
DP로 해결
원형이기 때문에 0번 인덱스의 스티커를 떼는 경우와 1번 인덱스의 스티커를 떼는 경우, 두 가지로 나눠서 계산

"""

def solution(sticker):
    length = len(sticker)
    if length == 1:
        return sticker[0]

    arr1 = [0] + sticker[:-1]
    arr2 = [0] + sticker[1:]
    for i in range(2, length):
        arr1[i] = max(arr1[i-1], arr1[i-2] + arr1[i])
        arr2[i] = max(arr2[i-1], arr2[i-2] + arr2[i])

    return max(arr1[-1], arr2[-1])
