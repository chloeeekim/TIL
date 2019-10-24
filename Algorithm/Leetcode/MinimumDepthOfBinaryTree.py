"""

111. Minimum Depth of Binary Tree : https://leetcode.com/problems/minimum-depth-of-binary-tree/

binary tree가 주어졌을 때, 해당 트리의 minimum depth를 구하는 문제
- root에서부터 leaf 노드까지의 가장 짧은 길이
- leaf 노드는 자식 노드가 없는 노드
- root 노드의 depth는 1이다

Example:
- Input : [3,9,20,null,null,15,7]
- Output : 2

Note:
queue를 사용하여 level order로 순회
level(depth)를 [node, level]의 형태로 queue에서 관리

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        res = -1
        queue = [[root, 1]]
        while queue :
            temp = queue.pop(0)
            node, level = temp[0], temp[1]
            if res != -1 and level >= res :
                break
            if not node.left and not node.right :
                res = (min(res, level) if res != -1 else level)
            if node.left :
                queue.append([node.left, level + 1])            
            if node.right :
                queue.append([node.right, level + 1])
        return res