"""

257. Binary Tree Paths : https://leetcode.com/problems/binary-tree-paths/

binary tree가 하나 주어졌을 때, 해당 트리의 모든 root-to-leaf path를 구하는 문제
- leaf node는 자식 노드가 없는 노드이다

Example:
- Input : [1,2,3,null,5]
- Output : ["1->2->5", "1->3"]

Note:
getPath() 함수를 생성하여 recursive하게 해결

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root :
            return []
        res = []
        def getPath(self, node: TreeNode, path: str) :
            if not node.left and not node.right :
                res.append(path)
                return
            if node.left :
                getPath(self, node.left, path + '->' + str(node.left.val))
            if node.right :
                getPath(self, node.right, path + '->' + str(node.right.val))
        getPath(self, root, str(root.val))
        return res
            