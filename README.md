# TaxiFare-ML-Project-by-health
Taxi Fare Prediction using ML and Streamlit. Predict total taxi fare based on trip details like pickup/dropoff location, time, and passenger count. Includes data preprocessing, feature engineering, model training, and a Streamlit app for real-time fare prediction.
# TripFare : Predicting Urban Taxi Fare with Machine Learning

## Project Overview
This project aims to build a machine learning model to accurately predict the total fare of taxi trips using historical trip data from a metropolitan transportation network. The goal is to enhance fare estimation, promote pricing transparency, and provide valuable insights for ride-hailing services, drivers, urban planners, and travelers.

## Skills and Techniques Applied
- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Feature Engineering (e.g., trip distance, time-based features)
- Regression Model Building (Linear Regression, Ridge, Lasso, RandomForest, GradientBoosting)
- Model Evaluation and Comparison using metrics like R², MSE, RMSE, MAE
- Hyperparameter Tuning with GridSearchCV
- Deployment using Streamlit for interactive user interface

## Problem Statement
As a Data Analyst at an urban mobility analytics firm, the task is to analyze real-world taxi trip data and build a predictive model for total taxi fare based on trip features like pickup/dropoff locations, passenger count, trip time, and additional charges.

## Real-World Use Cases
- Fare estimates for ride-hailing services before booking
- Driver incentive optimization by location and time
- Urban mobility fare trend analysis
- Travel budget planning for tourists
- Dynamic pricing in taxi-sharing apps

## Data Description
The dataset includes features such as:
- VendorID, pickup and dropoff datetime
- Passenger count
- Pickup/dropoff longitude & latitude
- RatecodeID, store_and_fwd_flag
- Payment type and fare-related charges (fare amount, extra, MTA tax, tip, tolls, surcharges)
- Target variable: `total_amount` (total trip fare)

## Feature Engineering Highlights
- Calculated trip distance using the Haversine formula
- Extracted temporal features: pickup hour, day of week, weekend flag, am/pm, night trip flag
- Converted pickup datetime from UTC to local timezone
- Engineered trip duration from pickup and dropoff times

## Model Selection: Why Linear Regression?
Linear Regression was selected as the primary model because:
- It provides a simple, interpretable baseline to understand relationships between features and fare
- Performs well with continuous target variables like fare amount
- Allows easy evaluation and improvement through regularization techniques (Ridge, Lasso)
- Faster to train and easier to deploy in a Streamlit app for quick predictions

Multiple models were trained and compared; Linear Regression offered a good balance of performance and simplicity, making it suitable for production deployment.

## Workflow Summary
1. Data Collection & Loading
2. Data Understanding (shape, types, missing values)
3. Feature Engineering (trip distance, time flags)
4. Exploratory Data Analysis (visualizing fare vs distance, time, passenger count)
5. Data Transformation (outlier treatment, encoding)
6. Feature Selection (correlation, importance)
7. Model Building & Evaluation (5+ regression models)
8. Hyperparameter Tuning
9. Final Model Selection & Saving
10. Streamlit UI Development for fare prediction

## How to Use the Project
1. Clone this repository  
2. Open Anaconda Prompt  
3. Navigate to the project folder  
4. Run the Streamlit app by typing:  

