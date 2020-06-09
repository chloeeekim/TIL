"""

961. N-Repeated Element in Size 2N Array : https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

N+1개의 unique한 원소들이 길이가 2N인 리스트 A에 포함되어 있을 때, N번 반복되어 나타나는 원소를 찾는 문제
- A의 길이는 4 이상 10000 이하이다
- A에 포함되는 값은 0 이상 10000 미만이다
- A의 길이는 짝수이다

Example:
- Input : [1,2,3,3]
- Output : 3

- Input : [2,1,2,5,3,2]
- Output : 2

- Input : [5,1,5,2,5,3,5,4]
- Output : 5

Note:
collections의 Counter를 사용하여 리스트 내에 N번 나타나는 원소를 찾는 방식

"""

from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count, N = Counter(A), len(A)//2
        for i, num in count.items():
            if num == N:
                return i