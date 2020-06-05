"""

528. Random Pick with Weight : https://leetcode.com/problems/random-pick-with-weight/

인덱스 i에 대한 weight가 주어졌을 때, weight에 따라 랜덤하게 숫자 하나를 리턴하는 메소드를 구현하는 문제
- 주어지는 weight 리스트의 길이는 1 이상 10000 이하이다
- weight 값은 1 이상 100000 이하이다
- pickIndex는 최대 10000번 호출된다

Example:
- Input :
["Solution","pickIndex"]
[[[1]],[]]
- Output : [null,0]

- Input :
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
- Output : [null,0,1,1,1,0]
- 출력되는 값의 비율이 유지되면 되므로, [null,0,1,1,1,1]과 같은 경우에도 답이 된다

Note:
가중치만큼의 범위를 지정하여 해당 범위에 속하면 해당 인덱스의 값을 리턴
참고) 더 빠른 방법?

"""

import random

class Solution:
    def __init__(self, w: List[int]):
        self.list, tsum, self.len = [], 0, len(w)
        for weight in w:
            tsum += weight
            self.list.append(tsum)
        self.total = tsum

    def pickIndex(self) -> int:
        pick = self.total*random.random()
        for i, weight in enumerate(self.list):
            if weight > pick:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()