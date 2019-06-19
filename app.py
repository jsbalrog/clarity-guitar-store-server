from flask import Flask, jsonify, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/guitars')
def get_guitars():
    response = [{'id': 1, 'make': 'Fender', 'model': 'Stratocaster', 'type': 'electric', 'year': '1995', 'price': 2000}, {'id': 2, 'make': 'Gibson', 'model': 'Hummingbird', 'type': 'acoustic', 'year': '2009', 'price': 2999},{'id': 3, 'make': 'PRS', 'model': 'Custom 24', 'type': 'electric', 'year': '2016', 'price': 3599}]
    return jsonify(response)

@app.route('/guitars/<id>')
def get_guitar(id):
    if id == '1':
        response = {'id': 1, 'make': 'Fender', 'model': 'Stratocaster', 'type': 'electric', 'year': '1995', 'price': 2000}
    elif id == '2':
        response = {'id': 2, 'make': 'Gibson', 'model': 'Hummingbird', 'type': 'acoustic', 'year': '2009', 'price': 2999}
    else:
        response = {'id': 3, 'make': 'PRS', 'model': 'Custom 24', 'type': 'electric', 'year': '2016', 'price': 3599}
    return jsonify(response);

@app.route('/files')
def get_files():
    response = [{'id': 1, 'name': 'Electric', 'isFolder': True}, {'id': 2, 'name': 'Acoustic', 'isFolder': True}]
    return jsonify(response)

@app.route('/files/<id>')
def get_file(id):
    if id == '1':
        response = [{'id': 1, 'name': 'Fender Stratocaster', 'isFolder': False}, {'id': 3, 'name': 'PRS Custom 24', 'isFolder': False}]
    else:
        response = [{'id': 2, 'name': 'Gibson Hummingbird', 'isFolder': False}]
    return jsonify(response);

if __name__ == '__main__':
    app.run(debug=True)