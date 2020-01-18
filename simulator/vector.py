import numbers

class Vector:

    def __init__(self):
        self.x, self.y, self.z = 0, 0, 0

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def __repr__(self):
        return self.__str__()

    def __add__(self, v):
        if isinstance(v, Vector):
            return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
        elif isinstance(v, numbers.Integral):
            return Vector(self.x + v, self.y + v, self.z + v)
        else:
            raise NotImplementedError

    def __radd__(self, v):
        return self.__add__(v)
    
    def __sub__(self, v):
        return self.__add__(-v)

    def __rsub__(self, v):
        return self.__neg__().__add__(v)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, a):
        if isinstance(a, Vector):
            return Vector(self.x * a.x, self.y * a.y, self.z * a.z)
        elif isinstance(a, numbers.Integral):
            return Vector(a * self.x, a * self.y, a * self.z)
        else:
            raise NotImplementedError

    def __rmul__(self, a):
        return self.__mul__(a)

    def __truediv__(self, a):
        if isinstance(a, Vector):
            return Vector(self.x / a.x, self.y / a.y, self.z / a.z)
        elif isinstance(a, numbers.Integral):
            return Vector(self.x / a, self.y / a, self.z / a)
        else:
            raise NotImplementedError

    def dot(self, v):
        if isinstance(v, Vector):
            return self.x * v.x + self.y * v.y + self.z * v.z
        else:
            raise NotImplementedError

    def cross(self, v):
        if isinstance(v, Vector):
            return Vector(
                self.y * v.z - self.z * v.y,
                self.z * v.x - self.x * v.z,
                self.x * v.y - self.y * v.x
            )
        else:
            raise NotImplementedError

    


