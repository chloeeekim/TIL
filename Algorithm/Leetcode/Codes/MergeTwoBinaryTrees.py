"""

617. Merge Two Binary Trees : https://leetcode.com/problems/merge-two-binary-trees/

두 개의 binary tree가 주어졌을 때, 하나의 binary tree로 merge하는 문제
- binary tree를 overlapping하여 합을 구하는 문제
- 동일한 위치에 노드가 둘 다 있는 경우, 새 트리 노드의 값은 합이 된다
- 노드가 둘 다 있지 않은 경우, null 노드가 아닌 노드의 값이 된다

Example:
- Input : t1 = [1,3,2,5], t2 = [2,1,3,null,4,null,7]
- Output : [3,4,5,5,4,null,7]

Note:
merge() 함수를 생성하여 recursive하게 해결
두 트리를 동일하게 순회하면서 null 노드가 있는 경우 다른 트리의 하위 subtree를 추가

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        res = TreeNode(-1)
        def merge(self, t1: TreeNode, t2: TreeNode, parent: TreeNode, isLeft: bool) :
            if t1 and t2 :
                node = TreeNode(t1.val + t2.val)
                if isLeft :
                    parent.left = node
                else :
                    parent.right = node
                merge(self, t1.left, t2.left, node, True)
                merge(self, t1.right, t2.right, node, False)
            else :
                if isLeft :
                    parent.left = t1 if not t2 else t2
                else :
                    parent.right = t1 if not t2 else t2
        merge(self, t1, t2, res, True)
        return res.left