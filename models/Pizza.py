from utils import db

class Pizza(db.Model):
    __tablename__="pizza"
    id = db.Column(db.Integer, primary_key = True)
    sabor = db.Column(db.String(280))
    imagem = db.Column(db.String(280))
    ingredientes = db.Column(db.String(280))
    preco=db.Column(db.Float)

    def __init__(self, sabor, imagem, ingredientes, preco):
        self.sabor = sabor
        self.imagem = imagem
        self.ingredientes = ingredientes
        self.preco = preco
    
    def __repr__(self):
        return "<Pizza {}>".format(self.sabor)