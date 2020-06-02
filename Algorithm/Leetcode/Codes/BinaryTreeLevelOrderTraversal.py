"""

102. Binary Tree Level Order Traversal : https://leetcode.com/problems/binary-tree-level-order-traversal/

binary tree가 하나 주어졌을 때, 해당 트리의 level order traversal의 결과를 구하는 문제
- 왼쪽에서 오른쪽 순서로 순회하며, 레벨별로 나타내어야 한다

Example:
- Input : [3,9,20,null,null,15,7]
- Output : [[3],[9,20],[15,7]]

Note:
- Solution 1
queue를 사용하여 해결
해당 노드의 레벨을 확인하기 위하여 queue에서 [node, level]의 형태로 관리
- Solution 2
queue를 사용하여 해결
각 레벨별로 tqueue와 tnodes 리스트를 두어 한 레벨이 끝날 때마다 queue와 결과 리스트를 갱신하는 방식

"""

# Solution 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        res = [[]]
        queue = [[root, 0]]
        while queue :
            temp = queue.pop(0)
            node, level = temp[0], temp[1]
            if len(res) <= level :
                res.append([node.val])
            else :
                res[level].append(node.val)            
            if node.left :
                queue.append([node.left, level + 1])
            if node.right :
                queue.append([node.right, level + 1])
        return res

# Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue, tqueue, tnodes = [root], [], []
        while queue:
            node = queue.pop(0)
            tnodes.append(node.val)
            if node.left:
                tqueue.append(node.left)
            if node.right:
                tqueue.append(node.right)
            if not queue:
                res.append(tnodes)
                queue, tqueue, tnodes = tqueue, [], []
        return res