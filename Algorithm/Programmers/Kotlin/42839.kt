/*

소수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

종이 조각에 적힌 숫자들이 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 구하는 문제
- 종이 조각에는 한 자리 숫자가 적혀 있다
- 종이 조각에 적힌 숫자가 적힌 문자열 number의 길이는 1 이상 7 이하이다
    - numbers는 0~9까지의 숫자만으로 이루어져 있다
    - "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져 있다는 의미이다

Example:
- Input : numbers="17"
- Output : 3
- 7, 17, 71을 만들 수 있다

- Input : numbers="011"
- Output : 2
- 11, 101을 만들 수 있다

Note:
permutations을 만드는 방식으로 만들 수 있는 모든 경우의 수를 확인
set을 사용하여 중복을 제거

 */

import kotlin.math.sqrt

class Solution {
    fun solution(numbers: String): Int {
        val numSet = (1 .. numbers.length).flatMap { getAllNumbers(numbers, it) }.toSet()
        return numSet.count { num -> isPrime(num) }
    }

    private fun isPrime(num: Int): Boolean {
        if (num == 0 || num == 1) return false
        return (2 .. sqrt(num.toDouble()).toInt()).all {
            num % it != 0
        }
    }

    private fun getAllNumbers(nums: String, size: Int): List<Int> {
        val result = mutableListOf<Int>()
        val used = BooleanArray(nums.length)

        fun backtrack(path: StringBuilder) {
            if (path.length == size) {
                result.add(path.toString().toInt())
                return
            }

            for (i in nums.indices) {
                if (used[i]) continue
                used[i] = true
                path.append(nums[i])
                backtrack(path)
                path.deleteCharAt(path.lastIndex)
                used[i] = false
            }
        }

        backtrack(StringBuilder())
        return result
    }
}