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
- Solution 1
리스트를 순회하면서 x와의 거리를 기준으로 정렬하기 위해 [거리, 값]의 형식으로 list에 append
이를 정렬하게 되면 거리가 동일한 경우 값을 기준으로 오름차순으로 정렬되므로 조건을 만족
결과 리스트도 오름차순으로 정렬하여 리턴
- Solution 2
주어진 리스트가 정렬되어 있으므로 sliding window 방식으로 해결 가능
원소가 반복되며 k 값이 작은 경우에 오답을 피하기 위해 양쪽 원소의 값이 동일한 경우는 고려하지 않고 넘어감
거리가 동일한 경우에 작은 값을 선택하기 위해서 왼쪽 원소의 거리가 오른쪽 원소의 거리와 동일한 경우에도 왼쪽을 선택

"""

# Solution 1

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp, res = [], []
        for num in arr:
            temp.append([abs(num-x), num])
        temp.sort()
        for i in range(k):
            res.append(temp[i][1])
        return sorted(res)

# Solution 2

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        length = len(arr)
        for left in range(len(arr)-k):
            right = left+k
            if arr[left] == arr[right]:
                continue
            if abs(arr[left]-x) <= abs(arr[right]-x):
                return arr[left:right]
        return arr[length-k:]