"""

697. Degree of an Array : https://leetcode.com/problems/degree-of-an-array/

양수로만 이루어진 비어 있지 않은 리스트가 주어졌을 때, 해당 리스트의 degree와 동일한 가장 작은 subarray의 길이를 구하는 문제
- degree란 가장 많이 등장하는 원소의 frequency이다
- 주어지는 nums의 길이는 1부터 50,000 사이이다
- nums[i]는 0부터 49,999까지이다

Example:
- Input : nums = [1,2,2,3,1]
- Output : 2
- 1과 2가 각각 2번씩 나타나므로 degree는 2가 된다
degree가 2인 subarray는 [1,2,2,3,1], [1,2,2,3], [2,2,3,1], [1,2,2], [2,2,3], [2,2] 이므로 가장 짧은 subarray의 길이는 2이다

- Input : nums = [1,2,2,3,1,4,2]
- Output : 6
- 2가 3번 나타나므로 degree는 3이 된다
degree가 3인 subarray는 [1,2,2,3,1,4,2], [2,2,3,1,4,2] 이므로 갖ㅇ 짧은 subarray의 길이는 6이다

Note:
defaultdict를 사용하여 특정 값의 인덱스를 시작부터 끝까지 추가
주어진 nums 리스트의 degree를 구한 다음, 해당 degree와 동일한 값의 첫 번째와 마지막 인덱스를 통해 최소 subarray의 길이를 구한다

"""

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count, degree = defaultdict(list), 0
        for i in range(len(nums)):
            count[nums[i]].append(i)
        for j in count:
            degree = max(degree, len(count[j]))
        ans = sys.maxsize
        for i in count:
            if len(count[i]) == degree:
                ans = min(ans, count[i][-1] - count[i][0]+1)
        return ans