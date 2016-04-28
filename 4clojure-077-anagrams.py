#!/usr/bin/env python

from collections import defaultdict


def group_anagram(memo, word):
    memo[''.join(sorted(word))].add(word)
    return memo


def anagrams(words):
    return reduce(group_anagram, words, defaultdict(set)).values()


print anagrams(['veer', 'lake', 'item', 'kale', 'mite', 'ever'])
