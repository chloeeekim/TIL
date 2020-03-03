"""

19. Remove Nth Node From End of List : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

linked list와 정수가 하나 주어졌을 때, list의 끝에서 n번째 노드를 지우는 문제

Example:
- Input : 1->2->3->4->5, n = 2
- Output : 1->2->3->5
- 끝에서 2번째 노드는 4

Note:
head 노드를 삭제하는 경우를 대비하여 head 노드의 앞에 노드를 하나 더 추가
list를 순회하면서 전체 노드 정보를 nodes 리스트에 저장
끝에서 n+1번째 노드의 next를 끝에서 n번째 노드의 next로 연결

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        res = ListNode(-1)
        res.next = head
        nodes, node = [], res
        while node :
            nodes.append(node)
            node = node.next
        nodes[-n-1].next = nodes[-n].next
        return res.next