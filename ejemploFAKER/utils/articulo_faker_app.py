from dao.articulos_dao import ArticulosDao
from utils.articulo_faker import ArticuloFaker

dao = ArticulosDao()
articulos = ArticuloFaker.generar_lote(100)

print(articulos)

for articulo in articulos:
     dao.save(articulo)