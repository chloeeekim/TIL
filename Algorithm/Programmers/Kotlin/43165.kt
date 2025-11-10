/*

타겟 넘버 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

n개의 음이 아닌 정수들이 주어졌을 때, 정수들의 순서를 변경하지 않고 더하거나 빼서 타겟 넘버를 만드는 방법의 수를 구하는 문제
- 사용할 수 있는 숫자가 담긴 배열 numbers의 길이는 2 이상 20 이하이다
    - 각 숫자는 1 이상 50 이하인 자연수이다
- 타겟 넘버 target은 1 이상 1000 이하인 자연수이다

Example:
- Input : numbers=[1, 1, 1, 1, 1], target=3
- Output : 5

- Input : numbers=[4, 1, 2, 1], target=4
- Output : 2

Note:
주어지는 숫자의 개수가 최대 20개이므로, 모든 경우의 수를 구하여 확인
products 함수를 생성하여 backtrack 방식으로 경우의 수를 구한다

 */

class Solution {
    fun solution(numbers: IntArray, target: Int): Int {
        return products(numbers.size).count { product ->
            var num = 0
            for ((i, op) in product.withIndex()) {
                when (op) {
                    '+' -> num += numbers[i]
                    '-' -> num -= numbers[i]
                }
            }
            num == target
        }
    }

    private fun products(size: Int): List<CharArray> {
        val chars = listOf('+', '-')
        val res = mutableListOf<CharArray>()
        val arr = CharArray(size)

        fun backtrack(depth: Int) {
            if (depth == size) {
                res.add(arr.copyOf())
                return
            }
            for (char in chars) {
                arr[depth] = char
                backtrack(depth + 1)
            }
        }

        backtrack(0)
        return res
    }
}