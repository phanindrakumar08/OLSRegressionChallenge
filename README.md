# 🏥 Cancer Mortality Rate Prediction (US Counties)  

## 📌 Project Overview  
This project aims to **predict cancer mortality rates (TARGET_deathRate) for US counties** using **Multiple Linear Regression (MLR)**. The dataset aggregates information from multiple sources, including:  
- **American Community Survey (census.gov)**  
- **clinicaltrials.gov**  
- **cancer.gov**  

The goal is to build an **Ordinary Least Squares (OLS) regression model** that provides insights into the key factors influencing cancer mortality rates across different regions.  

---

## 🛠 Methodology  

### 1️⃣ Exploratory Data Analysis (EDA) 📊  
- Examined data distributions and summary statistics.  
- Identified missing values and potential outliers.  
- Analyzed feature correlations with **TARGET_deathRate**.  

### 2️⃣ Data Preprocessing & Feature Engineering 🔍  
- **Handled missing values** using imputation techniques.  
- **Encoded categorical variables** (if applicable).  
- **Transformed skewed features** to improve model performance.  
- **Identified and removed outliers** where necessary.  
- **Checked for multicollinearity** using **Variance Inflation Factor (VIF)**.  

### 3️⃣ Model Development 🏗  
- Built a **Multiple Linear Regression (OLS) model**.  
- **Selected the best features** using backward elimination and statistical significance tests.  
- Evaluated the model using **Adjusted R² and Root Mean Squared Error (RMSE)**.  

### 4️⃣ Model Diagnostics & Evaluation 📉  
- **Linearity check**: Ensured linear relationships between features and the target variable.  
- **Independence of errors**: Used **Durbin-Watson test** for serial correlation.  
- **Heteroskedasticity assessment**: Applied **Breusch-Pagan test** to check for variance in errors.  
- **Normality of residuals**: Verified using **QQ plots and Shapiro-Wilk test**.  
- **Multicollinearity check**: Used **VIF values** to detect highly correlated features.  

---

## 📈 Key Results & Findings  
- **Final Model Equation:** (To be updated based on your model)  
- **Adjusted R²:** (To be updated)  
- **RMSE:** (To be updated)  

Our model successfully predicts cancer mortality rates with a reasonable level of accuracy. Further improvements can be made by incorporating additional features or using more complex models like **Random Forest Regression or Gradient Boosting**.  

---

