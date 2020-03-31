"""

319. Bulb Switcher : https://leetcode.com/problems/bulb-switcher/

n개의 전구를 다음 조건에 맞춰 on/off를 반복할 때, 최종적으로 켜져 있는 전구의 개수를 구하는 문제
- i번째 라운드에서는 매 i번째 전구를 toggle한다
- 1번째 라운드를 시작하기 전에는 모든 전구가 off되어 있다 (1 라운드 이후 모든 전구가 켜진다)

Example:
- Input : 3
- Output : 1
- 초기: [off,off,off] / 1 라운드: [on,on,on] / 2 라운드: [on,off,on] / 3 라운드: [on,off,off]

Note:
마지막에 켜져 있기 위해서는 홀수번 toggle되어야 한다
홀수번 toggle되기 위해서는 제곱수여야 하므로, 개수는 sqrt(n)이 된다

"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)