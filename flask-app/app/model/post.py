from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo= db.Column(db.Text, nullable =False)
    conteudo = db.Column(db.Text, nullable = False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'),nullable=False)

    def __init__(self, titulo, conteudo, autor_id):
        self.titulo = titulo
        self.conteudo = conteudo
        self.autor_id = autor_id

    def __repr__(self):
        str= "<Post{} {}.".format(self.id, self.titulo, self.conteudo)  
        return str

    def to_dict(self):
        return{
            "id": self.id,
            "titulo": self.titulo,
            'conteudo': self.conteudo,
            'autor_id': self.autor_id
        }
