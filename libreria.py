import json

class Libreria:
    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))

import json

class Libreria:
    """
    Clase para gestionar una colección de libros.

    Atributos:
        libros (list): Lista que almacena los libros como diccionarios con información sobre título, autor, género y año.

    Métodos:
        __init__(self): Constructor que inicializa la lista `libros` vacía.
        anadir_libro(self, titulo, autor, genero, anio):
            Agrega un nuevo libro a la lista `libros`.
            Retorna un mensaje de confirmación.
        buscar_libro(self, titulo):
            Busca libros por título (coincidencia no sensible a mayúsculas).
            Retorna una lista de libros que coincidan con la búsqueda.
            Si no se encuentra ningún libro, retorna una lista vacía.
        buscar_por_autor(self, autor):
            Busca libros por autor (coincidencia no sensible a mayúsculas).
            Retorna una lista de libros escritos por el autor especificado.
            Si no se encuentra ningún libro del autor, retorna una lista vacía.
        eliminar_libro(self, titulo):
            Elimina un libro de la lista por título (coincidencia no sensible a mayúsculas).
            Retorna un mensaje indicando si el libro se eliminó o no.
        guardar_libros(self, archivo):
            Guarda la lista de libros en un archivo JSON especificado.
            Retorna un mensaje de confirmación.
        cargar_libros(self, archivo):
            Carga una lista de libros desde un archivo JSON especificado.
            Actualiza la lista de libros `libros` con los datos del archivo.
            Retorna un mensaje indicando si la carga fue exitosa o no.
    """

    def __init__(self):
        """
        Constructor que inicializa la lista `libros` vacía.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Agrega un nuevo libro a la lista `libros`.

        Argumentos:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.

        Retorno:
            str: Mensaje de confirmación.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca libros por título (coincidencia no sensible a mayúsculas).

        Argumento:
            titulo (str): Título del libro a buscar.

        Retorno:
            list: Lista de libros que coincidan con la búsqueda.
            Si no se encuentra ningún libro, retorna una lista vacía.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por autor (coincidencia no sensible a mayúsculas).

        Argumento:
            autor (str): Autor de los libros a buscar.

        Retorno:
            list: Lista de libros escritos por el autor especificado.
            Si no se encuentra ningún libro del autor, retorna una lista vacía.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la lista por título (coincidencia no sensible a mayúsculas).

        Argumento:
            titulo (str): Título del libro a eliminar.

        Retorno:
            str: Mensaje indicando si el libro se eliminó o no.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON especificado.

        Argumento:
            archivo (str): Ruta del archivo JSON donde se guardarán los libros.

        Retorno:
            str: Mensaje de confirmación.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    
    def cargar_libros(self, archivo):
        """
        Carga una lista de libros desde un archivo JSON especificado.

        Argumento:
            archivo (str): Ruta del archivo JSON donde se encuentran los libros.

        Retorno:
            str: Mensaje indicando si la carga fue exitosa o no.
        """
    try:
        with open(archivo, 'r') as f:
            self.libros = json.load(f)
        return "Libros cargados"
    except FileNotFoundError:
        return "Archivo no encontrado"

# Ejemplo de uso
mi_libreria = Libreria()

# Añadir libros
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.anadir_libro("El coronel no tiene quien le escriba", "Gabriel García Márquez", "Novela", 1961)
mi_libreria.anadir_libro("Rayuela", "Julio Cortázar", "Novela", 1963")

# Buscar libros
libros_buscados = mi_libreria.buscar_libro("Cien años de soledad")
print(f"Libros encontrados por título: {libros_buscados}")

libros_autor = mi_libreria.buscar_por_autor("Gabriel García Márquez")
print(f"Libros del autor Gabriel García Márquez: {libros_autor}")

# Eliminar libro
titulo_eliminar = "Rayuela"
mensaje_eliminacion = mi_libreria.eliminar_libro(titulo_eliminar)
print(f"Resultado de eliminar '{titulo_eliminar}': {mensaje_eliminacion}")

# Guardar libros en archivo JSON
archivo_guardar = "libreria.json"
mensaje_guardar = mi_libreria.guardar_libros(archivo_guardar)
print(f"Resultado de guardar libros en '{archivo_guardar}': {mensaje_guardar}")

# Cargar libros desde archivo JSON
archivo_cargar = "libreria.json"
mensaje_cargar = mi_libreria.cargar_libros(archivo_cargar)
print(f"Resultado de cargar libros desde '{archivo_cargar}': {mensaje_cargar}")