# '''
# pip install faker
# '''
# import random
# from dao.articulos_dao import ArticulosDao
# from faker import Faker
#
# fake = Faker("es_ES")
#
# # print(fake.name())
# # print(fake.company())
# # print(fake.address())
# # print(fake.city())
# # print(fake.phone_number())
# # print(fake.street_address())
# def generar_articulo():
#     return {
#         "referencia": fake.bothify(text="???####").upper(),
#         "descripcion": fake.sentence(nb_words=10).capitalize(),
#         "precio": round(random.uniform(1, 200), 2),
#         "stock": random.randint(0, 500),
#         "observaciones": fake.sentence()
#     }
# print(generar_articulo())
# dao = ArticulosDao()
# dao.delete_all()
#
# total=10000
# for _ in range(0, total +1 ):
#     articulo = generar_articulo()
#     dao.save(articulo)
#     porcentaje = (i / total) * 100
#     # print(f"Generando articulo {i}/{total} ({porcentaje:.1f}%)"
#     #       end="\r", flush=True)
#     sys.stdout.write(f"Generando articulo {i}/{total} ({porcentaje:.1f}%)"
#           end="\r", flush=True)

import random
import sys
from dao.articulos_dao import ArticulosDao
from faker import Faker

fake = Faker("es_ES")

def generar_articulo():
    return {
        "referencia": fake.bothify(text="???####").upper(),
        "descripcion": fake.sentence(nb_words=10).capitalize(),
        "precio": round(random.uniform(1, 200), 2),
        "stock": random.randint(0, 500),
        "observaciones": fake.sentence()
    }

print(generar_articulo())

dao = ArticulosDao()
dao.delete_all()

total = 10000
for i in range(total + 1):
    articulo = generar_articulo()
    dao.save(articulo)
    porcentaje = (i / total) * 100
    print(f"Generando articulo {i}/{total} ({porcentaje:.1f}%)", end="\r", flush=True)


