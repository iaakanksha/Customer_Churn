
from flask import *
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))



@app.route('/',methods = ["GET"])
def login():
    return render_template('index1.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == "user" and password == "admin":
            return render_template('index.html')
        else:
            error = "username or password is wrong !!"
            return render_template('index1.html', error=error)
    
    return render_template('index1.html')

@app.route('/predict',methods=['GET','POST'])
def predict(): 
    if request.method == "POST":
        CreditScore = int(request.form['CreditScore'])
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        HasCrCard = int(request.form['HasCrCard'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])
        Geography_Germany = request.form['Geography_Germany']
        if(Geography_Germany == 'Germany'):
            Geography_Germany = 1
            Geography_Spain= 0
            Geography_France = 0
                
        elif(Geography_Germany == 'Spain'):
            Geography_Germany = 0
            Geography_Spain= 1
            Geography_France = 0
        
        else:
            Geography_Germany = 0
            Geography_Spain= 0
            Geography_France = 1
        Gender_Male = request.form['Gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
        prediction = model.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Germany,Geography_Spain,Gender_Male]])
        x = prediction
        if(x==0):
            x="No customer will not churn :)"
            return render_template("prediction.html", prediction_text="Prediction status is {}".format(x))
        else:
            x="Yes customer will churn :("
            return render_template("prediction.html", prediction_text="Prediction status is {}".format(x))
    else:
        return render_template("prediction.html")

@app.route('/analyze')
def analyze():
    return render_template('Analysis.html')
@app.route('/demo')
def demo():
    return render_template('Demo.html')

if __name__== "__main__":
    app.run(debug=True)
                


