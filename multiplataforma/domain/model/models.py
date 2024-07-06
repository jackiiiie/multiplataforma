import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, root_dir)
from sqlalchemy import Column, Integer, String

from multiplataforma.config.database import Base, engine


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(50))
    cpf = Column(String(11), unique=True)
    phone = Column(String(11))

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name}, email={self.email}, password={self.password}, cpf={self.cpf}, phone={self.phone})>'

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)