# Nutrient Score Prediction Web App

## Overview

This web application predicts the nutrient score of food items using data sourced from OpenFood Facts. The project includes data exploration, preprocessing, feature engineering, model selection, and deployment using Flask. The primary goal is to provide a tool that can estimate the nutritional quality of food products based on their features.

## Dataset

The dataset is derived from the [OpenFood Facts](https://world.openfoodfacts.org/) database, which contains information about thousands of food products from around the world. This dataset was used to train the model to predict the nutrient score, a measure of the nutritional quality of food.

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the structure, distribution, and relationships within the data. Key insights from EDA guided the feature selection and engineering process.

## Data Preprocessing

Data cleaning involved handling missing values, outliers, and irrelevant features. This step ensured that the dataset was ready for modeling, improving the accuracy and reliability of the predictions.

## Feature Engineering

Feature encoding was applied to transform categorical variables into numerical representations suitable for machine learning algorithms. This step was crucial for maximizing the performance of the models.

## Modeling

Several machine learning classifiers were evaluated for predicting the nutrient score:

1. **KNeighborsClassifier (KNN)**:

   - Configuration: `KNeighborsClassifier(n_jobs=-1)`
2. **GaussianNB (Naive Bayes)**:

   - Configuration: `GaussianNB()`
3. **DecisionTreeClassifier**:

   - **Gini Criterion**: `DecisionTreeClassifier(criterion="gini")`
   - **Entropy Criterion**: `DecisionTreeClassifier(criterion="entropy")`
4. **RandomForestClassifier**:

   - **Gini Criterion**: `RandomForestClassifier(criterion="gini", n_jobs=-1)`
   - **Entropy Criterion**: `RandomForestClassifier(criterion="entropy", n_jobs=-1)`

Out of these models, **Random Forest** with the **gini criterion** provided the highest accuracy and was selected for the final prediction model.

## K-Fold Cross-Validation

The dataset was split into 5 folds to perform cross-validation. This method helped in assessing the performance of the models and selecting the one with the highest accuracy.

## Flask Application

A Flask web application was developed to provide an interactive interface for users to input food product details and receive a predicted nutrient score. The application was designed with user-friendliness in mind and can be easily accessed through a web browser.

## Screenshots
![Screenshot 2024-08-12 035351](https://github.com/user-attachments/assets/10bec10e-7485-4464-bfba-143d7d79fb68)
 ![Screenshot 2024-08-12 035408](https://github.com/user-attachments/assets/a2c63de2-8584-4232-bfe3-d694d8cecfbb)


