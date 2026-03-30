import math
from multimethod import multimethod
class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    @multimethod
    def distancia(self, otroPunto: object):
        return math.hypot(self.__x - otroPunto.getX(), self.__y - otroPunto.getY())
    @multimethod
    def distancia(self, x: float, y: float):
        return math.hypot(self.__x - x, self.__y - y)
if __name__ == "__main__":
    p1 = MiPunto()
    p2 = MiPunto(10.0, 30.5)
    
    print(p1.distancia(p2))