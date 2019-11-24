"""

485. Max Consecutive Ones : https://leetcode.com/problems/max-consecutive-ones/

binary array가 주어졌을 때, 연속적으로 1이 등장하는 최대 길이를 구하는 문제
- 입력은 0과 1만이 포함된 array가 주어진다
- 입력의 사이즈는 10,000을 넘지 않는다

Example:
- Input : [1,1,0,1,1,1]
- Output : 3

Note:
1이 등장하는 경우 count
0이 등장하는 경우, count 값이 0이 아니라면 res 값과 비교

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums :
            if not num :
                if count :
                    res = max(res, count)
                count = 0
            else :
                count += 1
        return max(res, count)