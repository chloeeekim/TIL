"""

119. Pascal's Triangle II : https://leetcode.com/problems/pascals-triangle-ii/

양의 정수인 rowIndex가 주어졌을 때,
파스칼의 삼각형(Pascal's Triangle)에서 rowIndex번째를 구하는 문제
- 파스칼의 삼각형: 각 숫자는 위의 두 숫자의 합으로 이루어진다

Example:
- Input : 3
- Output : [1,3,3,1]
- [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]의 형태

Note:
메모리 O(n)만큼 사용
해당 인덱스의 값은 이전 사이클의 (해당 인덱스의 값 + 앞 인덱스의 값)
앞에서부터 순서대로 계산하려면 여분의 공간이 필요하므로 뒤에서부터 계산하는 방식 선택

"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0 for _ in range(rowIndex + 1)]
        row[0] = 1
        for i in range(rowIndex+1) :            
            for j in range(i-1, -1, -1) :
                row[j+1] += row[j]
        return row