/*

마법의 엘리베이터 : https://school.programmers.co.kr/learn/courses/30/lessons/148653

어떤 층에서 마법의 엘리베이터를 타고 0층으로 내려가는데 필요한 마법의 돌의 최소 개수를 구하는 문제
- 엘리베이터에는 -1, +1, -10, +10, -100, +100 등 절댓값이 10^c (c >= 0인 정수) 형태인 정수들이 적힌 버튼이 있다
    - 엘리베이터의 버튼을 누르면 현재 층 수에 버튼에 적혀 있는 값을 더한 층으로 이동한다
    - 단, 엘리베이터가 위치해 있는 층과 버튼의 값을 더한 결과가 0보다 작으면 엘리베이터는 움직이지 않는다
- 엘리베이터를 움직이기 위해서는 버튼 한 번당 마법의 돌 한 개를 사용한다
- 현재 있는 층을 나타내는 정수 storey는 1 이상 100,000,000 이하이다

Example:
- Input : storey=16
- Output : 6
- +1이 적힌 버튼을 4번, -10이 적힌 버튼을 2번 눌러 이동할 수 있다

- Input : storey=2554
- Output : 16

Note:
1의 자리부터 10의 자리, 100의 자리, ... 순으로 각 자릿수별로 계산
숫자가 5보다 작은 경우 -1을 하는 경우가 적은 횟수
숫자가 5보다 큰 경우 +1을 하는 경우가 적은 횟수
숫자가 5인 경우, 윗 자리를 확인하여 1을 더했을 때 이득이라면 더하는 방식으로, 아니라면 빼는 방식

 */

class Solution {
    fun solution(storey: Int): Int {
        var answer = 0
        var curr = storey

        while (curr > 0) {
            val digit = curr % 10
            curr = curr / 10

            when {
                digit < 5 -> answer += digit
                digit > 5 -> {
                    answer += 10 - digit
                    curr++
                }
                else -> {
                    if (curr % 10 >= 5) curr++
                    answer += digit
                }
            }
        }

        return answer
    }
}