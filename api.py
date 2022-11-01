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


@dataclass
class Macronutrient:
    name:str
    cals_per_gram: int

    def calc_calories(self) -> int:
        if self.name in ["carbohydrate", "protein"]:
            return self.cals_per_gram * 4
        else:
            return self.cals_per_gram * 9

@app.route('/calculate-cals/<string:name>/<int:grams>')
def calculate_cals(name, grams):
    if name and grams:
        macro = Macronutrient(name, grams)
        response = {
            "macro-name": name,
            "grams": grams,
            "calories": macro.calc_calories()
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)