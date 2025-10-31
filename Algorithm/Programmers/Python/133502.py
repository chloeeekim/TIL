"""

햄버거 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/133502

재료의 정보가 주어졌을 때, 포장 완료되는 햄버거의 개수를 구하는 문제
- 재료들은 조리된 순서대로 아래에서부터 위로 쌓이며, 순서에 맞게 쌓여서 완성된 햄버거는 포장한다
- 아래에서부터 빵 - 야채 - 고기 - 빵 순서로 쌓인 햄버거만 포장한다
- 재료의 정보를 나타내는 정수 배열 ingredient의 길이는 1 이상 1,000,000 이하이다
    - ingredient의 원소는 1, 2, 3 중 하나이며, 각각 빵, 야채, 고기를 의미한다

Example:
- Input : ingredient=[2, 1, 1, 2, 3, 1, 2, 3, 1]
- Output : 2

- Input : ingredient=[1, 3, 2, 1, 2, 1, 3, 1, 2]
- Output : 0

Note:
stack을 사용하여 해결
현재 주어진 재료가 빵(1)이며, stack에 들어간 재료들이 역순으로 고기(3), 야채(2), 빵(1)이라면 햄버거를 하나 만들 수 있다

"""

def solution(ingredient):
    answer = 0
    stack = []
    hamburger = [3, 2, 1]

    for i in ingredient:
        if i == 1 and len(stack) >= 3 and all(stack[-i] == hamburger[i-1] for i in range(1, 4)):
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
        else:
            stack.append(i)
    return answer