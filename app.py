import numpy as np
import pickle
import pandas as pd
import streamlit as st

loaded_XGB_model = pickle.load(open('XGB_model.pkl', 'rb'))

def predict(input_data):
    data_as_array = np.asarray(input_data, dtype=np.float32)
    data_frame = pd.DataFrame(columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'],
                              data=[data_as_array])
    pickle_y_preds = loaded_XGB_model.predict(data_frame)
    return pickle_y_preds[0]

def main():
    st.title('Calories Burnt Prediction')
    Gender = st.text_input('Your gender')
    Age = st.text_input('Your age')
    Height = st.text_input('Your height')
    Weight = st.text_input('Your weight')
    Duration = st.text_input('Your duration')
    Heart_Rate = st.text_input('Your heart rate')
    Body_Temp = st.text_input('Your body temperature')

    result = ''

    if st.button('Calories'):
        input_data = [Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]
        try:
            result = predict([float(value) for value in input_data])
            st.success(f"Predicted calories burnt: {result}")
        except ValueError:
            st.error("Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    main()
