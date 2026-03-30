import math
from multimethod import multimethod
class AlgebraVectorial:
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.__a1 = float(a1)
        self.__a2 = float(a2)
        self.__a3 = float(a3)
    def getA1(self): return self.__a1
    def getA2(self): return self.__a2
    def getA3(self): return self.__a3
    def modulo(self):
        return math.sqrt(self.__a1**2 + self.__a2**2 + self.__a3**2)
    @multimethod
    def perpendicular(self, b: object):
        dot_product = self.__a1 * b.getA1() + self.__a2 * b.getA2() + self.__a3 * b.getA3()
        return round(dot_product, 4) == 0
    @multimethod
    def perpendicular(self, b1: float, b2: float, b3: float):
        mod_suma = math.sqrt((self.__a1 + b1)**2 + (self.__a2 + b2)**2 + (self.__a3 + b3)**2)
        mod_resta = math.sqrt((self.__a1 - b1)**2 + (self.__a2 - b2)**2 + (self.__a3 - b3)**2)
        return round(mod_suma, 4) == round(mod_resta, 4)
    @multimethod
    def paralela(self, b: object):
        if b.getA1() == 0 or b.getA2() == 0 or b.getA3() == 0:
            return False
        r1 = self.__a1 / b.getA1()
        r2 = self.__a2 / b.getA2()
        r3 = self.__a3 / b.getA3()
        return r1 == r2 and r2 == r3
    @multimethod
    def paralela(self, b1: float, b2: float, b3: float):
        cross1 = self.__a2 * b3 - self.__a3 * b2
        cross2 = self.__a3 * b1 - self.__a1 * b3
        cross3 = self.__a1 * b2 - self.__a2 * b1
        return cross1 == 0 and cross2 == 0 and cross3 == 0
    def proyeccion(self, b):
        dot = self.__a1 * b.getA1() + self.__a2 * b.getA2() + self.__a3 * b.getA3()
        mod_b_sq = b.modulo() ** 2
        esc = dot / mod_b_sq
        return AlgebraVectorial(b.getA1() * esc, b.getA2() * esc, b.getA3() * esc)
    def componente(self, b):
        dot = self.__a1 * b.getA1() + self.__a2 * b.getA2() + self.__a3 * b.getA3()
        return dot / b.modulo()
    def __str__(self):
        return f"({self.__a1}, {self.__a2}, {self.__a3})"
if __name__ == "__main__":
    v1 = AlgebraVectorial(1.0, 0.0, 0.0)
    v2 = AlgebraVectorial(0.0, 1.0, 0.0)
    v3 = AlgebraVectorial(2.0, 0.0, 0.0)
    print(v1.perpendicular(v2))
    print(v1.paralela(v3))
    print(v1.proyeccion(v3))