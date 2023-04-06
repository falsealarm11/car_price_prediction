from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd


model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods =['GET','POST'])
def predict():
    year = int(request.form['Year'])
    km_driven = int(request.form['KM driven'])
    fuel = request.form['Fuel']
    if fuel == 'Diesel':
        fuel = 0
    if fuel == 'Petrol':
        fuel = 1
    if fuel == 'LPG':
        fuel = 2
    if fuel == 'CNG':
        fuel = 3
    seller = request.form['Seller Type']
    if seller == 'Individual':
        seller = 0
    if seller == 'Dealer':
        seller = 1
    if seller == 'Trustmark Dealer':
        seller = 2
    transmission = request.form['Transmission']
    if transmission == 'Manual':
        transmission = 0
    if transmission == 'Automatic':
        transmission = 1
    owner = request.form['Owner']
    if owner == 'First Owner':
        owner = 0
    if owner == 'Second Owner':
        owner = 1
    if owner == 'Third Owner':
        owner = 2
    if owner == 'Fourth & Above Owner':
        owner = 3
    if owner == 'Test Drive Car':
        owner = 4
    mileage = float(request.form['Mileage'])
    engine = float(request.form['Engine'])
    max_power = float(request.form['Max Power'])
    seats = float(request.form['Seats'])

    #total = [[year,km_driven,fuel,seller,transmission,owner,mileage,engine,max_power,seats]]
    #total = [int(year),int(km_driven),fuel,seller,transmission,owner,float(mileage),float(engine),float(max_power),float(seats)]
    #total = [np.array(total)]
    prediction = model.predict(pd.DataFrame([[year,km_driven,fuel,seller,transmission,owner,mileage,engine,max_power,seats]], columns= ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner',
       'mileage', 'engine', 'max_power', 'seats']))
    prediction = np.round(prediction,2)
    return render_template('index.html',prediction_text = "The predicted selling price is {}".format(prediction))



if __name__ == "__main__":
    app.run(debug=True)