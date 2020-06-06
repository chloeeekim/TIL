"""

406. Queue Reconstruction by Height : https://leetcode.com/problems/queue-reconstruction-by-height/

(h, k)의 형태로 주어지는 리스트를 다음 조건에 맞게 재정렬하는 문제
- h는 해당 사람의 키이다
- k는 해당 사람보다 앞에 위치한 키가 같거나 큰 사람의 수이다
- 주어지는 리스트의 길이는 1100을 넘지 않는다

Example:
- Input : [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
- Output : [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Note:
k가 가능한 범위가 아닌 정확한 숫자임을 이용
키가 작은 사람은 앞에 위치하더라도 키가 큰 사람에게 영향을 주지 않으므로 키가 큰 순서대로 배치
해당 사람을 배치하게 될 때 결과 리스트에는 키가 크거나 같은 사람만 존재하므로, k번째에 배치하면 된다

"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for person in people:
            res.insert(person[1], person)
        return res