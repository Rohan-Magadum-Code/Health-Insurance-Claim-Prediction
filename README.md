# 🏥 Health Insurance Claim Prediction

## 📌 Project Overview

This project focuses on predicting **health insurance claim amounts** using Machine Learning techniques. The goal is to analyze customer data such as age, BMI, smoking habits, and medical history to estimate the expected insurance claim.

This helps insurance companies:

* Assess risk more accurately
* Price policies effectively
* Detect high-cost customers

---

## 🔍 Exploratory Data Analysis (EDA)

Performed detailed EDA to understand the data:

* Checked missing values and duplicates
* Analyzed distributions of numerical features
* Identified outliers using boxplots
* Created **age groups using `pd.cut()`**
* Studied relationships:

  * Age vs Claim
  * BMI vs Claim
  * Smoker vs Claim (very strong impact)
* Correlation heatmap to find important features

---

## ⚙️ Data Preprocessing

* Handled missing values
* Encoded categorical variables
* Feature engineering (age groups)
* Scaled numerical features (if required)

---

## 🤖 Model Building

Tested multiple machine learning models:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

---

## 📊 Model Evaluation Metrics

Used the following metrics:

* **MAE (Mean Absolute Error)**
* **MSE (Mean Squared Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

---

## 🚀 Streamlit Web App

A user-friendly **Streamlit application** was built to predict insurance claim values in real-time.

### Features:

* Input user details (age, BMI, smoker, etc.)
* Instant prediction of claim amount
* Simple and interactive UI

---

## 🖼️ Streamlit App Screenshot

<img width="983" height="623" alt="Screenshot 2026-04-19 084906" src="https://github.com/user-attachments/assets/be58a2d9-346c-4e8d-9ccb-5520adb0f38c" />


---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Matplotlib, Seaborn**
* **Scikit-learn**
* **XGBoost**
* **Streamlit**

---

## 📈 Key Insights

* Smoking has a **major impact** on insurance claims
* Higher BMI leads to higher claims
* Age is positively correlated with claim amount
* Certain regions show slightly higher claim patterns

---

## 📌 Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Deploy model on cloud (AWS / Render)
* Add more real-world features
* Improve UI/UX of Streamlit app

---

## 👨‍💻 Author

**Rohan Magadum**
## ⭐ If you like this project
Give it a star ⭐ on GitHub!
