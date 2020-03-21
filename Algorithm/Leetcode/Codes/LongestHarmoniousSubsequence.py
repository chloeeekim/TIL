"""

594. Longest Harmonious Subsequence : https://leetcode.com/problems/longest-harmonious-subsequence/

정수가 포함된 array가 주어졌을 때, 가장 긴 harmonious subsequence의 길이를 구하는 문제
- harmonious subsequence란 가장 큰 값과 가장 작은 값의 차이가 정확히 1인 subsequence를 의미한다

Example:
- Input : [1,3,2,2,5,2,3,7]
- Output : 5
- longest harmonious subsequence는 [3,2,2,2,3]

Note:
dict 사용
리스트를 순회하며 seen에 해당 숫자가 발견된 총 개수를 저장
큰 값과 작은 값의 차이가 정확히 1이어야 하므로, 해당 숫자 +1 혹은 -1인 값을 확인하면 된다

"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        seen, res = {}, 0
        for num in nums :
            if num in seen :
                seen[num] += 1
            else :
                seen[num] = 1
            res = max(res, seen[num] + seen[num+1]) if num + 1 in seen else res
            res = max(res, seen[num] + seen[num-1]) if num - 1 in seen else res
        return res