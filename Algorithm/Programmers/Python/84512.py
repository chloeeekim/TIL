"""

모음 사전 : https://school.programmers.co.kr/learn/courses/30/lessons/84512

알파벳 모음 A, E, I, O, U만을 사용하여 만들 수 있는 길이 5 이하의 모든 단어가 수록되어 있을 때, 특정 단어가 사전에서 몇 번째 단어인지 구하는 문제
- 사전에서 첫 번째 단어는 "A"이고, 그 다음은 "AA"이며, 마지막 단어는 "UUUUU"이다
- word의 길이는 1 이상 5 이하이다
    - word는 알파벳 대문자 A, E, I, O, U로만 이루어져 있다

Example:
- Input : word="AAAAE"
- Output : 6

- Input : word="AAAE"
- Output : 10

- Input : word="I"
- Output : 1563

- Input : word="EIO"
- Output : 1189

Note:
다섯 종류의 문자로 길이 5 이하의 문자열을 만드는 것이므로 가능한 경우의 수가 적어 모든 경우의 수를 구하여도 문제 없다
itertools의 product로 중복순열을 구한 다음, 인덱스를 구하는 방식

"""

from itertools import product

def solution(word):
    products = []
    for i in range(1, 6):
        for p in product(["A", "E", "I", "O", "U"], repeat=i):
            products.append("".join(list(p)))
    products.sort()
    return products.index(word) + 1
