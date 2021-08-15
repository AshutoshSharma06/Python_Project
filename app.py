from flask import Flask, render_template, request
import joblib
# Instance of an app

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('landing.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return 'this is first feedback page'

@app.route('/data')
def data():
    return 'Form Submitted'

@app.route('/result', methods = ['POST'])
def result():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age  = request.form.get('age')
    model = joblib.load('diabetic_79.pkl')
    result = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if result[0] == 1:
        return 'Person is Diabetic'
    else:
        return'Not Diabetic'
    # print(type(preg), preg, type(pres), pres)
    # print(type(age), age)
    # return 'test'
    

if __name__ == '__main__':
    app.run(debug=True)