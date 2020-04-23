"""

658. Find K Closest Elements : https://leetcode.com/problems/find-k-closest-elements/

하나의 정렬된 리스트와 정수 k, x가 주어졌을 때, x에 가까운 k개의 원소를 찾는 문제
- 결과는 오름차순으로 정렬하여 나타내어야 한다
- 만약 x로부터의 거리가 동일한 경우가 있다면, 항상 숫자가 작은 쪽을 택한다

Example:
- Input : [1,2,3,4,5], k=4, x=3
- Output : [1,2,3,4]
- 1과 5 중에서 작은 수를 선택

- Input : [1,2,3,4,5], k=4, x=-1
- Output : [1,2,3,4]

Note:
리스트를 순회하면서 x와의 거리를 기준으로 정렬하기 위해 [거리, 값]의 형식으로 list에 append
이를 정렬하게 되면 거리가 동일한 경우 값을 기준으로 오름차순으로 정렬되므로 조건을 만족
결과 리스트도 오름차순으로 정렬하여 리턴

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp, res = [], []
        for num in arr:
            temp.append([abs(num-x), num])
        temp.sort()
        for i in range(k):
            res.append(temp[i][1])
        return sorted(res)