"""

997. Find the Town Judge : https://leetcode.com/problems/find-the-town-judge/

n명의 사람이 있는 town에서 trust 리스트가 주어졌을 때, town judge가 있는지 찾는 문제
- town judge는 아무도 믿지 않는다
- 모든 사람(town judge 자신을 제외한)은 town judge를 믿는다
- 위 조건을 만족하는 사람이 한 명일 때 town judge가 존재한다
- town judge가 존재하지 않는 경우 -1을 리턴

Example:
- Input : n = 2, trust = [[1,2]]
- Output : 2

- Input : n = 3, trust = [[1,3],[2,3]]
- Output : 3

- Input : n = 3, trust = [[1,3],[2,3],[3,1]]
- Output : -1

Note:
from, to 리스트를 생성하여 trust 값을 저장
아무도 믿지 않으면서 모두가 자신을 믿는 경우 town judge로 판단

"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tfrom, tto = [0] * (n+1), [0] * (n+1)
        for t in trust:
            tfrom[t[0]] += 1
            tto[t[1]] += 1
        for i in range(1, n+1):
            if tfrom[i] == 0 and tto[i] == n-1:
                return i
        return -1