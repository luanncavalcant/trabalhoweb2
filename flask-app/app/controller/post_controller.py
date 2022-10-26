from crypt import methods
from app import app, db, Post
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

@app.route("/post/add", methods= ["POST"])
def post_add():
    data = request.get_json()

    post = Post(
    titulo = data ["titulo"],
    conteudo = data ["conteudo"],
    autor_id = data ["autor_id"])

    db.session.add(post)

    try:
        db.session.commit()

    except(IntegrityError):
        return jsonify({"error": True, "mensage": "ocorreu um error"})

    return jsonify ({"error":False, "menssagem": "Post criado com sucesso" })

@app.route("/post/edit/<id>", methods= ["PUT"])
def post_edit(id):
    data = request.get_json()
    post = Post.query.get(id)

    if post is None:
        return jsonify({
            "mensage": "Não Encontrado",
            "error": True
        }), 404
    print(data)
    post.titulo = data["titulo"]
    post.conteudo = data ["conteudo"]
    post.autor_id = data["autor_id"]


    try:
        db.session.commit()

    except(IntegrityError):
        return jsonify({"error": True, "mensage": "ocorreu um error"})

    return jsonify ({"error":False, "menssagem": "Post criado com sucesso" })


@app.route("/post/delete/<id>", methods = ["DELETE"])
def post_delete(id):
    post = Post.query.get(id)
    if post is None:
        return jsonify({
            "mensage": "Não Encontrado",
            "error": True
        }), 404

    db.session.delete(post)
    try:
        db.session.commit()

    except(IntegrityError):
        return jsonify({"error": True, "mensage": "ocorreu um error"})

    return jsonify ({"error":False, "menssagem": "Autor deletado com sucesso" })


@app.route("/post/view/<id>", methods = ["VIEW"])
def post_view(id):
    post = Post.query.get(id)
    if post is None:
        return jsonify({
            "mensage": "Não Encontrado",
            "error": False
        }), 405
        
    return jsonify  ({
        "data": post.to_dict(),
        "error":False
    })

@app.route("/post/list", methods=["GET"])
def post_list():
    postes = Post.query.all()
    output ={"data": [], "error": False}

    for post in postes :
        output["data"].append(post.to_dict())
    
    return jsonify(output)