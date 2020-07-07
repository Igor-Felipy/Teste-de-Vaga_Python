from flask import Flask, jsonify
import consult

app = Flask(__name__)

@app.route("/")
def running():
    return "RUNNING"

@app.route("/<string:cpf>")
def get_cpf(cpf):
    return consult.response_cpf(cpf)


if __name__ == "__main__":
    app.run(debug=True)