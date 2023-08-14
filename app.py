from flask import Flask , render_template , request
import os

import numpy as np
import pandas as pd


from CreditCardFraud.pipeline.prediction import PredictionPipeline



app = Flask(__name__)


@app.route(rule='/',methods = ['GET'])

def homePage():

    return render_template('index.html')

@app.route('/train',methods=['GET']) # route to train the pipeline
def training():
    os.system('python main.py')
    return "Training Successful!"

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            LIMIT_BAL =int(request.form['LIMIT_BAL'])
            SEX =int(request.form['SEX'])
            EDUCATION =int(request.form['EDUCATION'])
            MARRIAGE =int(request.form['MARRIAGE'])
            AGE =int(request.form['AGE'])
            PAY_0 =int(request.form['PAY_0'])
            PAY_2 =int(request.form['PAY_2'])
            PAY_3 =int(request.form['PAY_3'])
            PAY_4 =int(request.form['PAY_4'])
            PAY_5 =int(request.form['PAY_5'])
            PAY_6 =int(request.form['PAY_6'])
            BILL_AMT1 =int(request.form['BILL_AMT1'])
            BILL_AMT2 =int(request.form['BILL_AMT2'])
            BILL_AMT3 =int(request.form['BILL_AMT3'])
            BILL_AMT4 =int(request.form['BILL_AMT4'])
            BILL_AMT5 =int(request.form['BILL_AMT5'])
            BILL_AMT6 =int(request.form['BILL_AMT6'])
            PAY_AMT1 =int(request.form['PAY_AMT1'])
            PAY_AMT2 =int(request.form['PAY_AMT2'])
            PAY_AMT3 =int(request.form['PAY_AMT3'])
            PAY_AMT4 =int(request.form['PAY_AMT4'])
            PAY_AMT5 =int(request.form['PAY_AMT5'])
            PAY_AMT6 =int(request.form['PAY_AMT6'])
       
         
            data = [LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]
            columns = ['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']
            data = np.array(data).reshape(1, 23)
            data = pd.DataFrame(data,columns=columns)
            print(data)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = int(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=True)