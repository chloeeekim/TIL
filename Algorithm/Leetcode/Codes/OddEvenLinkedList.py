"""

328. Odd Even Linked List : https://leetcode.com/problems/odd-even-linked-list/

Linked list가 주어졌을 때, 홀수번째와 짝수번째 노드들끼리 재구성하는 문제
- O(1) extra space complexity와 O(n) time complexity를 만족해야 한다

Example:
- Input : head = [1,2,3,4,5]
- Output : [1,3,5,2,4]

- Input : head = [2,1,3,5,6,4,7]
- Output : [2,3,6,7,1,5,4]

Note:
linked list를 순회하면서 각 순서대로 odd와 even 리스트에 추가하고,
최종적으로 odd 리스트의 마지막에 even 리스트를 연결

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        even, odd_start, odd = head, head.next, head.next
        while (odd and odd.next) and (even and even.next):
            even.next = odd.next
            even = odd.next
            
            if even:
                odd.next = even.next
                odd = even.next
            else:
                odd.next = None
                odd = None
        even.next = odd_start
        return head