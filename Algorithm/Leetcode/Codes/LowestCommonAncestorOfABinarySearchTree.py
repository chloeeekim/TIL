"""

235. Lowest Common Ancestor of a Binary Search Tree : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

BST와 두 개의 노드가 주어졌을 때, 두 노드의 LCA(lowest common ancestor)를 구하는 문제
- LCA란 두 개의 노드 p와 q의 공통 부모이자 가장 아래 레벨에 위치한 노드를 의미한다

Example:
- Input : [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
- Output : 6

- Input : [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
- Output : 2
- LCA로는 자기 자신도 될 수 있다

Note:
solve() 함수를 생성하여 recursive하게 해결
방문한 노드가 자기 자신인 경우 무조건 LCA가 되며,
해당 노드에서 양 옆으로 갈라지는 경우에도 무조건 LCA가 된다
q가 무조건 p보다 크다는 조건이 없으므로 함수 호출 전에 비교

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(self, node: 'TreeNode', p: int, q: int) -> 'TreeNode':
            tmp = None
            if node.val == p or node.val == q :
                return node
            elif node.val > p and node.val < q :
                return node
            else :
                nxt = node.right if node.val < p else node.left
                return solve(self, nxt, p, q)
        s = p.val if p.val < q.val else q.val
        l = p.val if p.val > q.val else q.val
        return solve(self, root, s, l)