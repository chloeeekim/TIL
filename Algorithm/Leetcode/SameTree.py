"""

100. Same Tree : https://leetcode.com/problems/same-tree/

binary tree가 두 개 주어졌을 때, 두 트리가 동일한 트리인지 확인하는 문제
- 동일한 트리의 조건 : 구조가 동일하고, 각 노드의 값이 동일

Example:
- Input : [1,2,3], [1,2,3]
- Output : true

- Input : [1,2], [1,null,2]
- Output : false

- Input : [1,2,1], [1,1,2]
- Output : false

Note:
isSameNode() 함수를 만들어 각 노드를 비교
1. 노드가 둘 다 None인 경우 true (동일)
2. 노드 중 하나만 None인 경우 false (다름)
3. 노드가 둘 다 None이 아니고, 값이 같은 경우, left와 right를 비교
4. 노드가 둘 다 None이 아니고, 값이 다른 경우 false (다름)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSameNode(self, p: TreeNode, q: TreeNode) -> bool:
            if not p and not q :
                return True
            elif (not p and q) or (p and not q) :
                return False
            else :
                if p.val == q.val :
                    return isSameNode(self, p.left, q.left) and isSameNode(self, p.right, q.right)
                else :
                    return False
        return isSameNode(self, p, q)