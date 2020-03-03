"""

234. Palindrome Linked List : https://leetcode.com/problems/palindrome-linked-list/

linked list가 하나 주어졌을 때, palindrome인지 확인하는 문제
- Palindrome : 회문. 거꾸로 읽었을 때도 제대로 읽었을 때와 동일한 경우

Example:
- Input : 1->2
- Output : false

- Input : 1->2->2->1
- Output : true

Note:
linked list를 순회하면서 값을 list에 저장
reverse한 리스트([::-1])와 동일한지 확인

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head :
            return True
        lst, node = [], head
        while node :
            lst.append(node.val)
            node = node.next
        return lst == lst[::-1]