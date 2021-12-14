from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/result', methods=['GET', 'POST'])

def result():
    if request.method == 'POST':
        area = request.form.get('land', '0')
        animals = request.form.get('animals', '0')
        rotation = request.form.get('crop_rotation', '0')
        tractors = request.form.get('tractors', '0')
        fertilizer =  request.form.get('fertilizers', '0')
        age = request.form.get('age', '0')
    # default_value = '0'
    # data = request.form.get('land', default_value)
    return render_template('result.html', area=area,animals=animals,rotation=rotation,tractors=tractors,fertilizer=fertilizer,age=age)

if __name__ == "__main__":
    app.run(debug=True)