"""

1차 / 뉴스 클러스터링 : https://school.programmers.co.kr/learn/courses/30/lessons/17677

두 문자열이 주어졌을 때, 주어진 문자열을 두 글자씩 끊어 만든 다중집합으로 자카드 유사도를 구하는 문제
- 자카드 유사도는 두 집합 A, B의 교집합 크기를 합집합 크기로 나눈 값으로 정의된다
- 집합 A와 B가 모두 공집합일 경우, 자카드 유사도는 1로 정의한다
- 입력으로 주어지는 str1과 str2는 길이 2 이상 1000 이하의 문자열이다
- 문자열을 두 글자씩 끊어서 다중집합으로 만들 때, 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수문자가 포함된 글자 쌍은 버린다
- 다중집합 원소 사이를 비교할 때, 대소문자의 차이는 무시한다
- 구해진 자카드 유사도 값에 65536을 곱한 후 소수점 아래를 버리고 정수부만 리턴한다

Example:
- Input : str1="FRANCE", str2="french"
- Output : 16384

- Input : str1="handshake", str2="shake hands"
- Output : 65536

- Input : str1="aa1+aa2", str2="AAAA12"
- Output : 43690

- Input : str1="E=M*C^2", str2="e=m*c^2"
- Output : 65536

Note:
set을 사용하여 다중집합에 포함된 원소를 확인
collections의 Counter를 사용해서 교집합과 합집합에 포함되는 원소들의 개수를 계산

"""

from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()

    def make_sp(string):
        sp = []
        for i in range(len(string) - 1):
            temp = string[i:i+2]
            if temp.isalpha():
                sp.append(temp)
        return sp

    sp1, sp2 = make_sp(str1), make_sp(str2)

    if not sp1 and not sp2:
        return 65536

    exists = set(sp1 + sp2)
    count1, count2 = Counter(sp1), Counter(sp2)

    minimum, maximum = 0, 0

    for e in exists:
        c1, c2 = count1[e], count2[e]
        minimum += min(c1, c2)
        maximum += max(c1, c2)

    return int(minimum / maximum * 65536)