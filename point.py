import numpy as np

class P:
    """ 2-D point """

    def __init__(self, x,y=None):
        if y is None:
            if isinstance(x,tuple):
                self.x = x[0]
                self.y = x[1]
            elif isinstance(x,P):
                self.x = x.x
                self.y = x.y
        else:
            self.x = x
            self.y = y

    @property
    def val(self):
        return (self.x, self.y)

    def __str__(self):
        return f'P({self.x}, {self.y})'

    def __add__(self, p):
        return P(self.x + p.x, self.y + p.y)

    def __iadd__(self, p):
        self.x += p.x
        self.y += p.y
        return self

    def __sub__(self, p):
        return P(self.x - p.x, self.y - p.y)

    def __isub__(self, p):
        self.x -= p.x
        self.y -= p.y
        return self

    def __mul__(self, p):
        return P(int(self.x * p.x), int(self.y * p.y))

    def __imul__(self, p):
        self.x *= p.x
        self.y *= p.y
        return self

    def dist(self, p):
        return np.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
