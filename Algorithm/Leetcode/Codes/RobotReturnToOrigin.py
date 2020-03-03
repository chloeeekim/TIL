"""

657. Robot Return to Origin : https://leetcode.com/problems/robot-return-to-origin/

로봇의 움직임을 나타낸 문자열이 주어졌을 때, 로봇이 시작 지점으로 돌아오는지 찾는 문제
- 시작 지점은 (0,0)이며, 모든 움직임이 종료되었을 때 (0,0)에서 끝나는지 확인
- 움직임은 총 4가지이다: R(right), L(left), U(up), D(down)
- 각 move마다 동일한 거리를 이동하며, 로봇의 이동 방향은 절대적이다

Example:
- Input : "UD"
- Output : true

- Input : "LL"
- Output : false

Note:
문자 케이스별로 확인하여 2차원 좌표 상의 위치를 계산

"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves :
            if move == 'R' :
                x += 1
            elif move == 'L' :
                x -= 1
            elif move == 'U' :
                y += 1
            else :
                y -= 1
        return True if x == 0 and y == 0 else False