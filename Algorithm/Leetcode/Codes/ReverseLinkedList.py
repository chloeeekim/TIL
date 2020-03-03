"""

206. Reverse Linked List : https://leetcode.com/problems/reverse-linked-list/

주어진 linked list를 뒤집는 문제

Example:
- Input : 1->2->3->4->5->NULL
- Output : 5->4->3->2->1->NULL

Note:
주어진 linked list를 돌면서 새로운 linked list의 앞에 붙이는 방법으로 구현

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res, tail = ListNode(-1), None
        node = head
        while node :
            res.next = ListNode(node.val)
            res.next.next = tail
            tail = res.next
            node = node.next
        return res.next