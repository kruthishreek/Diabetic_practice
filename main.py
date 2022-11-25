# install flask

from flask import Flask, render_template,request
import joblib
model = joblib.load('predict_79.pkl')


# initilizing the app
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/diabeticforms')
def diabeticforms():
    return render_template('diabeticforms.html')


# @app.route('/predict',methods = ['post'])
# def predict():
#     number = request.form.get('phone')
#     emailId = request.form.get('email')
#     name = request.form.get('name')
#     print(number)
#     print(emailId)
#     print(name)
#     res = model.predict([[1,1,1,1,1,1,1,1]])
#     if res[0]==0:
#         return "not diabetic"
#     else:
#         return "diabetic"
    

@app.route('/predict',methods = ['post'])
def predict():
    mpreg = int(request.form.get('preg'))
    mplas = int(request.form.get('plas'))
    mpres = int(request.form.get('pres'))
    mskin = int(request.form.get('skin'))
    mtest = int(request.form.get('test'))
    mmass = int(request.form.get('mass'))
    mpedi = int(request.form.get('pedi'))
    mage = int(request.form.get('age'))
   
    print(mpreg, mplas, mpres, mskin, mtest,mmass,mpedi,mage)
    res = model.predict([[mpreg, mplas, mpres, mskin, mtest,mmass,mpedi,mage]])
   
    # if res[0]==0:
    #     return "not diabetic"
    # else:
    #     return "diabetic"
    
    
    if res[0]==0:
        ans= "not diabetic"
    else:
        ans= "diabetic"
    
    return render_template("diabeticforms.html",data=ans)
    

# running the app, it should bealways written in end
app.run(debug=True)

