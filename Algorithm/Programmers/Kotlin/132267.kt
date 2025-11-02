/*

콜라 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/132267

일반화된 콜라 문제가 주어졌을 때, 받을 수 있는 콜라의 병 수를 구하는 문제
- 콜라 문제는 다음과 같다
    - 콜라 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있다
    - 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산한다
    - 단, 보유 중인 빈 병이 a개 미만이라면 콜라를 받을 수 없다
- a, b, n은 각각 1 <= b < a <= n <= 1,000,000을 만족하는 정수이다
- 정답은 항상 int 범위를 넘지 않게 주어진다

Example:
- Input : a=2, b=1, n=20
- Output : 19

- Input : a=3, b=1, n=20
- Output : 9

Note:
현재 가지고 있는 콜라 병의 개수는 n이므로, 마트에 줄 수 있는 a개 묶음의 콜라는 n // a, 남은 개수는 n % a가 된다
받아오는 콜라는 (n // a) * b이므로, 이전에 남은 콜라의 개수와 더하여 위 과정을 반복한다

 */

class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer = 0
        var remain = n
        while (remain >= a) {
            val give = (remain / a) * b
            remain = give + (remain % a)
            answer += give
        }
        return answer
    }
}