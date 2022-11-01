from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_survey():
    return render_template('survey.html')

@app.route('/get-results', methods=['GET', 'POST'])
def get_results():
    if request.method == 'POST':
        f_name = request.form.get("fname")
        l_name = request.form.get('lname')
        rating = request.form.get('rating')
        explanation = request.form.get('explanation')

        response = {
            "first_name": f_name,
            "last_name": l_name,
            "rating": rating,
            "explanation": explanation
        }

        return jsonify(response)
    else:
        return redirect(url_for('show_survey'))

if __name__ == '__main__':
    app.run(debug=True)