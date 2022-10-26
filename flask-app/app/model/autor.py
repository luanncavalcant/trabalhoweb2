from app import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    nascimento = db.Column(db.Date, nullable=False)
    post = db.relationship("Post", backref="autor", lazy=True)

    def __init__(self, nome, nascimento):
        self.nome=nome 
        self.nascimento = nascimento

    def __repr__(self):
        str= "<Autor{} {} {}.".format(self.id, self.nome, self.nascimento)  
        return str

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            'nascimento': self.nascimento
        }