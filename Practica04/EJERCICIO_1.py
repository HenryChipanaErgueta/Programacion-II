class Biblioteca:
    def __init__(self, nombreBiblioteca, diasApertura, horaApertura, horaCierre):
        self.__nombreBiblioteca = nombreBiblioteca
        self.__listaLibros = []
        self.__listaAutores = []    
        self.__listaPrestamosActivos = []
        self.__horario = Horario(diasApertura, horaApertura, horaCierre)

    def agregarLibro(self, Libro):
        self.__listaLibros.append(Libro)

    def agregarAutor(self, Autor):
        self.__listaAutores.append(Autor)
    
    def prestarLibro(self, Libro, Estudiante):
        # Corrección: Agregamos las fechas que el préstamo necesita
        nuevoPrestamo = Prestamo("10-May-2026", "17-May-2026", Estudiante, Libro)
        self.__listaPrestamosActivos.append(nuevoPrestamo)
    
    def mostrarEstado(self):
        print(f"\n--- Nombre de la biblioteca: {self.__nombreBiblioteca} ---")
        self.__horario.mostrarHorario()
        print(f"Libros disponibles: {len(self.__listaLibros)}")
        print(f"Prestamos activos: {len(self.__listaPrestamosActivos)}")

    def cerrarBiblioteca(self):
        print("\nBiblioteca cerrada. Prestamos finalizados.")
        self.__listaPrestamosActivos.clear()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        
    def mostrarInfo(self):
        print(f"Nombre Del Autor : {self.__nombre}, Nacionalidad: {self.__nacionalidad}")

class Horario:
    def __init__(self, diasApertura, horaApertura, horaCierre):
        self.__diasApertura = diasApertura
        self.__horaApertura = horaApertura
        self.__horaCierre = horaCierre
     
    def mostrarHorario(self):
        print(f"Dias de apertura : {self.__diasApertura}")
        print(f"Hora de apertura : {self.__horaApertura}")
        print(f"Hora de cierre : {self.__horaCierre}")
    
class Libro:
    def __init__(self, titulo, isbn, listaContenidos):
        self.__titulo = titulo
        self.__isbn = isbn
        self.__paginas = []
        for i in range(len(listaContenidos)):
            nuevaPagina = Pagina(i + 1, listaContenidos[i])
            self.__paginas.append(nuevaPagina)
    
    def leer(self):
        print(f"Leyendo el libro '{self.__titulo}' con isbn {self.__isbn}")
        # Corrección: Agregamos esto para que muestre las páginas
        for pag in self.__paginas:
            pag.mostrarPagina()

class Pagina:
    def __init__(self, numeroPagina, contenidoPagina):
        self.__numeroPagina = numeroPagina
        self.__contenidoPagina = contenidoPagina
        
    def mostrarPagina(self):
        print(f"Pagina {self.__numeroPagina}: {self.__contenidoPagina}")

class Prestamo:
    def __init__(self, fechaPrestamo, fechaDevolucion, Estudiante, Libro):
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaDevolucion
        self.__estudiante = Estudiante
        self.__libro = Libro   
        
    def mostrarInfo(self):
        # Corrección: Separamos los prints para que no imprima "None"
        print(f"\nFecha de prestamo : {self.__fechaPrestamo}")
        print(f"Fecha de devolucion : {self.__fechaDevolucion}")
        print("Estudiante: ", end="")
        self.__estudiante.mostrarInfo()
        print("Libro: ", end="")
        self.__libro.leer() 

class Estudiante:
    def __init__(self, codigo, nombre):
        self.__nombre = nombre
        self.__codigo = codigo

    def mostrarInfo(self):
        print(f"{self.__nombre}, Codigo : {self.__codigo}")



def app():
    mi_biblioteca = Biblioteca("Biblioteca Central UMSA", "Lunes a Viernes", "08:00", "20:00")

    autor1 = Autor("Franz Tamayo", "Boliviano")
    mi_biblioteca.agregarAutor(autor1)

    contenidos = ["Introducción a la POO", "Herencia y Polimorfismo", "Fin del capítulo"]
    libro1 = Libro("Aprende Python", "978-123", contenidos)

    mi_biblioteca.agregarLibro(libro1)

    estudiante1 = Estudiante("INF-2026", "Henry Dario Chipana Ergueta")

    mi_biblioteca.prestarLibro(libro1, estudiante1)

    mi_biblioteca.mostrarEstado()
    mi_biblioteca._Biblioteca__listaPrestamosActivos[0].mostrarInfo()
    mi_biblioteca.cerrarBiblioteca()
app()