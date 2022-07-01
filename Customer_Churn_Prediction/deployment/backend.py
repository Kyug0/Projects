from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np
from tensorflow import keras

app = Flask(__name__)

with open("pipe.pkl", "rb") as f:
    pipe = pickle.load(f)

model = keras.models.load_model("my_model_fun.h5")

columns = ['tenure', 'MonthlyCharges', 'TotalCharges', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
            'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
            'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']

label = ['No, Stays', 'Yes, Leaves']

@app.route("/")
def welcome():
    return "<h3>Welcome to the Backend</h3>"

@app.route("/predict", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        content = request.json
        try:
            # new_data = {'tenure':content['tenure'], 'MonthlyCharges':content['MonthlyCharges'], 'TotalCharges':content['TotalCharges'], 'gender':content['gender'],
            #     'SeniorCitizen':content['SeniorCitizen'], 'Partner':content['Partner'], 'Dependents':content['Dependents'], 'MultipleLines':content['MultipleLines'], 
            #     'InternetService':content['InternetService'], 'OnlineSecurity':content['OnlineSecurity'], 'OnlineBackup':content['OnlineBackup'], 'DeviceProtection':content['DeviceProtection'],
            #     'TechSupport':content['TechSupport'], 'StreamingTV':content['StreamingTV'], 'StreamingMovies':content['StreamingMovies'], 'Contract':content['Contract'], 
            #     'PaperlessBilling':content['PaperlessBilling'], 'PaymentMethod':content['PaymentMethod']}
            new_data = [content['tenure'], content['MonthlyCharges'], content['TotalCharges'], content['gender'],
                    content['SeniorCitizen'], content['Partner'], content['Dependents'], content['MultipleLines'], 
                    content['InternetService'], content['OnlineSecurity'], content['OnlineBackup'], content['DeviceProtection'],
                    content['TechSupport'], content['StreamingTV'], content['StreamingMovies'], content['Contract'], 
                    content['PaperlessBilling'], content['PaymentMethod'],]
            new_data = pd.DataFrame([new_data], columns=columns)
            data_scaled = pipe.transform(new_data)
            res = model.predict(data_scaled)
            res = np.where(res > 0.5, 1, 0)

            # result = {'class':str(res[0]),
            #           'class_name':label[res.shape[0]]}
            # response = jsonify(success=True,
            #                    result=result)

            response = {"code": 200, "status": "EY OK",
                        "result":{"class":str(res[0].item()), "class_name":label[res[0].item()]}}
            
            # return response, 200
            return jsonify(response)
        except Exception as e:
            response = jsonify(success=False,
                               message=str(e))
            return response, 400
    return "<p>Use the POST method for Model Inference</p>"

app.run(debug=True) #Since I cannot deploy the file to heroku I will leave this as is