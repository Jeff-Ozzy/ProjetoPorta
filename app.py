from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4521'
app.config['MYSQL_DB'] = 'projeto_porta'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Inicialização do MySQL
mysql = MySQL(app)

# Rota para adicionar um novo texto ao banco de dados
@app.route('/textos', methods=['POST'])
def adicionar_texto():
    texto = request.json['texto']
    pos_x = request.json['posX']
    pos_y = request.json['posY']
    font_size = request.json['fontSize']
    color = request.json['color']

    # Conexão com o banco de dados
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO textos (texto, posX, posY, fontSize, color) VALUES (%s, %s, %s, %s, %s)", (texto, pos_x, pos_y, font_size, color))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensagem': 'Texto adicionado com sucesso'}), 201

# Rota para obter todos os textos do banco de dados
@app.route('/', methods=['GET'])

def render_html():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM textos")
    textos = cur.fetchall()
    cur.close()
    return render_template('index.html', nomes=textos)

if __name__ == '__main__':
    app.run(debug=True)
