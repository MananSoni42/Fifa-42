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
        """ Return the value of the point as a tuple rounded to the nearest integer point """
        return (int(round(self.x,0)), int(round(self.y,0)))

    @property    
    def mag(self):
        """ Return the magnitude of the point, basically it's distance from zero or it's mod """
        return np.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f'P({self.x}, {self.y})'

    def __repr__(self):
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
        return P(self.x * p.x, self.y * p.y)

    def __imul__(self, p):
        self.x *= p.x
        self.y *= p.y
        return self

    def dist(self, p):
        return np.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
