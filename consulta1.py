from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from configuracion import cadena_base
from generar_tablas import Provincia, Canton, Parroquia, Institucion

engine = create_engine(cadena_base)

Session = sessionmaker(bind=engine)
session = Session()

# Todos los establecimientos de la provincia de Loja.
consulta1 = session.query(Institucion).join(Parroquia, Canton, Provincia).filter(
    Provincia.prov_name == "LOJA").order_by(Institucion.inst_name.asc()).all()

# Todos los establecimientos de la provincia de Loja.
consulta11 = session.query(Institucion).join(Parroquia, Canton, Provincia).filter(
    Canton.canton_name == "LOJA").order_by(Institucion.inst_name.asc()).all()

print("Establecimientos de la provincia de Loja")
print(consulta1)
print("Establecimientos del canton Loja")
print(consulta11)
