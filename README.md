# Old Car Price Prediction
A machine learning web application that predicts the price of used cars based on various features such as car name, age, kilometers driven, fuel type, and more.

Try it out : https://car-price-prediction-q0fz.onrender.com/
<br>
<hr>

## Table of Contents
- Introduction
- Features
- Dataset Description
- Technologies Used
- Installation
- Usage
- Results
- Future Work
- Demo

<hr>

## Introduction
The Old Car Price Prediction project utilizes a regression model trained on used car data to predict their market price. This tool is designed for both car dealers and buyers, helping them make informed decisions.

<hr>

## Features
- 🚗 Predicts the price of a used car based on input features.
- 📊 Provides insights into car pricing trends.
- 🌐 Interactive and user-friendly interface built with Flask.

<hr>

## Dataset Description
- The dataset used in this project was obtained from "Kaggle".
- Link : (https://www.kaggle.com/datasets/manishkr1754/cardekho-used-car-data) 

The dataset used includes the following columns:

- **Car Name**: Name and brand of the car.
- **Vehicle Age**: Age of the car in years.
- **Kilometers Driven**: Total distance the car has been driven, measured in kilometers.
- **Seller Type**: The category of the seller (e.g., Individual, Dealer).
- **Fuel Type**: Type of fuel used by the car (e.g., Petrol, Diesel, CNG, Electric).
- **Transmission Type**: Gear system of the car (e.g., Manual, Automatic).
- **Mileage**: Fuel efficiency of the car, typically measured in km/l or km/kg.
- **Engine**: Engine capacity or displacement, measured in cubic centimeters (cc).
- **Max Power**: The maximum power output of the car's engine, measured in brake horsepower (bhp).
- **Seats**: Number of seats available in the car.
- **Selling Price**: The final price at which the car was sold (target variable).

<hr>

## Technologies Used

- **Programming Language** : Python  
- **Framework** : Flask  
- **Libraries** : Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  


<hr>

## Installation
Follow these steps to set up the project locally:

1. Clone the repository:<br>
**command:** <i>git clone https://github.com/yashsahu02/Car_Price_Prediction.git</i>

2. Install the dependencies:<br>
**command:** <i>pip install -r requirements.txt</i>

3. Run the Flask application:<br>
**command:** <i>python app.py</i>

<hr>

## Usage
- Launch the application:
command: <code>python app.py</code>

- Open the web application in your browser.

- Enter the car details like: (Car name,Age,Kilometers driven,Fuel type, etc.)

- Get the predicted price displayed on the interface.

<hr>

## Results
The RandomForestRegressor achieved the highest performance as compared to other algorithms in predicting car prices:

- Achieved R² Score: 0.9042

<hr>

## Future Work
- Integrate advanced machine learning models like XGBoost or CatBoost to improve prediction accuracy.

<hr>

## Demo
- Watch the full project demo:






## Main Page
![Screenshot (1)](https://github.com/user-attachments/assets/0a6495a5-31d7-4b3f-97ae-34e9657e911b)

<br>

![Screenshot (2)](https://github.com/user-attachments/assets/043e1ddc-1ba5-42fb-9d2c-09e09ce74039)

<br>

![Screenshot (3)](https://github.com/user-attachments/assets/c326403b-1a04-4c41-ab97-f4df359e36ed)

<br>

## About Dataset Page
![Screenshot (4)](https://github.com/user-attachments/assets/ecc48685-961b-49d8-991d-2678ddf7db08)

<br>

## About Model Page
![Screenshot (6)](https://github.com/user-attachments/assets/899056c9-7258-40f8-b2dc-593619b99449)

<br>

## Github Link Page
![Screenshot (7)](https://github.com/user-attachments/assets/2c853b28-1cc7-4d74-b91b-3c624337310f)
