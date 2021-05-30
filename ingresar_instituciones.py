import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Institucion, Parroquia

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
institucion_csv = list(csv)
cont = 0

# Se guardan en una tupla solamente las columnas necesarias para instituciones
for row in institucion_csv:
    institucion_csv[cont] = tuple(row[i] for i in [0, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15])
    cont += 1

# Se eliminan los duplicados con el metodo set() y se lo vuelve a declarar como lista para mayor facilidad
instituciones = list(set(institucion_csv))

# Se guardan los datos en la tabla Institucion
for i in instituciones:
    i = Institucion(institucion_id=i[0], inst_name=i[1], distrito=i[3], sostenimiento=i[4], tipo_edu=i[5],
                    modalidad=i[6], jornada=i[7], acceso=i[8], n_estudiantes=int(i[9]), n_profesores=int(i[10]),
                    parroquia=session.query(Parroquia).filter_by(parroquia_id=i[2]).one())
    session.add(i)
session.commit()
