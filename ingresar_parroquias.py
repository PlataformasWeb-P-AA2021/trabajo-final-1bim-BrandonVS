import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Canton, Parroquia

from configuracion import cadena_base

# Se genera el enlace al gestor de base de datos usando la variable creada en configuracion
engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Se abre el archivo donde se encuentran todos los datos
read =  open('data/Listado-instituciones-Educativas.csv', 'r', encoding='utf-8')

# Se lo lee y guarda como un csv usando la libreria csv de python
csv = csv.reader(read, delimiter='|')

# Se salta el encabezado
next(csv)

# Se guarda cada una de las lineas del csv en una lista
parroquia_csv = list(csv)
cont = 0

# Se guardan en una tupla solamente las columnas necesarias para parroquia
for row in parroquia_csv:
    parroquia_csv[cont] = tuple(row[i] for i in [4, 6, 7])
    cont += 1

# Se eliminan los duplicados con el metodo set() y se lo vuelve a declarar como lista para mayor facilidad
parroquias = list(set(parroquia_csv))

# Se guardan los datos en la tabla Parroquia
for parr in parroquias:
    parr = Parroquia(parroquia_id=int(parr[1]), parroquia_name=parr[2], canton=session.query(Canton)
                     .filter_by(canton_id=parr[0]).one())
    session.add(parr)
session.commit()
