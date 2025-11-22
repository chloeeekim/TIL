/*

매칭 점수 : https://school.programmers.co.kr/learn/courses/30/lessons/42893

검색어와 웹페이지 정보가 주어졌을 때, 매칭 점수가 가장 높은 웹페이지의 인덱스를 구하는 문제
- 매칭 점수는 다음과 같은 규칙으로 계산한다
    - 한 웹페이지에 대해서 기본점수, 외부 링크 수, 링크점수, 매칭점수를 구할 수 있다
    - 기본점수는 해당 웹페이지의 텍스트 중 검색어가 등장하는 횟수이다 (대소문자는 무시한다)
    - 외부 링크 수는 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수이다
    - 링크점수는 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본 점수 / 외부 링크 수의 총합이다
    - 매칭점수는 기본점수와 링크점수의 합으로 계산한다
- pages는 HTML 형식의 웹페이지가 문자열 형태로 들어있는 배열로, 길이는 1 이상 20 이하이다
    - 한 웹페이지의 문자열의 길이는 1 이상 1,500 이하이다
    - 웹페이지의 index는 pages 배열의 index와 같으며, 0부터 시작한다
    - 한 웹페이지의 url은 HTML의 <head> 태그 내에 <meta> 태그의 값으로 주어진다
        - <meta ... content="xxx" /> 형태일 때, 웹페이지의 url은 xxx이다
    - 한 웹페이지의 모든 외부 링크는 <a href="xxx"> 형태로 주어진다
        - <a> 내에 다른 attribute가 주어지는 경우는 없으며, 항상 href로 연결할 사이트의 url만 포함된다
    - 모든 url은 https://로만 시작한다
- 검색어 word는 길이 1 이상 12 이하의 하나의 영어 단어이며, 알파벳 소문자와 대문자로만 이루어져 있다
    - 검색어를 찾을 때, 대소문자 구분은 무시하고 찾는다
    - 검색어는 단어 단위로 비교하며, 단어와 완전히 일치하는 경우에만 기본점수에 반영한다
        - 단어는 알파벳을 제외한 다른 모든 문자로 구분한다
        - 검색어가 "aba"일 때, "abab abababa"는 단어 단위로 일치하는 것이 없으므로 기본점수는 0이다
        - 검색어가 "aba"일 때, "aba@aba aba"는 단어 단위로 세 개가 일치하므로, 기본점수는 3이다
- 동일한 매칭점수를 가진 웹페이지가 여러 개라면 그 중 index 번호가 가장 작은 것을 리턴한다

Example:
- Input : word=blind, pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
- Output : 0
- 첫 번째 페이지: 기본점수 3, 외부 링크 수 1, 링크점수 1.5, 매칭점수 4.5
- 두 번째 페이지: 기본점수 1, 외부 링크 수 2, 링크점수 3, 매칭점수 4
- 세 번째 페이지: 기본점수 1, 외부 링크 수 1, 링크점수 0.5, 매칭점수 1.5

- Input : word=Muzi, pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
- Output : 1
- 첫 번째 페이지: 기본점수 0, 외부 링크 수 1, 링크점수 0, 매칭점수 0
- 두 번째 페이지: 기본점수 1, 외부 링크 수 1, 링크점수 0, 매칭점수 1

Note:
regex를 사용하여 HTML 형태의 문자열에서 필요한 데이터를 추출하여 map에 저장
텍스트는 단어 단위로 구분해야 하므로, regex를 사용하여 알파벳이 아닌 문자에 대해(^a-zA-Z) split하여 비교

 */

class Solution {
    data class Metadata(val id: Int, val links: List<String>)

    fun solution(word: String, pages: Array<String>): Int {
        val size = pages.size
        val basicScore = IntArray(size)
        val linkScore = DoubleArray(size)

        val metadata = mutableMapOf<String, Metadata>().apply {
            for ((idx, page) in pages.withIndex()) {
                val url = page.parseUrl()
                val links = page.parseLink()
                basicScore[idx] = page.countWord(word)
                this[url] = Metadata(idx, links)
            }
        }

        for ((url, meta) in metadata.entries) {
            val linkCount = meta.links.size.toDouble()
            for (link in meta.links) {
                if (link in metadata) {
                    linkScore[metadata[link]!!.id] += basicScore[meta.id] / linkCount
                }
            }
        }

        val totalScore = DoubleArray(size) { basicScore[it] + linkScore[it] }
        val maxScore = totalScore.maxOrNull() ?: 0
        return totalScore.withIndex().filter { (idx, score) -> score == maxScore }.first().index
    }

    fun String.parseUrl(): String {
        val regex = "<meta[^>]*content=\"([^\"]*)".toRegex()
        return regex.find(this)!!.groups[1]!!.value
    }

    fun String.parseLink(): List<String> {
        val regex = "<a[^>]*href=\"([^\"]*)".toRegex()
        return regex.findAll(this).map { it.groups[1]!!.value }.toList()
    }

    fun String.countWord(word: String): Int {
        val target = word.lowercase()
        val regex = """<body>([\s\S]*?)</body>""".toRegex()
        val body = regex.find(this)!!.groups[1]!!.value
        val words = body.split(Regex("[^a-zA-Z]+")).filter { it.isNotEmpty() }.map { it.lowercase() }
        return words.count { it == target }
    }
}