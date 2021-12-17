# """
""""

341. Flatten Nested List Iterator : https://leetcode.com/problems/flatten-nested-list-iterator/

숫자로 구성된 nested list가 주어졌을 때, 하나씩 순서대로 호출하는 문제
- NestedIterator class는 3가지 함수로 이루어진다 (__init__, int next(), boolean hasNext())
- hasNext() 함수의 결과가 False인 경우 종료된다
- Nested List의 길이는 1 이상 500 이하이다

Example:
- Input : nestedList = [[1,1],2,[1,1]]
- Output : [1,1,2,1,1]

- Input : nestedList = [1,[4,[6]]]
- Output : [1,4,6]

Note:
init 함수에서 list를 전부 flat하게 만든 다음 호출하는 방식
flattenFunc 함수를 생성하여 recursive하게 list를 flatten한다

"""

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:    
    def __init__(self, nestedList: [NestedInteger]):
        def flattenFunc(self, nested, flatten):
            for n in nested:
                if n.isInteger():
                    flatten.append(n.getInteger())
                else:
                    flattenFunc(self, n.getList(), flatten)
        self.flat, self.pointer = [], -1
        flattenFunc(self, nestedList, self.flat)
                
    
    def next(self) -> int:
        return self.flat[self.pointer]
        
    
    def hasNext(self) -> bool:
        self.pointer += 1
        if len(self.flat) > self.pointer :
            return True
        else:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())