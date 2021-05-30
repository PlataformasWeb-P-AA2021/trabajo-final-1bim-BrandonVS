from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from configuracion import cadena_base
from generar_tablas import Provincia, Canton, Parroquia, Institucion

engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
consulta2 = session.query(Institucion).filter(Institucion.n_profesores >= 100)\
    .order_by(Institucion.n_estudiantes.asc()).all()

# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
consulta21 = session.query(Institucion).filter(Institucion.n_profesores >= 100)\
    .order_by(Institucion.n_profesores.asc()).all()

print("Consulta 1")
print(consulta2)
print("Consulta 2")
print(consulta21)
