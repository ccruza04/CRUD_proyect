import logging

'''
OBSERVACIÓN: SI ALGUN CAMPO TIENE \n no SE GUARDARÁ CORRECTAMENTE
'''

class ArticulosDao:
    """
    Clase para manejar el almacenamiento de artículos en un fichero de texto.

    Esta clase permite guardar artículos representados como diccionarios en un archivo,
    y registra errores en un archivo de log si ocurre algún problema durante la escritura.

    Cada artículo se guarda en una línea del fichero, separando los campos con '|'.
    """

    def __init__(self, filename="articulos.dat"):
        """
        Inicializa el DAO con el nombre del fichero de datos y configura el logger.

        Args:
            filename (str, optional): Nombre del archivo donde se guardarán los artículos.
                                      Por defecto es 'articulos.dat'.
        """
        self.filename = filename
        self.config_log()

    def config_log(self):
        """
        Configura el logger para registrar eventos y errores en un archivo de log.

        El log se guarda en 'articulos.log' con nivel INFO y formato de fecha/hora,
        nivel de log y mensaje.
        """
        log_file = "articulos.log"
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def save(self, articulo: dict) -> bool:
        """
        Guarda un artículo en el fichero.

        Args:
            articulo (dict): Diccionario con los campos del artículo:
                             'referencia', 'descripcion', 'precio', 'stock', 'observaciones'.

        Returns:
            bool: True si el artículo se guardó correctamente, False si hubo un error.

        Ejemplo:
            dao = ArticulosDao()
            articulo = {
                "referencia": "A001",
                "descripcion": "Lápiz",
                "precio": 0.5,
                "stock": 100,
                "observaciones": "Sin observaciones"
            }
            dao.save(articulo)
        """
        try:
            with open(self.filename, "a") as f:
                f.write(f"{articulo.get('referencia','')}|"
                        f"{articulo.get('descripcion','')}|"
                        f"{articulo.get('precio','')}|"
                        f"{articulo.get('stock','')}|"
                        f"{articulo.get('observaciones','')}\n")
                return True
        except Exception as e:
            self.logger.error(f"Error al guardar artículo {articulo.get('referencia','')}: {e}")
            return False

    def find(self, referencia_buscada: str) -> dict:
        """
        Consulta un artículo en el fichero segun la referencia.

        Args:
            referencia_buscada (str): Referencia del articulo buscado.

        Returns:
            articulo (dict): - Diccionario con los campos del artículo:
                                'referencia', 'descripcion', 'precio', 'stock', 'observaciones'.
                             - Devuelve None si no existe.

        Ejemplo:
            dao = ArticulosDao()
            articulo = {
                "referencia": "A001",
                "descripcion": "Lápiz",
                "precio": 0.5,
                "stock": 100,
                "observaciones": "Sin observaciones"
            }
            dao.save(articulo)
        """
        try:
            with open(self.filename, "r") as f:
                articulo_str = f.readline().strip()
                articulo = self.str_to_dict(articulo_str)
                while articulo and articulo.get("referencia") != referencia_buscada:
                    articulo_str = f.readline().strip()
                    articulo = self.str_to_dict(articulo_str)

                if articulo:
                    return articulo
        except Exception as e:
            self.logger.error(f"Error al buscar artículo {referencia_buscada}: {e}")

        return None

    @staticmethod
    def str_to_dict(articulo_str):
        articulo_arr = articulo_str.split("|")
        articulo = {
            "referencia": articulo_arr[0],
            "descripcion": articulo_arr[1],
            "precio": float(articulo_arr[2]),
            "stock": float(articulo_arr[3]),
            "observaciones": articulo_arr[4]
        }
        return articulo
