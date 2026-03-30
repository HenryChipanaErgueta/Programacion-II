import math
from multimethod import multimethod
class Vector3D:
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.__a1, self.__a2, self.__a3 = float(a1), float(a2), float(a3)
    def getA1(self): return self.__a1
    def getA2(self): return self.__a2
    def getA3(self): return self.__a3
    def __add__(self, b):
        return Vector3D(self.__a1 + b.getA1(), self.__a2 + b.getA2(), self.__a3 + b.getA3())
    @multimethod
    def __mul__(self, r: float):
        return Vector3D(self.__a1 * r, self.__a2 * r, self.__a3 * r)
    @multimethod
    def __mul__(self, r: int):
        return Vector3D(self.__a1 * r, self.__a2 * r, self.__a3 * r)
    @multimethod
    def __mul__(self, b: object):
        return self.__a1 * b.getA1() + self.__a2 * b.getA2() + self.__a3 * b.getA3()
    def __matmul__(self, b):
        return Vector3D(self.__a2 * b.getA3() - self.__a3 * b.getA2(), self.__a3 * b.getA1() - self.__a1 * b.getA3(), self.__a1 * b.getA2() - self.__a2 * b.getA1())
    def longitud(self):
        return math.sqrt(self.__a1**2 + self.__a2**2 + self.__a3**2)
    def normal(self):
        l = self.longitud()
        return Vector3D(0, 0, 0) if l == 0 else Vector3D(self.__a1 / l, self.__a2 / l, self.__a3 / l)
    def __str__(self):
        return "(" + str(self.__a1) + ", " + str(self.__a2) + ", " + str(self.__a3) + ")"
if __name__ == "__main__":
    v1 = Vector3D(1.0, 2.0, 3.0)
    v2 = Vector3D(4.0, 5.0, 6.0)
    print(v1 + v2)
    print(v1 * v2)
    print(v1 @ v2)