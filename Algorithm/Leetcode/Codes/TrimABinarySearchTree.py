"""

669. Trim a Binary Search Tree : https://leetcode.com/problems/trim-a-binary-search-tree/

BST와 바운더리 L, R이 주어졌을 때, 모든 노드가 [L,R] 범위에 있도록 BST를 trim하는 문제
- 기존 BST의 root 노드를 변경해야 할 수 있으므로, 새롭게 만들어진 트리의 root 노드를 리턴

Example:
- Input : [1,0,2], L = 1, R = 2
- Output : [1,null,2]

- Input : [3,0,4,null,2,null,null,1], L = 1, R = 3
- Output : [3,2,null,1]

Note:
solve() 함수를 생성하여 recursive하게 해결
트리를 순회하며 바운더리에서 벗어나는 경우 해당 노드의 자식 노드를 parent에 연결
BST이므로, 해당 노드의 값이 lower bound 미만이라면 왼쪽 자식 노드들도 모두 바운더리를 벗어나게 되고,
upper bound 초과라면 오른쪽 자식 노드들도 모두 바운더리를 벗어나게 된다

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        res = TreeNode(-1)
        res.right = root
        def solve(self, node: TreeNode, parent: TreeNode, isLeft: bool):
            if not node:
                return
            if node.val < L:
                if isLeft:
                    parent.left = node.right
                else:
                    parent.right = node.right
                solve(self, node.right, parent, isLeft)
                return
            if node.val > R:
                if isLeft:
                    parent.left = node.left
                else:
                    parent.right = node.left
                solve(self, node.left, parent, isLeft)
                return
            if node.left:
                solve(self, node.left, node, True)
            if node.right:
                solve(self, node.right, node, False)
        solve(self, res.right, res, False)
        return res.right