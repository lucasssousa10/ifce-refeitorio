from app import db
from sqlalchemy.orm import validates


class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    produtos = db.relationship("Produto", backref="cliente", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, nome):
        self.nome = nome
        
    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Cliente %s>" % (self.nome)