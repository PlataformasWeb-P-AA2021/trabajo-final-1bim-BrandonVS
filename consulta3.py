from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from configuracion import cadena_base
from generar_tablas import Provincia, Canton, Parroquia, Institucion

engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Los cantones que tiene establecimientos con 0 número de profesores
consulta2 = session.query(Canton).join(Parroquia, Institucion).filter(Institucion.n_profesores == 0).order_by(
    Canton.canton_name.asc()).all()

# Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
consulta21 = session.query(Institucion).join(Parroquia).filter(and_(Parroquia.parroquia_name == "CATACOCHA",
                                                                    Institucion.n_estudiantes >= 21))\
                                                                    .order_by(Institucion.inst_name.asc()).all()

print("Consulta 1")
print(consulta2)
print("Consulta 2")
print(consulta21)
