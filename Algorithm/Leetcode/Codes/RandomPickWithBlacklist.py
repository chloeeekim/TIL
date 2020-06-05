"""

710. Random Pick with Blacklist : https://leetcode.com/problems/random-pick-with-blacklist/

blacklist가 주어졌을 때, [0,N) 범위에서 랜덤하게 숫자 하나를 리턴하는 메소드를 구현하는 문제
- N은 1 이상 1000000000 이하이다
- blacklist B의 길이는 0 이상 min(100000, N) 이하이다 (blacklist가 존재하지 않을 수 있다)
- [0,N) 범위는 N을 포함하지 않는다

Example:
- Input :
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
- Output : [null,0,0,0]

- Input :
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
- Output : [null,1,1,1]

- Input :
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
- Output : [null,0,0,2]

- Input :
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
- Output : [null,1,3,1]

Note:
blacklist의 크기에 따라 self.list를 다르게 설정하는 방식으로 해결
blacklist가 작고 N이 굉장히 큰 경우 모든 값이 전부 blacklist에 포함되어 있는지를 일일이 확인 후 list를 생성하는 것이 오버헤드
따라서 range(N)으로 blacklist까지 포함하도록 한 후, pick 시에 blacklist에 포함된 값이면 다시 pick한다
blacklist의 크기가 크다면 pick 시에 blacklist에 포함된 값이 아예 안 나오는 것이 효율적이므로 값이 모두 blacklist에 포함되어 있는지를 확인 후 list를 생성
N의 1/4 이상이 blacklist라면 후자의 방법을 사용하도록 구현

"""

import random

class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        self.blacklist = set(blacklist)
        self.black = len(self.blacklist) > N//4
        self.list = [x for x in range(N) if x not in self.blacklist] if self.black else range(N)
        self.choices = random.choices(self.list, k=1000)

    def pick(self) -> int:
        while True:
            if not self.choices:
                self.choices = random.choices(self.list, k=1000)
            temp = self.choices.pop()
            if self.black or temp not in self.blacklist:
                return temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()