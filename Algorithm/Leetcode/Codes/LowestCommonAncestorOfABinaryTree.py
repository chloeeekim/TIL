"""

236. Lowest Common Ancestor of a Binary Tree : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Binary Tree와 두 개의 노드가 주어졌을 때, 두 노드의 LCA(lowest common ancestor)를 구하는 문제
- LCA란 두 개의 노드 p와 q의 공통 부모이자 가장 아래 레벨에 위치한 노드를 의미한다

Example:
- Input : root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
- Output : 3

- Input : root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
- Output : 5
- LCA로는 자기 자신도 될 수 있다

Note:
solve() 함수를 생성하여 recursive하게 해결
방문한 노드의 p, q 여부와 왼쪽 서브 트리와 오른쪽 서브트리 각각의 p, q 존재 여부를 확인
셋 중 2개 이상이 True라면 해당 노드가 LCA가 된다
부모 노드로는 해당 노드를 포함한 서브트리의 p, q 여부를 return

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(node: 'TreeNode') -> bool:
            this = node.val == p.val or node.val == q.val
            left = solve(node.left) if node.left else False
            right = solve(node.right) if node.right else False
            if this+left+right >= 2:
                self.res = node
            return this or left or right
        self.res = None
        solve(root)
        return self.res