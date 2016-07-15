
class Trie(object):

    TERMINAL = '0'

    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.TERMINAL] = {}

    def search(self, word, trie=None):
        if trie is None:
            trie = self.root
        if not word:
            return self.TERMINAL in trie
        x, xs = word[0], word[1:]
        return x in trie and self.search(xs, trie[x])

    def startsWith(self, prefix, trie=None):
        if trie is None:
            trie = self.root
        if not prefix:
            return True
        x, xs = prefix[0], prefix[1:]
        return x in trie and self.startsWith(xs, trie[x])


if __name__ == '__main__':
    t = Trie()
    t.insert('abc')
    assert t.search('abc') is True
    assert t.search('ab') is False
    t.insert('ab')
    assert t.search('ab') is True
