"""

21. Merged Two Sorted Lists : https://leetcode.com/problems/merge-two-sorted-lists/

두 개의 정렬된 Linked List가 주어졌을 때,
이를 정렬된 하나의 Linked List로 만드는 문제

Example:
- Input : 1->2->4, 1->3->4
- Output : 1->1->2->3->4->4

Note:
next가 None이 아닐 때까지 값 하나씩 비교
하나의 리스트가 끝나면 다른 리스트의 남은 부분을 결과 리스트의 뒤에 붙임

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        head = res
        while l1 and l2 :
            if l1.val < l2.val :
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            else :
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
        if l1 :
            head.next = l1
        if l2 :
            head.next = l2
        return res.next
