from flask import Flask, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()

# Renderiza la página de inicio
@app.route("/", methods=["GET", "POST"])
def index():
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

