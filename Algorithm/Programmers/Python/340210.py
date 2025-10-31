"""

[PCCP 기출문제] 4번 / 수식 복원하기 : https://school.programmers.co.kr/learn/courses/30/lessons/340210

2 ~ 9진법 중 하나를 사용하는 진법 체계에서 덧셈 및 뺄셈 수식이 주어졌을 때, 결괏값이 지워진 수식들의 결괏값을 채워넣는 문제
- 결괏값이 불확실한 경우 ?를 사용하여 1 + 5 = ? 과 같이 출력한다
- expressions는 "A + B = C" 혹은 "A - B = C" 형태의 문자열이며, 공백 하나로 구분된다
- A, B는 음이 아닌 두자릿수 이하의 정수이다
- C는 알파벳 X(지워짐) 혹은 음이 아닌 세자릿수 이하의 정수이다
- 결괏값이 음수가 되거나 서로 모순되는 수식은 주어지지 않는다

Example:
- Input : expressions=["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
- Output : ["13 - 6 = 5"]
- 8진법

- Input : expressions=["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]
- Output : ["1 + 5 = ?", "1 + 2 = 3"]
- 6 ~ 9진법이 가능 / 1 + 5가 6진법일 때는 10, 7 ~ 9진법일 때는 6이 되므로 ?가 된다

- Input : expressions=["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]
- Output : ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]

- Input : expressions=["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]
- Output : ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]

- Input : ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]
- Output : ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]

Note:
수식에 포함된 숫자들을 바탕으로 가능한 최소 진법(숫자 6이 포함되었다면 7진법 이상이어야 모순되지 않는다) 계산
int(num, base)를 사용하여 base 진법에 기반한 값을 획득 가능

"""

def solution(expressions):
    known = []
    unknown = []
    numbers = set()

    for expr in expressions:
        a, op, b, c = parse_expression(expr)
        numbers.add(a)
        numbers.add(b)
        if c == "X":
            unknown.append((a, op, b, expr))
        else:
            known.append((a, op, b, c))
            numbers.add(c)

    min_base = get_min_base(numbers)

    possible_bases = []
    for base in range(min_base, 10):
        valid = True
        for a, op, b, c in known:
            if not all(is_valid(s, base) for s in numbers):
                valid = False
                break
            left = calc_left(a, op, b, base)
            if left != int(c, base):
                valid = False
                break
        if valid:
            possible_bases.append(base)

    answer = []
    for a, op, b, original_expr in unknown:
        results = set()
        for base in possible_bases:
            calc = change(calc_left(a, op, b, base), base)
            results.add(calc)

        if len(results) == 1:
            answer.append(f"{a} {op} {b} = {results.pop()}")
        else:
            answer.append(f"{a} {op} {b} = ?")

    return answer

def parse_expression(expr):
    a, op, b, _, c = expr.split()
    return a, op, b, c

def get_min_base(numbers):
    max_num = 0
    for s in numbers:
        for ch in s:
            max_num = max(max_num, int(ch))
    return max_num + 1

def is_valid(s, base):
    try:
        return all(int(ch) < base for ch in s)
    except:
        return False

def calc_left(a, op, b, base):
    return int(a, base) + int(b, base) if op == "+" else int(a, base) - int(b, base)

def change(num, base):
    if num == 0:
        return '0'
    res = ''
    while num > 0:
        num, mod = divmod(num, base)
        res += str(mod)
    return res[::-1]
