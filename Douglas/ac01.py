import os
from unicodedata import name
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calculadora.html')


@app.route('/calculadoraformulario', methods=['POST', 'GET'])
def calcula():
    v1 = request.form['v1']
    v2 = request.form['v2']
    operacao = request.form['operacao']

    v1 = int(v1)

    v2 = int(v2)

    if operacao == "soma":
        resultado = v1 + v2
    elif operacao == "subtracao":
        resultado = v1 - v2
    elif operacao == "divisao":
        resultado = v1 / v2
    elif operacao == "multiplicacao":
        resultado = v1 * v2

    return str(resultado)

app.run(debug=True)
