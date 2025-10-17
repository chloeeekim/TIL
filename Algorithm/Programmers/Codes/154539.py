"""

뒤에 있는 큰 수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/154539

정수로 이루어진 배열이 주어졌을 때, 배열의 각 원소들에 대해 뒷 큰수를 구하는 문제
- 뒷 큰수란 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 의미한다
- 모든 원소에 대한 뒷 큰수들을 차례대로 담은 배열을 리턴한다
    - 단, 뒷 큰수가 존재하지 않는 원소의 경우 -1을 배열에 담는다
- 정수 배열 numbers의 길이는 4 이상 1,000,000 이하이다
    - numbers의 원소는 1 이상 1,000,000 이하의 정수이다

Example:
- Input : numbers=[2, 3, 3, 5]
- Output : [3, 5, 5, -1]

- Input : numbers=[9, 1, 5, 3, 6, 2]
- Output : [-1, 5, 6, 6, -1, -1]

Note:
배열을 뒤에서부터 확인하며 다음과 같은 방식으로 stack에 큰 수를 저장한다
1. stack이 비어 있는 경우 뒷 큰수가 없으므로, 뒷 큰수는 -1이 되고, 현재 숫자를 stack에 추가
2. stack이 비어 있지 않는 경우
2-1. stack의 숫자가 현재 숫자보다 크면 해당 숫자가 뒷 큰수가 되고, 현재 숫자를 stack에 추가
2-2. stack의 숫자가 현재 숫자보다 작거나 같으면 stack에서 해당 숫자를 제거하고, stack을 계속 확인
2-3. stack에서 뒷 큰수를 찾을 수 없는 경우, 뒷 큰수는 -1이 되고, 현재 숫자를 stack에 추가
배열을 뒤에서부터 확인하면서 정답을 찾았으므로 결과는 뒤집어서 리턴

"""

def solution(numbers):
    answer = []
    stack = []

    for i in range(len(numbers)-1, -1, -1):
        if not stack:
            answer.append(-1)
            stack.append(numbers[i])
        else:
            exists = False
            for j in range(len(stack)-1, -1, -1):
                if stack[j] > numbers[i]:
                    answer.append(stack[j])
                    stack.append(numbers[i])
                    exists = True
                    break
                elif stack[j] <= numbers[i]:
                    stack.pop()

            if not exists:
                answer.append(-1)
                stack.append(numbers[i])

    return answer[::-1]