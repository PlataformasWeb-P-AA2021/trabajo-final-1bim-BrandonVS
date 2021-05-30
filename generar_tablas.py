from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base

# Se trae el gestor de base de datos que se declaro en configuracion
engine = create_engine(cadena_base)

Base = declarative_base()

# Se crea la tabla provincia
class Provincia(Base):
    __tablename__ = 'provincia'
    provincia_id = Column(Integer, primary_key=True)
    prov_name = Column(String(50))

    # Se declara la relacion con la tabla canton
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "\nProvincia: id = %s Nombre = %s\n\n" % (self.provincia_id, self.prov_name)

# Se crea la tabla canton
class Canton(Base):
    __tablename__ = 'canton'
    canton_id = Column(Integer, primary_key=True)
    canton_name = Column(String(50))

    provincia_id = Column(Integer, ForeignKey('provincia.provincia_id'))

    # Se declara la relacion con la tabla provincia
    provincia = relationship("Provincia", back_populates="cantones")
    # Se declara la relacion con la tabla parroquias
    parroquias = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "\nCanton: Nombre = %s\n\n" % self.canton_name

# Se crea la tabla parroquia
class Parroquia(Base):
    __tablename__ = 'parroquia'
    parroquia_id = Column(Integer, primary_key=True)
    parroquia_name = Column(String(50))

    canton_id = Column(Integer, ForeignKey('canton.canton_id'))

    # Se declara la relacion con la tabla canton
    canton = relationship("Canton", back_populates="parroquias")
    # Se declara la relacion con la tabla institucion
    instituciones = relationship("Institucion", back_populates="parroquia")

    def __repr__(self):
        return "\nParroquia: Nombre = %s\n\n" % self.parroquia_name

# Se crea la tabla institucion
class Institucion(Base):
    __tablename__ = 'institucion'
    institucion_id = Column(String, primary_key=True)
    inst_name = Column(String(100))
    distrito = Column(String(10))
    sostenimiento = Column(String(50))
    tipo_edu = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    n_estudiantes = Column(Integer)
    n_profesores = Column(Integer)

    parroquia_id = Column(Integer, ForeignKey('parroquia.parroquia_id'))
    # Se declara la relacion con la tabla parroquia
    parroquia = relationship("Parroquia", back_populates="instituciones")

    def __repr__(self):
        return "\nInstitucion: Nombre = %s\nDistrito: %s\nSotenimiento: %s\nTipo educación: %s\nModalidad: %s\nJornada: "\
               "%s\nAcceso: %s\nNúmero de estudiantes: %s\nNúmero de profesores: %s\n\n" % (self.inst_name,
                                                                                            self.distrito,
                                                                                            self.sostenimiento,
                                                                                            self.tipo_edu,
                                                                                            self.modalidad,
                                                                                            self.jornada,
                                                                                            self.acceso,
                                                                                            self.n_estudiantes,
                                                                                            self.n_profesores)

# Se crea la base de datos
Base.metadata.create_all(engine)
