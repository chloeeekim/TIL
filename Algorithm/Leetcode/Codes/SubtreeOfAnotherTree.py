""

572. Subtree of Another Tree : https://leetcode.com/problems/subtree-of-another-tree/

root와 subRoot, 두 트리가 주어졌을 때 subRoot 트리가 root 트리의 subtree인지 확인하는 문제
- 자기 자신 또한 subtree이다

Example:
- Input : root = [3,4,5,1,2], subRoot = [4,1,2]
- Output : true

- Input : root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
- Output : false

Note:
recursive하게 해결
isSame 함수를 생성하여 주어진 두 노드가 동일한지 확인
isSubtree 함수 또한 recursive하게 방문

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return isSame(s.left, t.left) and isSame(s.right, t.right)
        if not t:
            return True
        if not s:
            return False
        return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)