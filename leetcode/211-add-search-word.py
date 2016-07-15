"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one letter.

Strategy: use a prefix trie to allow for aggressive pruning
"""

TERM = '0'


def search_trie(word, trie):
    if not word:
        return TERM in trie

    first, rest = word[0], word[1:]
    if first == '.':
        return any(search_trie(rest, v) for v in trie.values())
    return first in trie and search_trie(rest, trie[first])


class WordDictionary(object):
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        d = self.trie
        for ch in word:
            if ch not in d:
                d[ch] = {}
            d = d[ch]
        d[TERM] = {}

    def search(self, word):
        return search_trie(word, self.trie)

if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True

    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("a")
    assert wd.search(".") is True
    assert wd.search("a") is True
    assert wd.search("aa") is False
    assert wd.search("a.") is False

    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("ab")
    assert wd.search("a") is True

    wd = WordDictionary()
    wd.addWord("at")
    assert wd.search("a") is False
