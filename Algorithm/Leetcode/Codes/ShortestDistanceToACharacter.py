"""

821. Shortest Distance to a Character : https://leetcode.com/problems/shortest-distance-to-a-character/

문자열 S와 문자 C가 주어졌을 때, S의 각 문자들의 C로부터의 최소 거리를 구하는 문제
- S의 길이는 [1, 10000] 범위이다
- C는 single character이며, S에 포함되어 있다
- S와 C는 모두 소문자 알파벳이다

Example:
- Input : S = "loveleetcode", C = 'e'
- Output : [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
왼쪽에서 오른쪽으로 순회하면서 C로부터의 거리를 측정하고,
오른쪽에서 왼쪽으로 순회하면서 C로부터의 거리를 측정하여 작은 값을 선택

"""

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        length, count = len(S), len(S)
        res = [length for _ in range(length)]
        for i, ch in enumerate(S):
            count = 0 if ch == C else count+1
            res[i] = count
        count = length
        for i in range(length-1, -1, -1):
            count = 0 if S[i] == C else count+1
            res[i] = min(res[i], count)
        return res