class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            index = ord(ch) - ord("a")
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

