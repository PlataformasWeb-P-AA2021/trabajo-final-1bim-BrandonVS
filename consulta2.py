from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, distinct

from configuracion import cadena_base
from generar_tablas import Provincia, Canton, Parroquia, Institucion

engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
consulta2 = session.query(Parroquia).join(Institucion).filter(Institucion.jornada == "Nocturna").order_by(
    Parroquia.parroquia_name.asc()) \
    .all()

# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
consulta21 = session.query(Canton).join(Parroquia, Institucion).filter(
    or_(Institucion.n_estudiantes == 448, Institucion.n_profesores == 448,
        Institucion.n_estudiantes == 450, Institucion.n_profesores == 450,
        Institucion.n_estudiantes == 451, Institucion.n_profesores == 451,
        Institucion.n_estudiantes == 454, Institucion.n_profesores == 454,
        Institucion.n_estudiantes == 458, Institucion.n_profesores == 458,
        Institucion.n_estudiantes == 459, Institucion.n_profesores == 459)) \
    .order_by(Canton.canton_name.asc()).all()

print("Consulta 1")
print(consulta2)
print("Consulta 2")
print(consulta21)
