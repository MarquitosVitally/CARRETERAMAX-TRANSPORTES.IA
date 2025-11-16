from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/ingresar", methods=["POST"])
def ingresar():
    usuario = request.form["usuario"]
    correo = request.form["correo"]
    contraseña = request.form["contraseña"]

    # Aquí puedes validar el login si quieres
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
