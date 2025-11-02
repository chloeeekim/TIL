/*

삼총사 : https://school.programmers.co.kr/learn/courses/30/lessons/131705

학생들의 번호가 주어졌을 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 구하는 문제
- 학생 3명의 정수 번호를 더했을 때 0이 되면 삼총사라고 한다
- 학생들의 번호를 나타내는 정수 배열 number의 길이는 3 이상 13 이하이다
    - number의 원소는 -1,000 이상 1,000 이하이다
    - 서로 다른 학생의 정수 번호가 같을 수 있다

Example:
- Input : number=[-2, 3, 0, 2, -5]
- Output : 2

- Input : number=[-3, -2, -1, 0, 1, 2, 3]
- Output : 5

- Input : number=[-1, 1, -1, 1]
- Output : 0

Note:
두 학생의 정수 번호가 각각 i, j라면 (i + j) * -1이 다른 학생의 정수 번호라면 삼총사가 된다
문제에서 서로 다른 학생의 정수 번호가 같을 수 있다고 하였으므로, 해당하는 정수 번호가 몇 번 나오는지 카운트하여 정답에 더한다

 */

class Solution {
    fun solution(number: IntArray): Int {
        var answer = 0
        val size = number.size

        for (i in 0 until size - 2) {
            for (j in i + 1 until size - 1) {
                val target = -(number[i] + number[j])
                answer += (j + 1 until size).count { number[it] == target }
            }
        }

        return answer
    }
}