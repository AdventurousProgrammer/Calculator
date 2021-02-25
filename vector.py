
class Vector():
    vector = list()

    def __init__(self, vector):
        self.vector = vector

    def __copy__(self):
        new = list()
        for i in self.vector:
            new.append(i)
        return new

    def __repr__(self):
        x = '<'
        x += ','.join([str(i) for i in self.vector])
        x += '>'
        return x

    def __add__(self, other):
        if isinstance(other, Vector):
            x = list()
            for i in range(0, len(self.vector)):
                x.append(self.vector[i] + other.vector[i])
            v = Vector(x)
            return v