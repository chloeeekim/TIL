"""

896. Monotonic Array : https://leetcode.com/problems/monotonic-array/

숫자로 이루어진 list가 주어졌을 때, 해당 리스트가 monotonic array인지 확인하는 문제
- monotonic increasing하거나 monotonic decreasing하는 경우 monotonic array이다
- monotonic increasing: 모든 i, j에 대해 i <= j, A[i] <= A[j]를 만족
- monotonic decreasing: 모든 i, j에 대해 i <= j, A[i] >= A[j]를 만족
- A의 길이는 1 이상 50000 이하이다
- A에 포함된 숫자의 범위는 -100000 이상 100000 이하이다

Example:
- Input : [1,2,2,3]
- Output : true

- Input : [6,5,4,4]
- Output : true

- Input : [1,3,2]
- Output : false

- Input : [1,2,4,5]
- Output : true

- Input : [1,1,1]
- Output : true

Note:
리스트를 순회하면서 증가하면 increasing을 true로, 감소하면 decreasing을 true로 두고
increasing과 decreasing이 모두 포함되는지를 확인
둘 다 true라면 monotonic array가 아니다

"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                increasing = True
            elif A[i] < A[i-1]:
                decreasing = True
            if increasing and decreasing:
                return False
        return True