/*

표 병합 : https://school.programmers.co.kr/learn/courses/30/lessons/150366

50x50 크기의 표와 명령어들이 주어졌을 때, PRINT 명령어에 대한 실행 결과를 구하는 문제
- UPDATE r c value
    - (r, c) 위치의 셀의 값을 value로 바꾼다
- UPDATE value1 value2
    - value1을 값으로 가지고 있는 모든 셀을 value2로 바꾼다
- MERGE r1 c1 r2 c2
    - (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합한다
    - 두 위치의 셀이 같은 셀일 경우 무시한다
    - 두 셀이 인접하지 않은 경우, 사이에 위치한 셀들은 영향을 받지 않는다
    - 두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가지게 된다
    - 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀의 값을 가진다
    - 이후 (r1, c1)과 (r2, c2) 중 어느 위치를 선택하더라도 병합된 셀로 접근한다
- UNMERGE r c
    - (r, c) 위치의 셀의 모든 병합을 해제한다
    - 선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기의 상태로 돌아간다
    - 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가진다
- PRINT r c
    - (r, c) 위치의 셀의 값을 출력한다
    - 선택한 셀이 비어있을 경우 "EMPTY"를 출력한다
- 주어지는 r, c는 1 이상 50 이하의 정수이다
- 주어지는 value는 알파벳 소문자와 숫자로 구성된 길이 1 이상 10 이하의 문자열이다
- commands는 1개 이상의 PRINT 명령어를 포함한다

Example:
- Input : commands=["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
- Output : ["EMPTY", "group"]

- Input : commands=["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
- Output : ["d", "EMPTY"]

Note:
각 명령어들을 별도의 함수로 구분하여 구현
각 셀(r, c)는 r * 50 + c의 값으로 초기화하며, 해당 값으로 group을 구분
group map에 Pair(r, c)가 가리키고 있는 table의 인덱스를 저장

 */

class Solution {
    fun solution(commands: Array<String>): Array<String> {
        val answer = mutableListOf<String>()
        val table = Array(50 * 50) { "EMPTY" }
        val group = mutableMapOf<Pair<Int, Int>, Int>().apply {
            for (i in 0 until 50) {
                for (j in 0 until 50) {
                    this[i to j] = i * 50 + j
                }
            }
        }

        fun update1(r: Int, c: Int, value: String) {
            table[group[r to c]!!] = value
        }

        fun update2(value1: String, value2: String) {
            for (i in 0 until 50 * 50) {
                if (table[i] == value1) table[i] = value2
            }
        }

        fun merge(r1: Int, c1: Int, r2: Int, c2: Int) {
            val group1 = group[r1 to c1]!!
            val group2 = group[r2 to c2]!!

            if (table[group1] == "EMPTY") table[group1] = table[group2]

            for ((key, num) in group.entries) {
                if (num == group2) group[key] = group1
            }
        }

        fun unmerge(r: Int, c: Int) {
            val gnum = group[r to c]!!
            val value = table[gnum]

            for ((key, num) in group.entries) {
                val temp = key.first * 50 + key.second
                if (num == gnum) {
                    table[temp] = "EMPTY"
                    group[key] = temp
                }
            }

            table[r * 50 + c] = value
        }

        fun pprint(r: Int, c: Int) {
            answer.add(table[group[r to c]!!])
        }

        for (comm in commands) {
            val sp = comm.split(" ")
            when (sp[0]) {
                "UPDATE" -> {
                    if (sp.size == 4) update1(sp[1].toInt() - 1, sp[2].toInt() - 1, sp[3])
                    else update2(sp[1], sp[2])
                }
                "MERGE" -> merge(sp[1].toInt() - 1, sp[2].toInt() - 1, sp[3].toInt() - 1, sp[4].toInt() - 1)
                "UNMERGE" -> unmerge(sp[1].toInt() - 1, sp[2].toInt() - 1)
                "PRINT" -> pprint(sp[1].toInt() - 1, sp[2].toInt() - 1)
            }
        }

        return answer.toTypedArray()
    }
}