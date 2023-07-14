# Calories-Burnt-Prediction
WEBSITE: https://calories-burnt-prediction-mr-devansh.streamlit.app/

This project is about predicting Calories burnt during a workout using Machine Learning with Python. For this prediction, I have used XGBoost Regressor model.
The dataset contains several fields like 
* User_ID      
* Gender        
* Age           
* Height        
* Weight        
* Duration      
* Heart_Rate    
* Body_Temp     
* Calories

We have used seaborn for several data analysis and visalization using heatmaps, countplots, distribution plots etc
Predictions using XGBRegressor which is a really powerful regression ML model
next we evaluated the model using the mean absolute error, r2 score
and finally saved the model for the future use using the pickle module of python

The features to be added are deployment on a web server along with a UI for evaluating real-life values entered by users! 
