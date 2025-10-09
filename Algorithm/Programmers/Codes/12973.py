"""

짝지어 제거하기 : https://school.programmers.co.kr/learn/courses/30/lessons/12973

알파벳 소문자로 이루어진 문자열이 주어졌을 때, 2개씩 붙어 있는 짝을 제거하는 방식으로 문자열을 모두 제거할 수 있는지 확인하는 문제
- 문자열 제거는 다음과 같은 방식으로 이루어진다
    - 같은 알파벳이 2개 붙어 있는 짝을 찾는다
    - 동일한 알파벳 두 개를 제거한 뒤, 앞뒤로 문자열을 이어 붙인다
- 문자열 s의 길이는 1,000,000 이하이며, 문자열은 모두 소문자로 이루어져 있다
- 문자열을 모두 제거할 수 있다면 1을, 아닐 경우 0을 리턴한다

Example:
- Input : s="baabaa"
- Output : 1

- Input : s="cdcd"
- Output : 0

Note:
stack을 사용하여 해결
동일한 문자가 이어서 나온다면 stack에서 제거, 아니라면 stack에 추가
최종적으로 stack이 비어 있는 경우 모두 제거할 수 있으므로 1을 리턴

"""

def solution(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return 1 if not stack else 0
