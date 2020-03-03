"""

429. N-ary Tree Level Order Traversal : https://leetcode.com/problems/n-ary-tree-level-order-traversal/

N-ary tree가 하나 주어졌을 때, 해당 트리의 level order traversal의 결과를 구하는 문제

Example:
- Input : root = [1,null,3,2,4,null,5,6]
- Output : [[1],[3,2,4],[5,6]]

- Input : root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
- Output : [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Note:
queue를 사용하여 level order로 순회하는 방식으로 해결
해당 노드의 level을 확인하기 위하여 queue에 [node, level] 형식으로 enqueue

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root :
            return []
        queue, res = [[root, 0]], []
        while len(queue) :
            temp = queue.pop(0)
            node, level = temp[0], temp[1]
            if len(res) <= level :
                res.append([node.val])
            else :
                res[level].append(node.val)
            for child in node.children :
                queue.append([child, level + 1])
        return res