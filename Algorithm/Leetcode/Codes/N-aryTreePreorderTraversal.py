"""

589. N-ary Tree Preorder Traversal : https://leetcode.com/problems/n-ary-tree-preorder-traversal/

N-ary tree가 하나 주어졌을 때, 해당 트리의 preorder traversal의 결과를 구하는 문제

Example:
- Input : {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
- Output : [1,3,5,6,2,4]

Note:
pre() 함수를 만들어 recursive하게 해결

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root :
            return []
        res = []
        def pre(self, node: 'Node'):
            res.append(node.val)
            if not node.children :
                return
            for child in node.children :
                pre(self, child)
        pre(self, root)
        return res