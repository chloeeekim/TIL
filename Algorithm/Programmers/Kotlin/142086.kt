/*

가장 가까운 같은 글자 : https://school.programmers.co.kr/learn/courses/30/lessons/142086

문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서 자신과 가장 가까운 곳에 있는 같은 글자의 위치를 구하는 문제
- 다음과 같이 진행한다
    - 처음 등장한 글자의 경우, 자신의 앞에 같은 글자가 없으므로 -1로 표현한다
    - 앞에 같은 글자가 있는 경우, 몇 칸 앞에 있는지로 표현한다
- s의 길이는 1 이상 10,000 이하이다
    - s는 영어 소문자로만 이루어져 있다

Example:
- Input : s="banana"
- Output : [-1, -1, -1, 2, 2, 2]

- Input : s="foobar"
- Output : [-1, -1, 1, -1, -1, -1]

Note:
등장한 글자의 마지막 인덱스를 map에 저장
map에 같은 글자가 있으면 차이를 계산하고, 없다면 -1
map의 값을 현재 인덱스로 업데이트

 */

class Solution {
    fun solution(s: String): IntArray {
        val indexMap = mutableMapOf<Char, Int>()

        return s.mapIndexed { now, ch ->
            val idx = indexMap[ch] ?: -1
            indexMap[ch] = now
            if (idx == -1) -1 else now - idx
        }.toIntArray()
    }
}