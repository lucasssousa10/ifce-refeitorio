from app import db
from sqlalchemy.orm import validates


class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    
    # --------------------------------------------------------------------------------------------------#

    def __init__(self, nome, cliente_id):
        self.nome = nome
        self.cliente_id = cliente_id
        
    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Produto %s>" % (self.nome)