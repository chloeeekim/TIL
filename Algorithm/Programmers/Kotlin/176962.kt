/*

과제 진행하기 : https://school.programmers.co.kr/learn/courses/30/lessons/176962

과제 계획이 주어졌을 때, 특정 순서대로 과제를 진행한 후 과제를 끝낸 순서를 구하는 문제
- 과제를 진행하는 순서는 다음과 같다
    - 과제는 시작하기로 한 시각이 되면 시작한다
    - 새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작한다
    - 진행 중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행한다
        - 만약, 과제를 끝낸 시각에 새로 시작해야 하는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행한다
    - 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작한다
- 과제 계획을 담은 이차원 문자열 배열 plans의 길이는 3 이상 1,000 이하이다
    - plans의 원소는 [name, start, playtime]의 구조로 이루어져 있다
        - 과제의 이름 name은 길이 2 이상 10 이하인 문자열로, 알파벳 소문자로만 이루어져 있다
        - name이 중복되는 원소는 없다
        - 과제의 시작 시간 start는 "hh:mm"의 형태로 "00:00" 부터 "23:59" 사이의 시간값만 들어가 있다
        - 모든 과제의 시작 시간은 다르다
        - 과제는 시와 분의 값이 작을수록 더 빨리 시작한다
        - 과제를 마치는데 걸리는 시간 playtime은 1 이상 100 이하의 정수로, 단위는 분이다
        - playtime은 0으로 시작하지 않는다
    - 배열은 시간순으로 정렬되어 있지 않을 수 있다
- 진행 중이던 과제가 끝나는 시각과 새로운 과제를 시작해야 하는 시각이 같은 경우, 진행 중이던 과제는 끝난 것으로 판단한다

Example:
- Input : plans=[["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
- Output : ["korean", "english", "math"]

- Input : plans=[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
- Output : ["science", "history", "computer", "music"]

- Input : plans=[["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
- Output : ["bbb", "ccc", "aaa"]

Note:
주어진 시간 입력값은 계산하기 편하도록 분으로 환산
잠시 멈춘 과제는 stack에 추가하여 시간이 남을 때 진행

 */

class Solution {
    fun solution(plans: Array<Array<String>>): Array<String> {
        val stack = ArrayDeque<Pair<String, Int>>()
        val answer = mutableListOf<String>()
        val size = plans.size
        val sPlans = plans.map { Triple(it[0], toMinutes(it[1]), it[2].toInt()) }.sortedBy { it.second }

        for (i in 0 until size) {
            val (name, start, playtime) = sPlans[i]
            val next = sPlans.getOrNull(i+1)?.second ?: Int.MAX_VALUE
            var term = next - start

            if (playtime > term) {
                stack.addLast(name to playtime - term)
            }
            else {
                answer.add(name)
                term -= playtime

                while (stack.isNotEmpty()) {
                    val (tname, remain) = stack.removeLast()
                    if (term >= remain) {
                        term -= remain
                        answer.add(tname)
                    } else {
                        stack.addLast(tname to remain - term)
                        break
                    }
                }
            }
        }

        return answer.toTypedArray()
    }

    private fun toMinutes(time: String): Int {
        val (hh, mm) = time.split(":").map { it.toInt() }
        return hh * 60 + mm
    }
}