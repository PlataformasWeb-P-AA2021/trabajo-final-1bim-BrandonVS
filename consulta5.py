from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from configuracion import cadena_base
from generar_tablas import Provincia, Canton, Parroquia, Institucion

engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en
# tipo de educación.
consulta2 = session.query(Institucion).filter(and_(Institucion.n_profesores >= 20,
                                                   Institucion.tipo_edu == "Permanente"))\
                                                   .order_by(Institucion.n_profesores.asc()).all()

# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.
consulta21 = session.query(Institucion).filter(Institucion.distrito == "11D02")\
    .order_by(Institucion.sostenimiento.asc()).all()

print("Consulta 1")
print(consulta2)
print("Consulta 2")
print(consulta21)
