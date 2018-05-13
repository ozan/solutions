from collections import defaultdict, deque, namedtuple
from itertools import permutations

QueueItem = namedtuple('QueueItem', ('word', 'steps'))


def construct_graph(words):
    # * add each word to WORD_LENGTH collections, one for each word
    #   obtained by replacing a character with a blank
    # * each bucket represents connected vertices, so iterate over each
    #   bucket making n(n-1) / 2 handshake pairs of vertices
    words_by_similarity = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            similarity_key = word[:i] + ' ' + word[(i + 1):]
            words_by_similarity[similarity_key].append(word)

    graph = defaultdict(list)
    for connected_words in words_by_similarity.values():
        for a, b in permutations(connected_words, 2):
            if a != b:
                graph[a].append(b)

    return graph

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        graph = construct_graph(wordDict)
        traversed = set([beginWord])
        traversal_queue = deque([QueueItem(beginWord, 1)])
    
        while traversal_queue:
            item = traversal_queue.pop()
            for next_word in graph[item.word]:
                if next_word == endWord:
                    return item.steps + 1
                if next_word not in traversed:
                    traversed.add(next_word)
                    next_item = QueueItem(next_word, item.steps + 1)
                    traversal_queue.appendleft(next_item)
    
        return 0
        