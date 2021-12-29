"""

347. Top K Frequent Elements : https://leetcode.com/problems/top-k-frequent-elements/

정수로 이루어진 리스트 nums와 정수 k가 주어졌을 때, 가장 많이 등장하는 k번째까지의 숫자를 구하는 문제
- 결과는 어떤 순서로 리턴하건 상관없다
- 정답은 unique하다는 것이 보장된다
- k는 1부터 리스트 nums의 unique elements의 개수까지로 주어진다

Example:
- Input : nums = [1,1,1,2,2,3], k = 2
- Output : [1,2]

- Input : nums = [1], k = 1
- Output : [1]

Note:
dict를 사용하여 등장하는 개수를 확인
lambda를 사용하여 key가 아닌 value로 정렬

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        seen = sorted(seen.items(), key = lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(seen[i][0])
        return ans