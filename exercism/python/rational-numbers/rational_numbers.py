from __future__ import division


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Rational(object):
    def __init__(self, a, b):
        d = gcd(a, b)
        self.a = a / d
        self.b = b / d

    def __eq__(self, other):
        try:
            return self.a == other.a and self.b == other.b
        except AttributeError:
            return False

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return Rational(self.a * other.b - self.b * other.a, self.b * other.b)

    def __mul__(self, other):
        return Rational(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Rational(self.a * other.b, self.b * other.a)

    def __abs__(self):
        return Rational(abs(self.a), abs(self.b))

    def __pow__(self, power):
        return Rational(self.a**power, self.b**power)

    def __rpow__(self, base):
        return base**(self.a / self.b)
