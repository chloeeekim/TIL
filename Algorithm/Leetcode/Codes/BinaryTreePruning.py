"""

814. Binary Tree Pruning : https://leetcode.com/problems/binary-tree-pruning/

0과 1로 이루어진 binary tree가 하나 주어졌을 때, 서브트리 내에 1인 노드가 존재하지 않는 노드를 삭제하는 문제

Example:
- Input : [1,null,0,0,1]
- Output : [1,null,0,null,1]

- Input : [1,0,1,0,0,0,1]
- Output : [1,null,1,null,1]

- Input : [1,1,0,1,1,0,1,0]
- Output : [1,1,0,1,1,null,1]

Note:
pruning() 함수를 만들어 recursive하게 해결
가장 아래 노드부터 삭제 대상인지를 확인하므로, 자식 노드가 존재하는 경우에는 삭제 대상이 아니게 된다

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def pruning(self, node: TreeNode, parent: TreeNode, isLeft: bool) :
            if node.left :
                pruning(self, node.left, node, True)
            if node.right :
                pruning(self, node.right, node, False)
            if not node.left and not node.right and node.val == 0 :
                if isLeft :
                    parent.left = None
                else :
                    parent.right = None
        res = TreeNode(0)
        res.left = root
        pruning(self, root, res, True)
        return res.left