from app import db

class Livro(db.Model):
    __tablename__ = "livro"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    
    # --------------------------------------------------------------------------------------------------#

    def __init__(self, nome):
        self.nome = nome
        
    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Livro %s>" % (self.nome)
