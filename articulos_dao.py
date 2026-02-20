import logging


class ArticulosDao:
    """Acceso a datos de artículos en fichero de texto plano."""

    def __init__(self, filename="articulos.dat"):
        self.filename = filename
        self.config_log()

    def config_log(self):
        log_file = "articulos.log"
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def _dict_to_str(self, articulo: dict) -> str:
        observaciones = str(articulo.get('observaciones', '')).replace('\n', ' ')
        return (
            f"{articulo.get('referencia', '')}|"
            f"{articulo.get('descripcion', '')}|"
            f"{articulo.get('precio', '')}|"
            f"{articulo.get('stock', '')}|"
            f"{observaciones}"
        )

    @staticmethod
    def str_to_dict(articulo_str: str):
        if not articulo_str:
            return None
        articulo_arr = articulo_str.split("|")
        if len(articulo_arr) != 5:
            return None
        try:
            return {
                "referencia": articulo_arr[0],
                "descripcion": articulo_arr[1],
                "precio": float(articulo_arr[2]),
                "stock": int(float(articulo_arr[3])),
                "observaciones": articulo_arr[4]
            }
        except ValueError:
            return None

    def get_all(self) -> list:
        articulos = []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for linea in f:
                    articulo = self.str_to_dict(linea.strip())
                    if articulo:
                        articulos.append(articulo)
        except FileNotFoundError:
            return []
        except Exception as e:
            self.logger.error(f"Error al leer artículos: {e}")
        return articulos

    def _save_all(self, articulos: list) -> bool:
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for articulo in articulos:
                    f.write(self._dict_to_str(articulo) + "\n")
            return True
        except Exception as e:
            self.logger.error(f"Error al guardar artículos: {e}")
            return False

    def save(self, articulo: dict) -> bool:
        articulos = self.get_all()
        for existente in articulos:
            if existente.get("referencia") == articulo.get("referencia"):
                return False
        articulos.append(articulo)
        return self._save_all(articulos)

    def find(self, referencia_buscada: str):
        for articulo in self.get_all():
            if articulo.get("referencia") == referencia_buscada:
                return articulo
        return None

    def delete(self, referencia_buscada: str) -> bool:
        articulos = self.get_all()
        original = len(articulos)
        articulos = [a for a in articulos if a.get("referencia") != referencia_buscada]
        if len(articulos) == original:
            return False
        return self._save_all(articulos)

    def update(self, articulo_modificado: dict) -> bool:
        articulos = self.get_all()
        referencia = articulo_modificado.get("referencia")
        actualizado = False
        for i, articulo in enumerate(articulos):
            if articulo.get("referencia") == referencia:
                articulos[i] = articulo_modificado
                actualizado = True
                break
        if not actualizado:
            return False
        return self._save_all(articulos)
