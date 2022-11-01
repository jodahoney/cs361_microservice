from dataclasses import dataclass
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/square-results/<int:num>')
def square_results(num):
    val_sqd = num**2
    response = {
        "squared_value": val_sqd,
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)