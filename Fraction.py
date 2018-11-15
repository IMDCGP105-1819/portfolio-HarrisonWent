class Fraction(object):

    def __int__(self, a,b):
        try:
            int(a)
            self.a = a
        except TypeError:
            print("a is not an integer!")
        try:
            int(b)
            self.b = b
        except TypeError:
            print("b is not an integer!")

    def __add__(self, other):
        return self.a + self.b

    def __sub__(self, other):
        return self.a - self.b

    def __mul__(self, other):
        return self.a*self.b

    def __truediv__(self, other):
        return self.a / self.b

    def __invert__(self):
        return -self.a
