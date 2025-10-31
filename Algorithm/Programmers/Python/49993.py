"""

스킬트리 : https://school.programmers.co.kr/learn/courses/30/lessons/49993

선행 스킬 순서와 유저들이 만든 스킬트리가 주어졌을 때, 가능한 스킬트리의 개수를 구하는 문제
- 선행 스킬은 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 의미한다
- 선행 스킬 순서에 없는 스킬은 순서에 상관없이 배울 수 있다
- 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있다
- 스킬 순서와 스킬트리는 문자열로 표기한다
    - 예를 들어, C -> B -> D 라면 "CBD"로 표기한다
- 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해서 주어지지 않는다
- skill_trees는 길이 1 이상 20 이하인 배열이다
    - skill_trees의 원소는 길이 2 이상 26 이하인 문자열이며, 스킬은 중복해서 주어지지 않는다

Example:
- Input : skill="CBD", skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
- Output : 2
- "CBADF"와 "AECB"가 가능한 스킬트리

Note:
선행 스킬 순서의 idx로 판단
특정 문자(스킬)이 선행 스킬 순서에 없으면(find 결과가 -1) 고려하지 않고,
있다면 현재 나와야 하는 idx와 일치하는지 확인

"""

def solution(skill, skill_trees):
    answer = 0
    for stree in skill_trees:
        idx = 0
        avail = True
        for ch in stree:
            temp = skill.find(ch)
            if temp == -1:
                continue
            elif temp == idx:
                idx += 1
            else:
                avail = False
                break
        answer += 1 if avail else 0
    return answer