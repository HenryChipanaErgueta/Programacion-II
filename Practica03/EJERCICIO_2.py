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
           if self.validaNumero(numeroIngresado) == False:
               print("Numero Invalido, ingresa un numero entre 0 y 10")
               continue
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
    def validaNumero(self,numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            return False
        

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10 and numero % 2 == 0:
            return True
        else:
            print("Numero Invalido, ingresa un numero par entre 0 y 10")
            return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >=0 and numero <= 10 and numero % 2 != 0:
            return True
        else:
            print("Numero Invalido, ingresa un numero impar entre 0 y 10")
            return False


class Aplicacion:
    def main(self):
        print("=== INICIANDO JUEGO NORMAL ===")
        juego_normal = JuegoAdivinaNumero(3)
        juego_normal.juega()
        
        print("\n=== INICIANDO JUEGO DE PARES ===")
        juego_pares = JuegoAdivinaPar(3)
        juego_pares.juega()
        
        print("\n=== INICIANDO JUEGO DE IMPARES ===")
        juego_impares = JuegoAdivinaImpar(3)
        juego_impares.juega()

app = Aplicacion()
app.main()