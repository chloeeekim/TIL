"""

크기가 작은 부분문자열 : https://school.programmers.co.kr/learn/courses/30/lessons/147355

숫자로 이루어진 문자열 t, p가 주어졌을 때, t에서 p와 길이가 같은 부분문자열 중 p보다 작거나 같은 것이 나오는 횟수를 구하는 문제
- p의 길이는 1 이상 18 이하이다
- t의 길이는 p의 길이 이상 10,000 이하이다
- t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않는다

Example:
- Input : t="3141592", p="271"
- Output : 2
- 141, 159 두 가지

- Input : t="500220839878", p="7"
- Output : 8

- Input : t="10203", p="15"
- Output : 3

Note:
p의 길이만큼 t의 부분문자열을 구한 다음, 숫자로 변환하여 비교

"""

def solution(t, p):
    answer = 0

    lenp = len(p)
    pnum = int(p)
    for i in range(len(t) - lenp + 1):
        tnum = int(t[i:i+lenp])
        if tnum <= pnum:
            answer += 1

    return answer