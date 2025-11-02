/*

부족한 금액 계산하기 : https://school.programmers.co.kr/learn/courses/30/lessons/82612

놀이기구를 count번 타게 되면 현재 가지고 있는 금액에서 얼마가 모자라는지를 구하는 문제
- 놀이기구의 이용료는 price원이다
    - 놀이기구를 N번째 이용하면 원래의 이용료에서 N배로 요금이 인상된다
- 놀이기구의 이용료 price는 1 이상 2,500 이하의 자연수이다
- 가지고 있는 금액 money는 1 이상 1,000,000,000 이하의 자연수이다
- 놀이기구의 이용 횟수 count는 1 이상 2,500 이하의 자연수이다
- 금액이 부족하지 않은 경우 0을 리턴한다

Example:
- Input : price=3, money=20, count=4
- Output : 10

Note:
놀이기구를 count번 탈 때 이용료의 합은 price * (1 + 2 + ... + count)가 된다
1 + 2 + ... + count는 count * (count + 1) / 2이다

 */

class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        val need = price.toLong() * count * (count + 1) / 2
        return (need - money).coerceAtLeast(0L)
    }
}