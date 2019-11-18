"""

173. Binary Search Tree Iterator : https://leetcode.com/problems/binary-search-tree-iterator/

binary search tree가 주어졌을 때, 해당 트리를 가장 작은 순서부터 순회하는 함수를 작성하는 문제
- next() : 다음으로 가장 작은 숫자를 리턴
- hasNext() : 다음 값이 있는지를 리턴
- next는 항상 valid한 경우에만 호출된다고 가정한다

Example:
- Input : ["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"], [[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]
- Output : [null,3,7,true,9,true,15,true,20,false]

Note:
한 번 bst가 생성된 이후 next와 hasNext가 여러번 호출되는 구조이므로, __init__에서 bst를 순회한 리스트를 생성

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.idx = -1
        self.bst = []
        def getbst(self, node: TreeNode) :
            if node.left :
                getbst(self, node.left)
            self.bst.append(node.val)
            if node.right :
                getbst(self, node.right)
        if root :
            getbst(self, root)
        self.length = len(self.bst) - 1

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.idx += 1
        return self.bst[self.idx]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.idx < self.length

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()