from flask import Flask
from admin import admin
from auth import auth

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(auth)

app.secret_key = "senha_secreta"

@app.route("/")
def index():
    return "Pagina principal"

if __name__ == '__main__':
    app.run(debug=True)