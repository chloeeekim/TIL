"""

3진법 뒤집기 : https://school.programmers.co.kr/learn/courses/30/lessons/68935

자연수 n이 주어졌을 때, n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 구하는 문제
- n은 1 이상 100,000,000 이하인 자연수이다

Example:
- Input : n=45
- Output : 7
- 45 -> 1200 (3진법) -> 0021 (3진법 뒤집기) -> 7 (10진법)

- Input : n=125
- Output : 229
- 125 -> 11122 (3진법) -> 22111 (3진법 뒤집기) -> 229 (10진법)

Note:
divmod를 사용하여 뒤집은 3진법을 구한 다음, 10진법으로 변환

"""

def solution(n):
    tri = ''
    while n >= 3:
        n, mod = divmod(n, 3)
        tri += str(mod)
    tri += str(n)
    return int(tri, 3)