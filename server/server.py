from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


def carregar_areas_atuacao():
    caminho_json = os.path.join('data', 'areas-atuacao.json')
    try:
        with open(caminho_json, 'r', encoding='utf-8') as arquivo: 
            return json.load(arquivo)
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return []
    
def carregar_consultas():
    caminho_json = os.path.join('data', 'lista-consultas.json')
    try:
        with open(caminho_json, 'r', encoding='utf-8') as arquivo: 
            return json.load(arquivo)
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return []

@app.route('/areas-atuacao', methods=['GET'])
def obter_areas():
    dados = carregar_areas_atuacao()
    if not dados: 
        return jsonify({"error": "Dados não encontrados"}), 404
    return jsonify(dados)

@app.route('/consulta', methods=['GET'])
def listar_consultas():
    dados = carregar_consultas()
    if not dados: 
        return jsonify({"error":
                         "Dados não encontrados"}), 404
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 