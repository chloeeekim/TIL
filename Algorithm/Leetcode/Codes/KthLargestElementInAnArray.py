"""

215. Kth Largest Element in an Array : https://leetcode.com/problems/kth-largest-element-in-an-array/

숫자로 이루어진 정렬되지 않은 리스트가 주어졌을 때, k번째로 큰 숫자를 구하는 문제

Example:
- Input : [3,2,1,5,6,4], k = 2
- Output : 5

- Input : [3,2,3,1,2,4,5,5,6], k = 4
- Output : 4

Note:
reverse=True 옵션을 준 경우 역순으로 정렬
sort에 reverse=True 옵션을 주지 않은 경우에는 return nums[-k]

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]