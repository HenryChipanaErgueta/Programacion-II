import random
class Juego:
    def __init__(self,numeroDeVidas , record):
        self.numeroDeVidas = numeroDeVidas
        self.vidasIniciales = numeroDeVidas
        self.record = record
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
        self.record = 0
    def actualizaRecord(self,record):
        self.record = record
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas, record = 0)
        self.numeroAAdivinar = 0
    def juega (self):
       self.reiniciaPartida()
       self.numeroAAdivinar = random.randint(0,10)
       print("Adivina el numero entre 0 y 10")
       while self.numeroDeVidas > 0:
           numeroIngresado = int(input("Ingresa un numero de 0 a 10: "))
           if numeroIngresado == self.numeroAAdivinar:
               print("Acertaste!")
               self.actualizaRecord(self.record + 1)
               break
           else:
               vidas = self.quitaVida()
               print("Numero Incorrecto")
           if vidas:
                if self.numeroAAdivinar > numeroIngresado:
                    print("El numero es mayor sigue intentando") 
                else:
                    print("El numero es menor sigue intentando")
           else:
                print("Perdiste! El numero era: ", self.numeroAAdivinar)

class Aplicacion:
    def main(self):
        mi_partida = JuegoAdivinaNumero(5)
        
        mi_partida.juega()

app = Aplicacion()
app.main() 