from flask import Flask, request, jsonify, after_this_request
from model.classifier import tratar_texto, treinar_modelo

app = Flask(__name__)
MODELO = treinar_modelo()


@app.route("/analise", methods=["GET"])
def chamar_analise():
    @after_this_request
    def add_header(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    texto = request.args.get("texto", "").strip()
    if not texto:
        return jsonify({"erro": "Parâmetro 'texto' é obrigatório."}), 400

    predicao = MODELO.predict([tratar_texto(texto)])[0]
    return jsonify({"racista": str(predicao)})


if __name__ == "__main__":
    app.run(host="localhost", port=8989, debug=True)