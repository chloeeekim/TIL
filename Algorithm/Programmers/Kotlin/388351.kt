/*

유연근무제 : https://school.programmers.co.kr/learn/courses/30/lessons/388351

직원들의 출근 희망 시각과 실제 출근한 기록을 바탕으로, 일주일 동안 출근 희망 시각 + 10분 이내에 출근한 사람이 몇 명인지 구하는 문제
- 토요일, 일요일의 출근 시각은 영향을 끼치지 않는다
- 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현된다 (e.g., 10시 13분 -> 1013, 9시 58분 -> 958)
- startday는 이벤트의 시작 날짜로, 1은 월요일, 2는 화요일, ... , 7은 일요일을 의미한다

Example:
- Input : schedules=[700, 800, 1100], timelogs=
[
    [710, 2359, 1050, 700, 650, 631, 659],
    [800, 801, 805, 800, 759, 810, 809],
    [1105, 1001, 1002, 600, 1059, 1001, 1100]
], startday=5
- Output : 3

- Input : schedules=[730, 855, 700, 720], timelogs=
[
    [710, 700, 650, 735, 700, 931, 912],
    [908, 901, 805, 815, 800, 831, 835],
    [705, 701, 702, 705, 710, 710, 711],
    [707, 731, 859, 913, 934, 931, 905]
], startday=1
- Output : 2
- 첫 번째와 세 번째 직원만 해당

Note:
출근 희망 시각 + 10분을 구한 다음 timelogs의 값과 비교
토요일 및 일요일의 출근 시각은 영향을 끼치지 않으므로 제외
indices.count를 사용하여 조건을 만족하는 요소 수를 계산
none을 사용하여 true 반환 시 반복이 종료되도록 구현

*/

class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        return schedules.indices.count { idx ->
            val time = schedules[idx].plusTenMin()
            var day = startday

            timelogs[idx].none {
                if (day in 1 .. 5 && it > time) {
                    true
                }
                else {
                    day  = (day % 7) + 1
                    false
                }
            }
        }
    }

    private fun Int.plusTenMin(): Int {
        var hour = this / 100
        var minute = (this % 100) + 10

        if (minute >= 60) {
            hour += 1
            minute -= 60
        }

        return hour * 100 + minute
    }
}