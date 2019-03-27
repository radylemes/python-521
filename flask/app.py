#!/usr/bin/python3
from datetime import datetime
from flask import Flask, jsonify, make_response, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'mensagem' : 'Rodando'})

@app.route('/data')
def data():
    return jsonify({'hoje' : datetime.now()})
@app.route('/naotemnadaaqui')
def notemnadaaqui():
    return redirect('/')
@app.route('/cadastrar', methods=['POST'])
def bunda():
    dados = request.get_json()
    #se dados for nulo, retornar 400
    #{"mensagem" : "Corpo não pode ser vazio"}

    if dados is None:
        return make_response(jsonify({'mensagem' : "Corpo nao pode ser vazio"}), 400)
        dados['lapetina'] = 'fumacinha'
    return jsonify(dados)
@app.route('/site')
def site():
    dados = [{'id' : 2, 'nome' : 'Paramahansa Yogananda'}]
    dados.append({'id' : '3', 'nome' : 'Gabriel o pensador'})
    dados.append({'id' : '4', 'nome' : 'João Batista' })
    return render_template('index.html', nome = 'Hector', usuarios = dados)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
