"""

110 옮기기 : https://school.programmers.co.kr/learn/courses/30/lessons/77886

0과 1로 이루어진 문자열이 주어졌을 때, 특정 행위를 통해 만들 수 있는 문자열 중 사전 순으로 가장 앞에 오는 문자열을 구하는 문제
- 문자열 x에 대해 다음과 같은 행동을 반복한다
    - x에 있는 "110"을 뽑아서, 임의의 위치에 다시 삽입한다
- 변형시킬 문자열 x가 여러 개 들어있는 문자열 배열 s의 길이는 1 이상 1,000,000 이하이다
    - s의 각 원소의 길이는 1 이상 1,000,000 이하이다
    - s의 모든 원소의 길이의 합은 1 이상 1,000,000 이하이다

Example:
- Input : s=["1110","100111100","0111111010"]
- Output : ["1101","100110110","0110110111"]

Note:
stack을 사용하여 "110"이 나오는 경우를 모두 카운트 후 제거
남은 문자열은 "110"이 없는 "1"과 "0"으로 이루어진 문자열
만약 남은 문자열에 "0"이 있다면 "100", "101" 등 "110"보다는 사전 순으로 앞에 있게 된다
따라서 마지막에 있는 "0" 뒤에 "110"을 반복해서 붙이는 것이 사전 순으로 가장 빠른 문자열이 된다
만약 남은 문자열에 "0"이 없다면 모두 "1"로 이루어져 있으므로,
가장 앞에 "110"을 반복해서 붙이는 것이 사전 순으로 가장 빠른 문자열이 된다

"""

def solution(s):
    answer = []
    for x in s:
        stack = []
        count_110 = 0
        for num in x:
            if len(stack) >= 2 and num == "0":
                if stack[-1] == "1" and stack[-2] == "1":
                    count_110 += 1
                    stack.pop()
                    stack.pop()
                    continue
            stack.append(num)

        insert_idx = "".join(stack).rfind("0")

        ans = "".join(stack[:insert_idx+1]) + "110" * count_110 + "".join(stack[insert_idx+1:])
        answer.append(ans)

    return answer