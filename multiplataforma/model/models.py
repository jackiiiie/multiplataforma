import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)





# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import Relationship, Session, relationship

# from multiplataforma.config.database import Base, engine

# class Usuario(Base):
#     __tablename__ = "usuarios"
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     nome = Column(String(50))
#     email = Column(String(50))
#     senha = Column(String(11))
#     endereco_id = Column(Integer, ForeignKey("enderecos.id", ondelete="CASCADE", onupdate="CASCADE"))
#     endereco = relationship("Endereco", back_populates="usuarios", uselist=False)

#     @staticmethod
#     def create(session: Session, **kwargs):
#         user = Usuario(**kwargs)
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         return user

#     @staticmethod
#     def update(session: Session, user_id: int, **kwargs):
#         user = Usuario.read(session, user_id)
#         for key, value in kwargs.items():
#             setattr(user, key, value)
#         session.commit()
#         session.refresh(user)
#         return user

#     @staticmethod
#     def delete(session: Session, user_id: int):
#         user = Usuario.read(session, user_id)
#         session.delete(user)
#         session.commit()
#         return user_id

#     @staticmethod
#     def read(session: Session, user_id: int):
#         return session.query(Usuario).filter(Usuario.id == user_id).first()
# # Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


# class Usuario(Base):
#     __tablename__ = 'usuarios'

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String(50))
#     email = Column(String(50), unique=True)
#     password = Column(String(50))
#     cpf = Column(String(11), unique=True)
#     phone = Column(String(11))

#     def __repr__(self):
#         return f'<User(id={self.id}, name={self.name}, email={self.email}, password={self.password}, cpf={self.cpf}, phone={self.phone})>'

# Base.metadata.drop_all(bind=engine) #colocar apenas em anbiente de dev nunca no trabalho
# Base.metadata.create_all(bind=engine) #colocar apenas em anbiente de dev nunca no trabalho