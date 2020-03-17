"""

150. Evaluate Reverse Polish Notation : https://leetcode.com/problems/evaluate-reverse-polish-notation/

RPN(Reverse Polish Notation)의 형태로 주어진 수식의 답을 구하는 문제
- valid한 operator는 +, -, *, / 네 종류이다
- 두 정수를 나눈 경우 소수점 이하는 내림으로 처리한다
- 주어진 RPN expression은 항상 valid하다 (0으로 나누거나 하는 경우는 없다)

Example:
- Input : ["2", "1", "+", "3", "*"]
- Output : 9
- ((2 + 1) * 3) = 9

- Input : ["4", "13", "5", "/", "+"]
- Output : 6
- (4 + (13 / 5)) = 6

- Input : ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
- Output : 22
- ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22

Note:
stack을 사용하여 해결
op가 아닌 경우 숫자임이 보장되므로,
숫자라면 stack에 넣고, op가 나오면 이전에 stack에 넣었던 두 숫자를 꺼내서 연산 후 다시 stack에 넣는다

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        stack = []
        for token in tokens :
            if token in op :
                a, b = stack.pop(-1), stack.pop(-1)
                if token == '+' :
                    stack.append(a+b)
                elif token == '-' :
                    stack.append(b-a)
                elif token == '*' :
                    stack.append(a*b)
                else :
                    stack.append(int(b/a))
            else :
                stack.append(int(token))
        return stack.pop(-1)