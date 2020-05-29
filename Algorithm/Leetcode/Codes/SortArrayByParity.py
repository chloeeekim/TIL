"""

905. Sort Array By Parity : https://leetcode.com/problems/sort-array-by-parity/

음수가 아닌 숫자로 이루어진 리스트 A가 주어졌을 때, A에 속한 모든 홀수가 짝수 다음에 등장하도록 재정렬하는 문제
- A의 길이는 1 이상 5000 이하이다
- A에 포함된 숫자의 범위는 0 이상 5000 이하이다
- 조건을 만족한다면 리스트의 순서는 상관 없다

Example:
- Input : [3,1,2,4]
- Output : [2,4,3,1]
- [4,2,3,1], [2,4,1,3], [4,2,1,3] 모두 가능

Note:
- Solution 1
리스트를 순회하면서 odd, even 리스트에 각각 append하여 합치는 방식
in-place로 해결해야 하는 경우 solution 2의 방식을 사용해야 한다
- Solution 2
in-place로 해결하는 방법
리스트를 순회하며 발견되는 모든 짝수를 리스트의 앞으로 이동하는 방식

"""

# Solution 1
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd

# Solution 1-1
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = [x for x in A if x%2 != 0]
        even = [x for x in A if x%2 == 0]
        return even+odd

# Solution 2
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = -1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even += 1
                A[i], A[even] = A[even], A[i]
        return A