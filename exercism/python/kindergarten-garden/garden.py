from itertools import chain
from functools import partial


def chunk(n, xs):
    return [xs[i*n:(i+1)*n] for i in range(len(xs) // n)]

chunk2 = partial(chunk, 2)


def flatten(xs):
    return list(chain(*xs))


class Garden(object):
    DEFAULT_STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    PLANT_NAMES = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }

    def __init__(self, rows, students=DEFAULT_STUDENTS):
        students.sort()
        plants = map(flatten, zip(*map(chunk2, rows.split('\n'))))
        self.mapping = dict(zip(students, plants))

    def plants(self, student):
        return [self.PLANT_NAMES[p] for p in self.mapping[student]]
