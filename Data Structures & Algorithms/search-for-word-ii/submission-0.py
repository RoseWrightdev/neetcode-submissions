class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.word = word

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        rows, cols = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                (r, c) in visited or board[r][c] not in node.children):
                return

            visited.add((r, c))
            next_node = node.children[board[r][c]]

            if next_node.word:
                res.add(next_node.word)
                next_node.word = None

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return list(res)