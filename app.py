from flask import Flask, render_template, request
from calculate import calc

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
        fertilizer =  request.form.get('fertilizers', 'a')
        trac_func = request.form.get('tractors_function', 'a')
        age = request.form.get('age', '0')
    
    emissions = calc(int(area), int(animals), int(tractors), trac_func, fertilizer, age, rotation)
    # default_value = '0'
    # data = request.form.get('land', default_value)
    if emissions>=5393.51:
        st = f'{round((emissions/5393)*100 - 1,2)}% more than average'
    else:
        st = f'{round((5393-emissions)/5393 *100, 2)}% less than average'
    return render_template('result.html', emissions=round(emissions, 2), statement= st)

if __name__ == "__main__":
    app.run(debug=True)