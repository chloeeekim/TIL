"""

116. Populating Next Right Pointers in Each Node : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

binary tree가 하나 주어졌을 때, 각 노드의 next가 같은 레벨의 오른쪽 노드를 가리키도록 만드는 문제
- 해당 레벨의 마지막 포인터는 NULL(None)으로 설정되어야 한다

Example:
- Input : [1,2,3,4,5,6,7]
- Output : [1,#,2,3,#,4,5,6,7,#]

Note:
queue를 사용하여 해결
해당 노드의 레벨을 확인하기 위하여 queue에서 [node, level]의 형태로 관리
큐가 비어있지 않은 경우 다음 노드의 레벨을 확인하여 next를 연결하거나 None으로 설정

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return root
        queue = [[root, 0]]
        while queue :
            tmp = queue.pop(0)
            node, level = tmp[0], tmp[1]
            if node.left :
                queue.append([node.left, level + 1])
            if node.right :
                queue.append([node.right, level + 1])
            if not queue or queue[0][1] != level :
                node.next = None
            else :
                node.next = queue[0][0]
        return root