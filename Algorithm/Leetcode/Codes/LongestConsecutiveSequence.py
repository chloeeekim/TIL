"""

128. Longest Consecutive Sequence : https://leetcode.com/problems/longest-consecutive-sequence/

정렬되지 않은 정수로 이루어진 array가 주어졌을 때, 연속적인 수로 만들 수 있는 가장 긴 sequence의 길이를 구하는 문제
- Your algorithm should run in O(n) complexity

Example:
- Input : [100, 4, 200, 1, 3, 2]
- Output : 4
- longest consecutive elements sequence는 [1,2,3,4]

Note:
중복을 제거하기 위해 set 사용
하나의 sequence를 여러 번 체크하게 되면 비효율적이므로, 해당 sequence에서 가장 작은 값일 때(num-1이 없을 때)만 확인
1씩 더해가면서 최종 길이를 구한다

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, res = set(nums), 0
        for num in nums :
            if num - 1 not in nums :
                mnum = num
                while mnum + 1 in nums :
                    mnum += 1
                res = max(res, mnum - num + 1)
        return res