"""

977. Squares of a Sorted Array : https://leetcode.com/problems/squares-of-a-sorted-array/

정수로 이루어진 리스트 A가 주어졌을 때, 각 원소들의 제곱을 non-decreasing order로 정렬하는 문제
- A의 길이는 1 이상 10000 이하이다
- A에 포함된 원소들은 -10000 이상 10000 이하이다
- A는 non-decreasing order로 정렬되어 있다

Example:
- Input : [-4,-1,0,3,10]
- Output : [0,1,9,16,100]

- Input : [-7,-3,2,3,11]
- Output : [4,9,9,49,121]

Note:
각 원소의 제곱을 구한 리스트를 정렬하는 방식
참고) two pointer로 풀어볼 것

"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x*x for x in A])