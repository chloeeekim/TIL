"""

590. N-ary Tree Postorder Traversal : https://leetcode.com/problems/n-ary-tree-postorder-traversal/

N-ary tree가 하나 주어졌을 때, 해당 트리의 postorder traversal의 결과를 구하는 문제

Example:
- Input : {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
- Output : [5,6,3,2,4,1]

Note:
post() 함수를 만들어 recursive하게 해결
preorder와 함수 호출 순서만 변경

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:        
        if not root :
            return []
        res = []
        def post(self, node: 'Node'):
            if not node.children :
                res.append(node.val)
                return
            for child in node.children :
                post(self, child)            
            res.append(node.val)
        post(self, root)
        return res