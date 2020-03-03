"""

155. Min Stack : https://leetcode.com/problems/min-stack/

주어진 함수를 포함하는 stack을 만드는 문제
- push(x), pop(), top(), getMin() 네 가지 함수를 만들어야 한다

Example:
- Input : ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]
- Output : [null,null,null,null,-3,null,0,-2]

Note:
getMin 함수에서 소요 시간이 오래 걸려 최소값을 저장하는 리스트를 따로 관리
stack의 특성 상 요소가 제거되더라도(pop) min 리스트를 업데이트 해 줄 필요가 없음

"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """        
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min :
            self.min.append(x)
        else :
            self.min.append(min(self.min[-1], x))
        
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()