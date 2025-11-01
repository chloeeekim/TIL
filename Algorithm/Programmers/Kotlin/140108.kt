/*

문자열 나누기 : https://school.programmers.co.kr/learn/courses/30/lessons/140108

문자열 s에 대해 특정 규칙을 따라 여러 문자열로 분해할 때, 분해한 문자열의 개수를 구하는 문제
- 다음 규칙에 따라 문자열을 분해한다
    - 첫 번째 글자를 x라고 한다
    - 문자열을 왼쪽에서 오른쪽으로 읽어 나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 센다
    - 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리한다
    - s에서 분리한 문자열을 빼고 남은 부분에 대해 위 과정을 반복한다
        - 만약 남은 부분이 없다면 종료한다
        - 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 지금까지 읽은 문자열을 분리하고 종료한다
- 문자열 s의 길이는 1 이상 10,000 이하이며, 영어 소문자로만 이루어져 있다

Example:
- Input : s="banana"
- Output : 3
- ba - na - na와 같이 분해

- Input : s="abracadabra"
- Output : 6
- ab - ra - ca - da - br - a와 같이 분해

- Input : s="aaabbaccccabba"
- Output : 3
- aaabbacc - ccab - ba와 같이 분해

Note:
문제에 주어진 규칙대로 x의 횟수(xcount)와 x가 아닌 다른 글자들의 횟수(notx)를 카운트
더 이상 읽을 문자열이 없을 때, 남아 있는 문자열이 있다면 분리해야 하므로 +1

 */

class Solution {
    fun solution(s: String): Int {
        var answer = 0
        var x: Char? = null
        var xcount = 0
        var notx = 0

        for (ch in s) {
            if (x == null) {
                x = ch
            }

            println(ch)

            if (ch == x) xcount++ else notx++

            if (xcount == notx) {
                x = null
                answer++
                xcount = 0
                notx = 0
            }
        }

        if (x != null) {
            answer++
        }

        return answer
    }
}