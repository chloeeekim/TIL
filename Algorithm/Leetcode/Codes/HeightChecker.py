"""

1051. Height Checker : https://leetcode.com/problems/height-checker/

non-decreasing 하도록 리스트를 정렬하고자 할 때, 최소한 몇 개의 원소의 위치를 옮겨야 하는지 구하는 문제
- 주어진 리스트의 길이는 1 이상 100 이하이다
- 리스트 내에 포함된 원소 값의 범위는 1 이상 100 이하이다

Example:
- Input : heights = [1,1,4,2,1,3]
- Output : 3

- Input : heights = [5,1,2,3,4]
- Output : 5

- Input : heights = [1,2,3,4,5]
- Output : 0

Note:
문제를 정확히 이해하는 데 시간이 소요되었던 문제..
결론적으로 non-decreasing한 리스트로 정렬했을 때, 제 위치에 있지 않은 원소의 개수를 구하면 된다

"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        count = 0
        for i in range(len(heights)):
            count += 1 if heights[i] != target[i] else 0
        return count