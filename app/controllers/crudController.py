from app import app, db, Messages
from flask import request, jsonify, render_template


@app.route("/crud/add")
def crudAdd():  
    return render_template("crud/add.html")

@app.route("/crud/login", methods=["GET", "POST"])
def crudLogin():   
	error = ''
	if request.method == "POST":
		nome = request.form['nome']
		email = request.form['email']
		print (nome,email)
	return render_template("crud/add.html")

@app.route("/crud/home", methods=["GET", "POST"])
def crudHome():   
    return render_template("crud/home.html")

@app.route("/crud/edit", methods=["GET", "POST"])
def crudEdit():   
    return render_template("crud/edit.html")

@app.route("/crud/ngc", methods=["GET", "POST"])
def crudNgc():   
    return render_template("crud/ngc.html")
