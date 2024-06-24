from flask import Flask, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/cls', methods=['GET'])
def get_cls():
    return jsonify({'cls': 'hello'})

@app.route('/test/<command>', methods=['GET'])
def execute_command(command):
    result = subprocess.check_output(command, shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT)
    rs = result.decode('utf-8')
    return jsonify({'command': rs})


if __name__ == '__main__':
    app.run()