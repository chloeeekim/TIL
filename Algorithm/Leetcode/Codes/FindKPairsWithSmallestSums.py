"""

373. Find K Pairs with Smallest Sums : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

정수로 이루어진 리스트 두 개가 주어졌을 때, 각 리스트에서 값 하나씩을 뽑아 만든 pair 중 

Example:
- Input : nums1 = [1,7,11], nums2 = [2,4,6], k = 3
- Output : [[1,2],[1,4],[1,6]]

- Input : nums1 = [1,1,2], nums2 = [1,2,3], k = 2
- Output : [[1,1],[1,1]]

- Input : nums1 = [1,2], nums2 = [3], k = 3
- Output : [[1,3],[2,3]]
- 가능한 모든 pair의 개수가 k보다 작은 경우 전체를 리턴

Note:
heapq 모듈을 통해 min-heap을 사용하여 해결
heap에 push하는 과정을 조금이나마 줄이기 위해 불필요한 값(큰 값들)은 heap에 추가하지 않음
합을 기준으로 정렬하기 위해 튜플을 사용하여 heap에 push

"""

from heapq import heappush, heappop
    
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap, maxval, heapsize = [], -sys.maxsize-1, 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s = nums1[i] + nums2[j]
                if heapsize > k and s > maxval:
                    break
                heappush(heap, (s, [nums1[i], nums2[j]]))
                heapsize += 1
                if heapsize <= k:
                    maxval = max(maxval, s)
        res = []
        for i in range(k):
            if not heap:
                break
            res.append(heappop(heap)[1])
        return res