from collections import defaultdict


class School(object):
    def __init__(self, name):
        self._store = defaultdict(list)

    def add(self, student, grade):
        self._store[grade].append(student)

    def grade(self, g):
        return tuple(sorted(self._store[g]))

    def sort(self):
        return sorted((key, self.grade(key)) for key in self._store)
