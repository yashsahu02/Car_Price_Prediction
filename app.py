from flask import Flask,render_template,request,url_for

## importing all required libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

le=pickle.load(open('models/labelEncoder.pkl','rb'))
preprocessor=pickle.load(open('models/processor.pkl','rb'))
RF_model=pickle.load(open('models/model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("home.html", price='')

@app.route('/predictprice',methods=['GET','POST'])
def predictprice():
    if request.method=="POST":
        col_names=['car_name', 'vehicle_age', 'km_driven', 'seller_type', 'fuel_type','transmission_type', 'mileage', 'engine', 'max_power', 'seats']
        
        car_name=request.form.get('car')
        car_age=int(request.form.get('car_age'))
        km_driven=int(request.form.get('km_driven'))
        seller_type=request.form.get('sellingtype')
        fuel_type=request.form.get('fuel')
        transmission_type=request.form.get('transmission')
        mileage=float(request.form.get('mileage'))
        engine=int(request.form.get('engine'))
        max_power=float(request.form.get('max_power'))
        seats=int(request.form.get('seats'))

        inp=pd.DataFrame([[car_name,car_age,km_driven,seller_type,fuel_type,transmission_type,mileage,engine,max_power,seats]],columns=col_names)
        inp['car_name']=le.transform(inp['car_name'])
        inp=preprocessor.transform(inp)
        predicted_price=RF_model.predict(inp)
    
        return render_template('home.html',price=int(predicted_price[0]))
    else:
        return "<p>Sorry can't proceed....</p>"


if __name__=="__main__":
    app.run(debug=True)