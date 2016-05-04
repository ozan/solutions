
class TriangleError(Exception):
    pass


class Triangle(object):

    CASES = 'wat equilateral isosceles scalene'.split()

    def __init__(self, *sides):
        if any(s <= 0 for s in sides):
            raise TriangleError

        a, b, c = sorted(sides)
        if a + b <= c:
            raise TriangleError

        self.kind = lambda: self.CASES[len(set(sides))]
