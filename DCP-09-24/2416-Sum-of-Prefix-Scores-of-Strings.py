class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def get_score(self, word):
        node = self.root
        score = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            score += node.count
        return score

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return [trie.get_score(word) for word in words]