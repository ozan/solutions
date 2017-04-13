"""
Given a 2D board and a word, find if the word exists in the grid.

Take a recursive backtracking approach to thoroughly search, using a trie to
prune the search tree as we go.
'"""

TRIE_END = 'END'


def find_from(board, trie, coords, visited, prefix):
    found = set()

    if TRIE_END in trie:
        found.add(prefix)

    # expand the search to every neighbor
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ci, cj = coords[0] + di, coords[1] + dj

        # prune the branch if we're off the board, the prefix is missing from
        # the trie, or we've already visited the candidate coordinate
        if not 0 <= ci < len(board) or not 0 <= cj < len(board[ci]) \
                or not board[ci][cj] in trie or (ci, cj) in visited:
            continue

        # temporarily mark candidate as visited
        visited.add((ci, cj))

        # combine what's been found so far with those found searching deeper
        found |= find_from(board, trie[board[ci][cj]], (ci, cj), visited,
                           prefix + board[ci][cj])
        # backtrack
        visited.remove((ci, cj))

    return found


def make_trie(words):
    trie = {}
    for word in words:
        d = trie
        for ch in word:
            if ch not in d:
                d[ch] = {}
            d = d[ch]
        d[TRIE_END] = True
    return trie


class Solution(object):
    def findWords(self, board, words):
        found = set()
        trie = make_trie(words)
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if board[i][j] in trie:
                    found |= find_from(board, trie[board[i][j]],
                                       (i, j), {(i, j)}, board[i][j])
        return list(found)


large_word_list = ['baabab', 'abaaaa', 'abaaab', 'ababba', 'aabbab', 'aabbba',
                   'aabaab']
large_board = [
    'bbaabaabaaaaabaababaaaaababb',
    'aabbaaabaaabaabaaaaaabbaaaba',
    'babaababbbbbbbaabaababaabaaa',
    'bbbaaabaabbaaababababbbbbaaa',
    'babbabbbbaabbabaaaaaabbbaaab',
    'bbbababbbbbbbababbabbbbbabaa',
    'babababbababaabbbbabbbbabbba',
    'abbbbbbaabaaabaaababaabbabba',
    'aabaabababbbbbbababbbababbaa',
    'aabbbbabbaababaaaabababbaaba',
    'ababaababaaabbabbaabbaabbaba',
    'abaabbbaaaaababbbaaaaabbbaab',
    'aabbabaabaabbabababaaabbbaab',
    'baaabaaaabbabaaabaabababaaaa',
    'aaabbabaaaababbabbaabbaabbaa',
    'aaabaaaaabaabbabaabbbbaabaaa',
    'abbaabbaaaabbaababababbaabbb',
    'baabaababbbbaaaabaaabbababbb',
    'aabaababbaababbaaabaabababab',
    'abbaaabbaabaabaabbbbaabbbbbb',
    'aaababaabbaaabbbaaabbabbabab',
    'bbababbbabbbbabbbbabbbbbabaa',
    'abbbaabbbaaababbbababbababba',
    'bbbbbbbabbbababbabaabababaab',
    'aaaababaabbbbabaaaaabaaaaabb',
    'bbaaabbbbabbaaabbaabbabbaaba',
    'aabaabbbbaabaabbabaabababaaa',
    'abbababbbaababaabbababababbb',
    'aabbbabbaaaababbbbabbababbbb',
    'babbbaabababbbbbbbbbaabbabaa']

if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    s = Solution()
    assert s.findWords(board, ['SEE', 'CAT', 'SAD', 'SE']) \
        == ['SEE', 'SE', 'SAD']
    assert s.findWords(large_board, large_word_list) == [
        'aabbab', 'ababba', 'baabab', 'aabaab', 'abaaab', 'abaaaa', 'aabbba']
    print('ok')
