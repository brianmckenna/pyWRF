from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

# -- &physics
class mp_physics(Base):
    __tablename__ = 'mp_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)

class ra_lw_physics(Base):
    __tablename__ = 'ra_lw_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)

class ra_sw_physics(Base):
    __tablename__ = 'ra_sw_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)

class sf_sfclay_physics(Base):
    __tablename__ = 'sf_sfclay_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
 
class sf_surface_physics(Base):
    __tablename__ = 'sf_surface_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)

class bl_pbl_physics(Base):
    __tablename__ = 'bl_pbl_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)

class cu_physics(Base):
    __tablename__ = 'cu_physics'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)

 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
