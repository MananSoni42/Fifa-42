"""
Defines a 2d Point

Supports:

- addition
- subtaction
- multiplication
- distance calculation
"""

import math

class P:
    """
    Implementation of a 2-D point
    """

    def __init__(self, x,y=None):
        """
        Initialize an point

        Examples:
        ```
        pt1 = P(3,4)
        pt2 = P((3,4))
        pt3 = P([3,4])
        pt4 = P(pt3)
        ```
        """
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
        """
        Return the value of the point as a tuple rounded to the nearest integer point
        """
        return (int(round(self.x,0)), int(round(self.y,0)))

    @property
    def mag(self):
        """
        Return the magnitude of the point (it's distance from zero)
        """
        return math.sqrt(self.x**2 + self.y**2)

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
        return math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
