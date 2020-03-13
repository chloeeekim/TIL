"""

127. Word Ladder : https://leetcode.com/problems/word-ladder/

wordList가 주어졌을 때, 시작 문자열에서 끝 문자열로 변환하는 최소 거리를 구하는 문제
- 한 번에 한 글자만 변경할 수 있다
- 변경된 단어는 wordList에 포함되어야 한다 (endWord 포함)
- beginWord는 wordList에 포함되지 않는다
- 변경할 수 없는 경우 0을 리턴한다
- 모든 단어들은 길이가 동일하며, 영문 소문자로만 이루어져 있다
- wordList 내에 중복은 없다고 가정한다
- beginWord와 endWord는 비어있지 않으며, 같은 단어가 아니다

Example:
- Input : beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
- Output : 5
- hit -> hot -> dot -> dog -> cog

- Input : beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
- Output : 0
- endWord인 "cog"가 wordList에 없으므로 변환 불가능

Note:
queue를 사용하여 BFS 방식으로 해결
queue에 포함된 단어를 한 글자씩 변경하여 해당 단어가 wordList에 있는지 확인하여 queue에 추가
참고) 더 빠른 방법?

"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList :
            return 0        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        count, queue, seen = 1, [beginWord], {beginWord}
        while queue :
            tmpq = []
            for word in queue :
                for i in range(len(word)) :
                    for ch in alphabets :
                        tmp = word[:i] + ch + word[i+1:]
                        if tmp == endWord :
                            return count + 1
                        if tmp in wordList and tmp not in seen :
                            tmpq.append(tmp)
                            seen.add(tmp)
            count += 1
            queue = tmpq
        return 0