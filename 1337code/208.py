class Trie:
    class Node:
        def __init__(self, value, children):
            self.value = value
            self.children = children
    
    def __init__(self):
        self.root = self.Node('', {})

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                next = self.Node(c, {})
                curr.children[c] = next
                curr = next

        if '.' not in curr.children:
            curr.children['.'] = self.Node('.', {})            

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
    
        return '.' in curr.children

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
word = "apple"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)