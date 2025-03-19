```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import mysql.connector
import json

app = Flask(__name__)

db_config = {
    'host': 'seu_usuario.mysql.pythonanywhere-services.com',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'seu_usuario$suinocultura'
}

class Suino:
    def __init__(self, id, raca, data_nascimento, peso, sexo):
        self.id = id
        self.raca = raca
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.sexo = sexo
        self.status = "Ativo"
        self.historico_vacinas = []
        self.historico_peso = []

class Reproducao:
    def __init__(self):
        self.status = "Disponível"
        self.data_ultima_inseminacao = None
        self.numero_partos = 0
        self.historico_partos = []
        self.gestacoes_atuais = []
        self.periodo_gestacao = 114

class CalendarioSuino:
    def __init__(self):
        self.eventos = {}
        self.ciclos = {
            "Gestação": 114,
            "Lactação": 21,
            "Desmame-Cio": 7,
            "Ciclo Total": 142
        }
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suinos')
def suinos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suinos")
    suinos = cursor.fetchall()
    conn.close()
    return render_template('suinos.html', suinos=suinos)

@app.route('/reproducao')
def reproducao():
    return render_template('reproducao.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/api/adicionar_suino', methods=['POST'])
def adicionar_suino():
    dados = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    sql = """INSERT INTO suinos (raca, data_nascimento, peso, sexo, status) 
             VALUES (%s, %s, %s, %s, %s)"""
    valores = (dados['raca'], dados['data_nascimento'], 
              dados['peso'], dados['sexo'], 'Ativo')
    
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
