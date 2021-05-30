import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Provincia

from configuracion import cadena_base

# Se genera el enlace al gestor de base de datos usando la variable creada en configuracion
engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Se abre el archivo donde se encuentran todos los datos
read = open('data/Listado-instituciones-Educativas.csv', 'r', encoding='utf-8')

# Se lo lee y guarda como un csv usando la libreria csv de python
csv = csv.reader(read, delimiter='|')

# Se salta el encabezado
next(csv)

# Se guarda cada una de las lineas del csv en una lista
prov_csv = list(csv)
cont = 0

# Se guardan en una tupla solamente las columnas necesarias para provincias
for row in prov_csv:
    prov_csv[cont] = tuple(row[i] for i in [2, 3])
    cont += 1

# Se eliminan los duplicados con el metodo set() y se lo vuelve a declarar como lista para mayor facilidad
provincias = list(set(prov_csv))

# Se guardan los datos en la tabla Provincia
for p in provincias:
    p = Provincia(provincia_id=int(p[0]), prov_name=p[1])
    session.add(p)
session.commit()
