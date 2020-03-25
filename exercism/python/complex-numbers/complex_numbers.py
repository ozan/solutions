import math

class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return self + ComplexNumber(-1, 0) * other

    def __truediv__(self, other):
        scale = ComplexNumber(1/(other.real**2 + other.imaginary**2), 0)
        return scale * ComplexNumber(
                self.real * other.real + self.imaginary * other.imaginary,
                self.imaginary * other.real - self.real * other.imaginary)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(math.exp(self.real), 0) * ComplexNumber(
                math.cos(self.imaginary),
                math.sin(self.imaginary))
