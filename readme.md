# 🛒 Walmart ML Project – Regression Model for Prediction

## 📌 Overview

This project builds a machine learning model to predict numeric outcomes (e.g., sales or transaction values) using structured data. The goal is to evaluate multiple models, compare their performance, and select the most accurate one.

---

## 🎯 Objectives

* Train regression models on historical data
* Evaluate model performance using appropriate metrics
* Compare multiple algorithms
* Improve prediction accuracy using ensemble techniques

---

## 🧠 Models Used

* Random Forest Regressor
* XGBoost Regressor

Both models were trained and evaluated on the same dataset split to ensure a fair comparison.

---

## ⚙️ Methodology

### 1. Data Preparation

* Cleaned dataset
* Split data into training and testing sets (80/20 split)
* Ensured consistent preprocessing across models

### 2. Model Training

* Trained both Random Forest and XGBoost on the same training data
* Tuned hyperparameters such as:

  * `max_depth`
  * `n_estimators`
  * `learning_rate`

### 3. Evaluation Metrics

* Mean Absolute Error (MAE)
* R-squared (R² score)

---

## 📊 Results

| Model             | MAE    | R² Score |
| ----------------- | ------ | -------- |
| Random Forest     | ~3584  | ~0.9999  |
| XGBoost           | ~3169  | ~0.9996  |
|

---

## 🔍 Key Insights

* XGBoost produced the lowest error and best overall performance
* Random Forest performed well but slightly worse than XGBoost
* High R² scores indicate strong predictive power, but MAE was used to determine the best model

---

## ✅ Final Model Selection

The XGBoost model was selected as the final model because it achieved the lowest Mean Absolute Error and provided the most accurate predictions.

---

## 🧪 Lessons Learned

* Always use the same train/test split when comparing models
* High training accuracy can indicate overfitting
* Ensemble methods like stacking do not always improve results
* Evaluation metrics must be interpreted relative to the scale of the data

---

## 🛠️ Tools & Technologies

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib / Seaborn 

---

## 🚀 Future Improvements

* Perform hyperparameter tuning using GridSearchCV
* Try advanced stacking with a meta-model
* Explore feature engineering to improve performance further

---

## 👤 Author

 Adeniji Elijah

---

## 📌 Conclusion

This project demonstrates the importance of model comparison and proper evaluation. While multiple models performed well, XGBoost provided the best balance of accuracy and reliability for this task.