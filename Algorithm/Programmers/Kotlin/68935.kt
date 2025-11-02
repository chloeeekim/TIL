/*

3진법 뒤집기 : https://school.programmers.co.kr/learn/courses/30/lessons/68935

자연수 n이 주어졌을 때, n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 구하는 문제
- n은 1 이상 100,000,000 이하인 자연수이다

Example:
- Input : n=45
- Output : 7
- 45 -> 1200 (3진법) -> 0021 (3진법 뒤집기) -> 7 (10진법)

- Input : n=125
- Output : 229
- 125 -> 11122 (3진법) -> 22111 (3진법 뒤집기) -> 229 (10진법)

Note:
10진법 -> N진법 변환: toString(N)
N진법 -> 10진법 변환: toInt(N)

 */

class Solution {
    fun solution(n: Int): Int {
        return n.toString(3).reversed().toInt(3)
    }
}