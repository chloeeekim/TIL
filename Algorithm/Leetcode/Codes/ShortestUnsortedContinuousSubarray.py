"""

581. Shortest Unsorted Continuous Subarray : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

정수로 이루어진 array가 주어졌을 때, 증가순으로 정렬하면 전체 리스트로 정렬이 되는 continuous subarray의 길이를 찾는 문제
- 입력 array의 길이는 [1,10000] 범위이다
- 입력 array는 중복이 존재할 수 있다. 즉, ascending order란 <= 를 의미한다

Example:
- Input : [2,6,4,8,10,9,15]
- Output : 5
- [6,4,8,10,9]를 정렬하면 전체 array도 정렬된다

Note:
양쪽 끝에서부터 정렬되지 않은 부분을 구하는 방식
continuous subarray를 구하는 문제이므로, 중간 부분이 정렬되어 있더라도 subarray에 포함되어야 한다

"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums, bottom, top = sorted(nums), 0, len(nums) - 1
        while nums[bottom] == snums[bottom] and bottom < top :
            bottom += 1
        if bottom == top :
            return 0
        while nums[top] == snums[top] :
            top -= 1
        return top - bottom + 1