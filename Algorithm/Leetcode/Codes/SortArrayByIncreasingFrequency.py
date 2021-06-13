"""

1636. Sort Array by Increasing Frequency : https://leetcode.com/problems/sort-array-by-increasing-frequency/

nums 리스트가 주어졌을 때, 숫자를 출현 빈도에 따라 오름차순으로 정렬하는 문제
- 출현 빈도가 동일한 경우, 내림차순으로 정렬한다

Example:
- Input : nums = [1,1,2,2,2,3]
- Output : [3,1,1,2,2,2]

- Input : nums = [2,3,1,3,2]
- Output : [1,3,3,2,2]
- 2와 3의 출현 빈도가 동일하므로, 내림차순으로 정렬

- Input : nums = [-1,1,-6,4,5,-6,1,4,1]
- Output : [5,-1,4,4,-6,-6,1,1,1]

Note:
각 숫자의 출현 빈도를 dict에 저장
sorted와 lambda를 사용하여 우선 key를 내림차순으로 정렬한 후
value(frequency) 값을 기준으로 오름차순으로 정렬
sorted의 결과는 리스트임을 기억하자...

"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count, res = {}, []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        dec = sorted(count.items(), reverse=True, key=lambda x: x[0])
        fre = sorted(dec, key=lambda x: x[1])
        for key, val in fre:
            res += [key]*val
        return res