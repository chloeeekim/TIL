/*

멀쩡한 사각형 : https://school.programmers.co.kr/learn/courses/30/lessons/62048

가로 길이가 W, 세로 길이가 H인 직사각형을 대각선으로 잘랐을 때, 사용할 수 있는 정사각형의 개수를 구하는 문제
- 모든 격자칸은 1cm x 1cm이다
- 잘라진 종이에서 원래 종이의 가로, 세로 방향과 평행하게 1cm x 1cm로 잘라 사용할 수 있는 칸을 구한다
- W, H는 1억 이하의 자연수이다

Example:
- Input : W=8, H=12
- Output : 80

Note:
입출력 예시 그림을 살펴보면, 사용할 수 없는 정사각형에 일정한 패턴이 발견
기존 사각형이 8 x 12인 경우, 2 x 3 크기의 사각형에서 잘리는 정사각형의 개수가 4개인 패턴이 반복
여기서 4는 8과 12의 최대 공약수이며, 2와 3은 서로소 관계
이걸 발전시켜 잘리는 사각형의 개수가 w + h - gcd(w, h)임을 계산 가능
gcd는 유클리드 호제법을 사용하여 구현

 */

class Solution {
    fun solution(w: Int, h: Int): Long {
        val wLong = w.toLong()
        val hLong = h.toLong()

        val total = wLong * hLong
        val erase = wLong + hLong - gcd(wLong, hLong)
        return total - erase
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val temp = y
            y = x % y
            x = temp
        }
        return x
    }
}