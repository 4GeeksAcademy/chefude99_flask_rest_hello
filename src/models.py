from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()
class Usuario_instagram(db.Model):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_de_usuario: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(10), nullable=False)
    apellido: Mapped[str] = mapped_column(String(15), nullable=False)
    correo: Mapped[str] = mapped_column(
        String(50), primary_key=True, unique=True)
    comentario: Mapped[list['Comentario']
                  ] = relationship(back_populates='comentario_id')
    


class Comentario(db.Model):
    __tablename__ = 'comentario'
    id: Mapped[int] = mapped_column(primary_key=True)
    texto_comentario: Mapped[str] = mapped_column(String(200), nullable=False)
    autor_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    comentario_id: Mapped['Usuario_instagram'] = relationship(back_populates='comentario')


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
