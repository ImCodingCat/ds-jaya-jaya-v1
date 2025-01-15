import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn.preprocessing as preprocessing

data = pd.read_csv('./data/employee_data.csv').drop(['Attrition', 'EmployeeId'], axis=1)

non_number_col = data.select_dtypes(exclude=[np.number]).columns.tolist()
encoders = {col: preprocessing.LabelEncoder() for col in non_number_col}

category_value = {col: data[col].unique().tolist() for col in non_number_col}

number_col = data.select_dtypes(include=[np.number]).columns.tolist()
number_value = {col: [int(data[col].min()), int(data[col].max())] for col in number_col}

input_orders = ['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
                 'EducationField', 'EmployeeCount', 'EnvironmentSatisfaction', 'Gender', 
                 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 
                 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18', 
                 'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 
                 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 
                 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 
                 'YearsWithCurrManager']

for col in non_number_col:
    encoders[col].fit(data[col])

st.title("Prediction by Muhammad Dava Pasha (mdavap) @ Dicoding")

model_file = open('model.bin', 'rb')
model = pickle.load(model_file)                    
model_file.close()

input_prediction = {}

for category in category_value:
    input_prediction[category] = st.selectbox(category, category_value[category])

for number in number_value:
    min_max = number_value[number]
    min = min_max[0]
    max = min_max[1]

    max = 100 if max == min else max

    input_prediction[number] = st.slider(number, min, max)

if st.button('Predict'):
    input = pd.DataFrame()

    for order in input_orders:
        input[order] = [input_prediction[order]]

    # Encoding
    for col in non_number_col:
         input[col] = encoders[col].transform(input[col])
         
    print(input.value_counts())
    result = model.predict(input)[0]

    st.write(f'Attrition prediction: {result}')