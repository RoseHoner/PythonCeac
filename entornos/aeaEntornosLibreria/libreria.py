import json

class Libreria:
    """
    Gestiona una colección de libros, permitiendo añadir, buscar, eliminar,
    y guardar o cargar los libros desde un archivo en formato JSON.
    """

    def __init__(self):
        """Inicializa la librería con una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la librería.
        
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.
        
        Returns:
            str: Mensaje confirmando que el libro fue añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 
                            'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca libros por su título exacto.
        
        Args:
            titulo (str): El título del libro a buscar.
        
        Returns:
            list: Lista de libros que coinciden con el título buscado.
        """
        return [libro for libro in self.libros if
                libro['titulo'].lower() == titulo.lower()]
    
    

    def buscar_por_autor(self, autor):
        """
        Busca libros que contengan el nombre del autor dado.
        
        Args:
            autor (str): El nombre del autor a buscar.
        
        Returns:
            list: Lista de libros que contienen el nombre del autor dado.
        """
        return [libro for libro in self.libros if
                autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por título.
        
        Args:
            titulo (str): El título del libro a eliminar.
        
        Returns:
            str: Mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if
                       libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON.
        
        Args:
            archivo (str): Ruta del archivo JSON donde guardar los libros.
        
        Returns:
            str: Mensaje indicando que los libros fueron guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la lista de libros desde un archivo JSON.
        
        Args:
            archivo (str): Ruta del archivo JSON a cargar.
        
        Returns:
            str: Mensaje indicando si los libros fueron cargados o el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"
    def actualizar_libro(self, titulo_original, titulo_nuevo,
                         autor_nuevo, genero_nuevo, anio_nuevo):
        """
        Actualiza la información de un libro existente.

        Args:
            titulo_original (str): El título actual del libro.
            titulo_nuevo (str): El nuevo título del libro.
            autor_nuevo (str): El nuevo autor del libro.
            genero_nuevo (str): El nuevo género del libro.
            anio_nuevo (int): El nuevo año de publicación del libro.
        
        Returns:
            str: Mensaje indicando si la actualización fue exitosa o el libro no fue encontrado.
        """
        for libro in self.libros:
            if libro['titulo'].lower() == titulo_original.lower():
                libro['titulo'] = titulo_nuevo
                libro['autor'] = autor_nuevo
                libro['genero'] = genero_nuevo
                libro['anio'] = anio_nuevo
                return "Libro actualizado"
        return "Libro no encontrado"