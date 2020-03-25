"""

61. Rotate List : https://leetcode.com/problems/rotate-list/

linked list가 하나 주어졌을 때, 이를 오른쪽으로 k번 회전한 결과를 구하는 문제
- k는 음수가 아니다

Example:
- Input : 1->2->3->4->5->NULL, k = 2
- Output : 4->5->1->2->3->NULL

- Input : 0->1->2->NULL, k = 4
- Output : 2->0->1->NULL

Note:
dict를 사용하여 각 노드의 순서 정보를 저장
k가 0이거나 linked list 길이의 배수라면 회전하지 않으므로 그대로 리턴
k가 0이 아닌 경우 필요한 인덱스의 노드를 seen에서 찾아서 연결
cycle이 있으면 안 되므로 새로운 head node로 연결되는 부분은 끊어줌

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        count, seen, node = 0, {}, head
        if not head :
            return head
        while node :
            count += 1
            seen[count] = node
            node = node.next
        k = k % count
        if k == 0:
            return head
        res = seen[count - k + 1]
        seen[count].next = seen[1]
        seen[count - k].next = None
        return res