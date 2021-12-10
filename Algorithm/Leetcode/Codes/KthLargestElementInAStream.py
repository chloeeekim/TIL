"""

703. Kth Largest Element in a Stream : https://leetcode.com/problems/kth-largest-element-in-a-stream/

stream의 형태로 숫자가 주어질 때, k번째로 큰 숫자를 구하는 문제
- KthLargest(int k, int[] nums)는 초기 숫자 리스트와 k를 초기화하는 함수이다
- int add(int val)로 숫자 val가 주어지며, 해당 숫자를 포함하여 k번째로 큰 숫자를 리턴한다

Example:
- Input : ["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
- Output : [null, 4, 5, 5, 8, 8]

Note:
리스트의 길이를 항상 최대 k로 유지하여 k번째보다 작은 경우에는 정렬을 하지 않는 방식
참고) 좀 더 효율적인 방법? 힙을 이용하면 빠를 듯

"""

class KthLargest(object):
    
    k = 0
    nums = []
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) > 1 and val <= self.nums[-1]:
            return self.nums[-1]
        else:
            self.nums.append(val)
            self.nums = sorted(self.nums, reverse=True)[:self.k]
            return self.nums[-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)