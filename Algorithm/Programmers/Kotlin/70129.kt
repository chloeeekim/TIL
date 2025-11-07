/*

이진 변환 반복하기 : https://school.programmers.co.kr/learn/courses/30/lessons/70129

0과 1로 이루어진 문자열에 대해 이진 변환을 반복하여 s가 "1"이 될 때까지 했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 구하는 문제
- 문자열 x에 대한 이진 변환은 다음과 같이 정의한다
    - x의 모든 0을 제거한다
    - x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 변경한다
- s의 길이는 1 이상 150,000 이하이다
- s에는 '1'이 최소 하나 이상 포함되어 있다

Example:
- Input : s="110010101001"
- Output : [3, 8]

- Input : s="01110"
- Output : [3, 3]

- Input : s="1111111"
- Output : [4, 1]

Note:
문자열의 길이는 0의 개수 + 1의 개수가 되므로, 0의 개수와 문자열의 길이를 구하여 1의 개수를 구한다

 */

class Solution {
    fun solution(s: String): IntArray {
        val answer = IntArray(2)
        var str = s

        while (str != "1") {
            val zeros = str.count { it == '0' }
            val length = str.length

            str = (length - zeros).toString(2)
            answer[0]++
            answer[1] += zeros
        }

        return answer
    }
}