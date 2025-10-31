"""

봉인된 주문 : https://school.programmers.co.kr/learn/courses/30/lessons/389481

앒파벳 소문자로 이루어진 문자열이 정렬되어 있고, 몇몇 문자열이 지워졌을 때, n번째 문자열을 찾는 문제
- 문자열은 알파벳 소문자 11글자 이하로 쓸 수 있는 모든 문자열이 정렬되어 있다
    - 글자 수가 적은 주문부터 먼저 기록된다
    - 글자 수가 같다면, 사전 순서대로 기록된다
- n은 1 이상 10^15 이하이다
- bans의 길이는 1 이상 300,000 이하이며, bans의 원소는 알파벳 소문자로만 이루어진 길이 1 이상 11 이하인 문자열이다
- bans의 원소는 중복되지 않는다

Example:
- Input : n=30, bans=["d", "e", "bb", "aa", "ae"]
- Output : "ah"

- Input : n=7388, bans=["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]
- Output : "jxk"

Note:
문자열을 순서(정수)로 변환 후, 구해진 답을 다시 문자열로 변환하는 방식
bans를 그대로 정렬하면 ["a", "aa", "b", ... ] 같은 순서로 정렬되므로, 원하는 순서로 정렬하기 위해 알파벳으로 이루어진 26진법을 10진법으로 변환

"""

def solution(n, bans):
    ibans = []
    for ban in bans:
        temp = 0
        for ch in ban:
            temp = temp * 26 + (ord(ch) - ord("a") + 1)
        ibans.append(temp)
    ibans.sort()
    for i in ibans:
        if i <= n:
            n += 1
        else:
            break
    res = ""
    while n > 0:
        n, mod = divmod((n-1), 26)
        res += chr(mod + ord("a"))
    return res[::-1]