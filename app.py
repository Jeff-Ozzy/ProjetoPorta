from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/textos_db'
mongo = PyMongo(app)


@app.route('/textos', methods=['POST'])
def adicionar_texto():
    texto = request.json['texto']
    pos_x = request.json['posX']
    pos_y = request.json['posY']
    font_size = request.json['fontSize']
    color = request.json['color']

    texto_id = mongo.db.textos.insert_one({
        'texto': texto,
        'posX': pos_x,
        'posY': pos_y,
        'fontSize': font_size,
        'color': color
    })

    novo_texto = mongo.db.textos.find_one({'_id': texto_id})

    return jsonify({'mensagem': 'Texto adicionado com sucesso', 'texto': novo_texto}), 201


@app.route('/textos', methods=['GET'])
def obter_textos():
    textos = list(mongo.db.textos.find())
    return jsonify(textos), 200


if __name__ == '__main__':
    app.run(debug=True)
