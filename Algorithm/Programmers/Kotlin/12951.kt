/*

JadenCase 문자열 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/12951

문자열이 주어졌을 때, JadenCase로 바꾼 문자열을 구하는 문제
- JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열을 의미한다
    - 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓴다
- 문자열 s는 길이 1 이상 200 이하이다
    - s는 알파벳과 숫자, 공백 문자(" ")로 이루어져 있다
    - 숫자는 단어의 첫 문자로만 나온다
    - 숫자로만 이루어진 단어는 없다
    - 공백문자가 연속해서 나올 수 있다

Example:
- Input : s="3people unFollowed me"
- Output : "3people Unfollowed Me"

- Input : s="for the last week"
- Output : "For The Last Week"

Note:
s를 lowercase로 변경한 후 공백을 기준으로 나눈 다음, 각 단어에 대해서 첫 번째 문자를 uppercase로 변환한 다음 join
공백이 연속해서 나올 수 있으므로 예외 처리 추가

 */

class Solution {
    fun solution(s: String): String {
        return s.toLowerCase().split(" ").map { str ->
            if (str.isEmpty()) ""
            else {
                str.replaceFirstChar { it.uppercaseChar() }
            }
        }.joinToString(" ")
    }
}