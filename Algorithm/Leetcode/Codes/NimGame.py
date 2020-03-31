"""

292. Nim Game : https://leetcode.com/problems/nim-game/

Nim Game 중 남은 돌의 갯수가 주어졌을 때, 내가 이길 수 있는지 여부를 확인하는 문제
- 한 턴에 1개에서 3개의 돌을 가져갈 수 있다
- 마지막 남은 돌을 지우는 사람이 승리한다

Example:
- Input : 4
- Output : false
- 내가 1~3개 중 몇 개의 돌을 가져가건 상대방이 무조건 마지막 돌을 가져갈 수 있다

Note:
남은 돌의 개수와 승패 유무를 확인해보면, 내 턴에 무조건 질 수 밖에 없는 돌의 갯수를 만들 수 있다면 이길 수 있다
1~3개가 남은 경우 무조건 이기고, 4개가 남은 경우에는 무조건 지며,
5개가 남은 경우 1개만 가져가면 상대방에게 4개만 남기 때문에 무조건 이길 수 있다
이런 방식으로 규칙을 계산해보면 돌의 개수가 4의 배수인 경우에 진다

"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        b = n >> 2 << 2
        if b == n :
            return False
        else :
            return True