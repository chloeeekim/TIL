"""

수식 최대화 : https://school.programmers.co.kr/learn/courses/30/lessons/67257

수식이 주어졌을 때, 연산자의 우선순위를 새롭게 정의해 만들 수 있는 가장 큰 숫자를 구하는 문제
- 수식에 포함되는 연산자는 +, -, * 세 가지이다
- 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 한다
- 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 가장 큰 숫자를 선택한다
- expression은 길이 3 이상 100 이하인 문자열이다
    - expression은 공백문자, 괄호문자 없이 숫자와 3가지의 연산자만으로 이루어진 올바른 중위표기법으로 표현된 연산식이다
    - 잘못된 연산식은 입력으로 주어지지 않는다
    - expression의 피연산자(operand)는 0 이상 999 이하의 정수이다
        - 피연산자가 음수인 수식은 입력으로 주어지지 않는다
    - expression은 적어도 1개 이상의 연산자를 포함한다
    - 연산자 우선순위를 어떻게 적용하더라고 중간 계산값과 최종 결과값은 절댓값이 2^63 - 1 이하가 되도록 입력이 주어진다
    - 같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높다

Example:
- Input : expression="100-200*300-500+20"
- Output : 60420

- Input : expression="50*6-3*2"
- Output : 300

Note:
3가지 연산자에 대해서 기능한 우선순위 조합은 6가지이므로 permutations로 조합을 생성하여 전부 다 확인

"""

from itertools import permutations

def solution(expression):
    numbers, ops = [], []
    temp = 0
    for ch in expression:
        if ch.isdigit():
            temp = temp * 10 + int(ch)
        else:
            numbers.append(temp)
            temp = 0
            ops.append(ch)
    numbers.append(temp)

    def calc(tnums, tops, orders):
        for op in orders:
            while op in tops:
                idx = tops.index(op)
                if op == "*":
                    calc = tnums[idx] * tnums[idx + 1]
                elif op == "+":
                    calc = tnums[idx] + tnums[idx + 1]
                else:
                    calc = tnums[idx] - tnums[idx + 1]
                tnums[idx] = calc
                tnums.pop(idx + 1)
                tops.pop(idx)
        return tnums[0]

    perm = permutations(["*", "+", "-"], 3)
    res = []
    for p in perm:
        res.append(calc(numbers[:], ops[:], p))
    return max(abs(r) for r in res)