from flask import Flask, request, jsonify
import argparse

app = Flask(__name__)

def add(i=int, j=int):
    return i + j


# View
@app.route('/', methods=['GET'])
def index():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    r = add(a, b)
    print(r)
    return jsonify({'add': r})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)