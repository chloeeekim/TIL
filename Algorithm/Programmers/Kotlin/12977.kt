/*

소수 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/12977

숫자들이 들어있는 배열이 주어졌을 때, 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하는 문제
- nums의 길이는 3 이상 50 이하이며, nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자는 들어있지 않다

Example:
- Input : nums=[1,2,3,4]
- Output : 1

- Input : nums=[1,2,7,6,4]
- Output : 4

Note:
가능한 3개 숫자의 합을 모두 구하여 소수인지 판별
소수 판별용 isPrime 함수를 생성

 */

import kotlin.math.sqrt

class Solution {
    fun solution(nums: IntArray): Int {
        var answer = 0
        val size = nums.size

        for (i in 0 until size-2) {
            for (j in i+1 until size-1) {
                for (k in j+1 until size) {
                    if (isPrime(nums[i] + nums[j] + nums[k])) {
                        answer++
                    }
                }
            }
        }

        return answer
    }

    private fun isPrime(num: Int): Boolean {
        if (num < 2) return false
        val sqrtNum = sqrt(num.toDouble()).toInt()
        return (2 .. sqrtNum).none { num % it == 0 }
    }
}