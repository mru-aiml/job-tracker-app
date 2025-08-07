# Trie logic for resume skills
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_words_with_prefix(self, prefix):
        def dfs(node, path, results):
            if node.is_end_of_word:
                results.append("".join(path))
            for char, child in node.children.items():
                dfs(child, path + [char], results)

        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        dfs(node, list(prefix.lower()), results)
        return results
