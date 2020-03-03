"""

300. Longest Increasing Subsequence : https://leetcode.com/problems/longest-increasing-subsequence/

정렬되지 않은 숫자가 포함된 list가 주어졌을 때, longest increasing subsequence의 길이를 구하는 문제

Example:
- Input : [10,9,2,5,3,7,101,18]
- Output : 4
- lis는 [2,3,7,101]

Note:
해당 숫자가 마지막이 되는 lis의 길이를 seen으로 저장
다음 숫자의 경우 자신보다 작은 숫자의 lis의 길이 중 가장 큰 것에 +1
참고) 더 빠른 방법?

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums :
            return 0
        maxlen, seen = 1, {nums[0]: 1}
        for i in nums :
            tempmax = 0
            for j in seen :
                if i > j :
                    tempmax = max(tempmax, seen[j])
            seen[i] = tempmax + 1
            maxlen = max(maxlen, seen[i])
        return maxlen