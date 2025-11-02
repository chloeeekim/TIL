/*

로또의 최고 순위와 최저 순위 : https://school.programmers.co.kr/learn/courses/30/lessons/77484

구매한 로또 번호와 당첨 번호가 주어졌을 때, 당첨 가능한 최고 순위와 최저 순위를 구하는 문제
- 로또 순위는 6개 모두 일치 시 1위, 5개 일치 시 2위, ... , 2개 일치 시 5위, 그 외에는 6위이다
- 구매한 로또 번호 중 알아볼 수 없는 번호는 0으로 표기한다
- 순서와 상관없이 구매한 로또에 당첨 번호와 일치하는 번호가 있다면 맞힌 것으로 인정된다
- lottos에 0을 제외한 다른 숫자들은 중복이 없으며, 정렬되어 있지 않을 수 있다
- win_nums에는 중복이 없으며, 정렬되어 있지 않을 수 잇다

Example:
- Input : lottos=[44, 1, 0, 0, 31, 25], win_nums=[31, 10, 45, 1, 6, 19]
- Output : [3, 5]

- Input : lottos=[0, 0, 0, 0, 0, 0], win_nums=[38, 19, 20, 40, 15, 25]
- Output : [1, 6]

- Input : lottos=[45, 4, 35, 20, 3, 9], win_nums=[20, 9, 3, 45, 4, 35]
- Output : [1, 1]

Note:
최고 순위는 0이 전부 다 당첨 번호인 경우
최저 순위는 0이 전부 다 당첨 번호가 아닌 경우
순위는 최고 6(낙첨)까지밖에 없으므로 coerceAtMost로 최대 6으로 값 제한

 */

class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        val zeros = lottos.count { it == 0 }
        val match = lottos.count { it in win_nums }

        return intArrayOf(
            (7 - zeros - match).coerceAtMost(6),
            (7 - match).coerceAtMost(6)
        )
    }
}