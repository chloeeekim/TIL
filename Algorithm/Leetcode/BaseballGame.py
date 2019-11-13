"""

682. Baseball Game : https://leetcode.com/problems/baseball-game/

야구 게임의 점수가 기록된 list가 주어졌을 때, 최종 점수를 구하는 문제
- 입력은 총 4가지이다 (integer, '+', 'D', 'C')
- integer : 해당 round의 점수
- '+' : valid한 이전 두 round의 점수의 합이 해당 round의 점수
- 'D' : valid한 이전 round의 점수의 두 배가 해당 round의 점수
- 'C' : 이전 round의 점수가 invalid함을 나타냄 (해당 점수는 삭제)
- 입력되는 list의 크기는 [1,1000] 범위이다
- 입력으로 들어오는 integer는 [-30000, 30000] 범위이다

Example:
- Input : ["5","2","C","D","+"]
- Output : 30
- valid한 각 라운드별 점수는 [5,10,15] (2는 invalid)

- Input : ["5","-2","4","C","D","9","+","+"]
- Output : 27
- valid한 각 라운드별 점수는 [5,-2,-4,9,5,14] (3번째의 4는 invalid)

Note:
각 라운드별로 유효한 점수를 scores 리스트로 관리하여 마지막에 전체 합을 구하는 방식
isdigit, isdecimal, isnumeric 모두 음수에 대해서는 판별이 불가
음수의 경우 op[0] == '-' and op[1:].isdecimal()로 확인

"""

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops :
            if op.isdecimal() :
                scores.append(int(op))
            elif op[0] == '-' and op[1:].isdecimal() :
                scores.append(int(op))
            elif op == 'C' :
                scores.pop()
            elif op == 'D' :
                scores.append(scores[-1] * 2)
            else :
                scores.append(scores[-1] + scores[-2])
        return sum(scores)