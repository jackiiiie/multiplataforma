import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, root_dir)

from sqlalchemy.orm import Session

from multiplataforma.domain.model.models import Usuario


class UsuarioRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: Usuario):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: Usuario):
        self.session.delete(user)
        self.session.commit()

    def read(self, user_id: int):
        return self.session.query(Usuario).filter(Usuario.id == user_id).first()

    def find_all(self):
        return self.session.query(Usuario).all()