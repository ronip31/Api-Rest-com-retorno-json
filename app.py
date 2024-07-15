from flask import Flask, Response
import json
import os

app = Flask(__name__)

def load_data():
    with open('pubsub.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

@app.route('/data', methods=['GET'])
def get_data():
    data = load_data()
    response = Response(
        response=json.dumps(data, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
