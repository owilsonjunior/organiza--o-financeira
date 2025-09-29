from app import app
from flask import request, jsonify

@app.route('/')
def home():
    return 'Backend da Organização Financeira está online!'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Lógica de autenticação temporária (NÃO USE EM PRODUÇÃO)
    if username == 'admin' and password == 'admin':
        return jsonify({"message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"message": "Credenciais inválidas"}), 401