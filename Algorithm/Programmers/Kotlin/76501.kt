/*

음양 더하기 : https://school.programmers.co.kr/learn/courses/30/lessons/76501

정수들의 절댓값과 부호를 담은 배열이 주어졌을 때, 실제 정수들의 합을 구하는 문제
- 정수들의 절댓값을 담은 정수 배열 absolutes의 길이는 1 이상 1,000 이하이다
    - absolutes의 모든 수는 각각 1 이상 1,000 이하이다
- 정수들의 부호를 담은 불리언 배열 signs의 길이는 absolutes의 길이와 같다
    - signs[i]가 참이면 absolutes[i]의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미한다

Example:
- Input : absolutes=[4,7,12], signs=[true,false,true]
- Output : 9

- Input : absolutes=[1,2,3], signs=[false,false,true]
- Output : 0

Note:
signs의 값이 양수면 결과에 더하고, 음수면 결과에서 빼는 방식으로 전체 값에 대해서 계산

 */

class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        return absolutes.toTypedArray().zip(signs.toTypedArray()).sumOf { (a, sign) ->
            if (sign) a else -a
        }
    }
}