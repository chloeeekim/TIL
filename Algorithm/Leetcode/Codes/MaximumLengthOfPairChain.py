"""

646. Maximum Length of Pair Chain : https://leetcode.com/problems/maximum-length-of-pair-chain/

두 개의 숫자로 이루어진 n개의 pair가 주어졌을 때, 만들 수 있는 chain의 최대 길이를 구하는 문제
- 모든 pair는 첫 번째 숫자가 두 번째 숫자보다 작다
- b < c인 경우에 (a,b)와 (c,d)를 chain으로 연결할 수 있다
- 주어지는 pair의 개수는 [1,1000] 범위이다

Example:
- Input : [[1,2], [2,3], [3,4]]
- Output : 2
- [1,2] -> [3,4]

Note:
dp로 해결했을 때 생각보다 속도가 느렸다..
첫 번째 숫자를 기준으로 정렬하는 경우, 두 번째 숫자가 크다면 chain을 길게 만들 수 없으므로
두 번째 숫자를 기준으로 정렬하여 greedy한 방식으로 해결

"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs, before, count = sorted(pairs, key=(lambda x:x[1])), -sys.maxsize, 0
        print(pairs)
        for i in range(len(pairs)):
            if pairs[i][0] > before:
                before = pairs[i][1]
                count += 1
        return count