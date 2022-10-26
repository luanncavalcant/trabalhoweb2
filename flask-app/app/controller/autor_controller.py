from crypt import methods
from pickle import PUT, TRUE
from sqlite3 import IntegrityError
from app import app, db, Autor
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from datetime import datetime

@app.route("/autor/add", methods=["POST"])
def autor_add():
    data = request.get_json()
    
    autor = Autor( 
    nome = data["nome"],
    nascimento = datetime.strptime(data["nascimento"], "%Y-%m-%d"))

    db.session.add(autor)

    try:
        db.session.commit()

    except(IntegrityError):
        return jsonify({"error": True, "mensage": "ocorreu um error"})

    return jsonify ({"error":False, "menssagem": "Autor criado com sucesso" })


@app.route("/autor/edit/<id>", methods = ["PUT"])
def autor_edit(id):
    data = request.get_json()
    autor = Autor.query.get(id)
    if autor is None:
        return jsonify({
            "mensage": "Não Encontrado",
            "error": True
        }), 404

    autor.nome = data["nome"]
    try:
        db.session.commit()

    except(IntegrityError):
        return jsonify({"error": True, "mensage": "ocorreu um error"})

    return jsonify ({"error":False, "menssagem": "Autor editado com sucesso" })


@app.route("/autor/delete/<id>", methods = ["DELETE"])
def autor_delete(id):
    autor = Autor.query.get(id)
    if autor is None:
        return jsonify({
            "mensage": "Não Encontrado",
            "error": True
        }), 404

    db.session.delete(autor)
    try:
        db.session.commit()

    except(IntegrityError):
        return jsonify({"error": True, "mensage": "ocorreu um error"})

    return jsonify ({"error":False, "menssagem": "Autor deletado com sucesso" })



@app.route("/autor/view/<id>", methods = ["VIEW"])
def autor_view(id):
    autor = Autor.query.get(id)
    if autor is None:
        return jsonify({
            "mensage": "Não Encontrado",
            "error": True
        }), 404
    return jsonify ({
        "data":autor.to_dict(),
        "error":False
    })


@app.route("/autor/list", methods = ["GET"])
def autor_list():
    autores = Autor.query.all()
    output ={"data":[], "error":False}

    for autor in autores:
        output["data"].append(autor.to_dict())

    return jsonify(output)