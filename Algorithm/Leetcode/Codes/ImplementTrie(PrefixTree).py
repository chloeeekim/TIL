"""

208. Implement Trie (Prefix Tree) : https://leetcode.com/problems/implement-trie-prefix-tree/

Trie의 insert, search, startsWith method를 구현하는 문제
- 모든 입력은 a-z까지의 소문자 알파벳만을 포함한다
- 모든 입력은 non-empty string임이 보장된다

Example:
- Input : ["Trie","insert","search","search","startsWith","insert","search"], [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
- Output : [null,null,true,false,true,null,true]

Note:
TrieNode를 생성하여 트리를 구성
단어의 끝에 '.'을 붙여 prefix인지 word 전체인지를 구분

"""

class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('.')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        word = word + '.'
        idx, node = 0, self.root
        while idx < len(word) and word[idx] in node.children :
            node = node.children[word[idx]]
            idx += 1
        while idx < len(word) :
            tmp = TrieNode(word[idx])
            node.children[word[idx]] = tmp
            node = tmp
            idx += 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.startsWith(word + '.')
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix :
            if ch not in node.children :
                return False
            node = node.children[ch]
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)