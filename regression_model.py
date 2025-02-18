import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from data_processing import split_data  # Assuming a custom function for splitting data

# Function to identify highly correlated features
def correlation_among_numeric_features(df, cols):
    numeric_col = df[cols]
    corr = numeric_col.corr()
    corr_features = set()

    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > 0.8:  # Threshold for high correlation
                colname = corr.columns[i]
                corr_features.add(colname)
    return corr_features

# Function to train Linear Regression model
def lr_model(x_train, y_train):
    X_train_with_intercept = sm.add_constant(x_train)  # Adding constant for intercept
    lr = sm.OLS(y_train, X_train_with_intercept).fit()
    return lr

# Function to identify significant variables based on p-values
def identify_significant_vars(lr, p_value_threshold=0.05):
    print("P-values:", lr.pvalues)
    print("R-squared:", lr.rsquared)
    print("Adjusted R-squared:", lr.rsquared_adj)

    significant_vars = [var for var in lr.pvalues.keys() if lr.pvalues[var] < p_value_threshold]
    return significant_vars

if __name__ == "__main__":
    capped_data = pd.read_csv("/Users/phanindrakumar/Desktop/OLSRegressionChallenge/capped_data.csv")
    print("Data Shape:", capped_data.shape)

    # Select columns with more than 3 unique values
    # cols = capped_data.nunique()[capped_data.nunique() > 3].keys().tolist()

    # Remove highly correlated features
    corr_features = correlation_among_numeric_features(capped_data, capped_data.columns)
    print("Highly Correlated Features:", corr_features)

    highly_corr_cols = [
        "povertyPercent", "MedianAge", "PctPrivateCoverageAlone", "MedianAgeFemale",
        "PctEmpPrivCoverage", "PctBlack", "popEst2015", "PctMarriedHouseholds",
        "upper_bound", "lower_bound", "PctPrivateCoverage", "MedianAgeMale",
        "state_ District of Columbia", "PctPublicCoverageAlone"
    ]

    # Ensure the target column is included
    cols = [col for col in capped_data.columns if col not in highly_corr_cols]
    len(cols)
    # Split the data
    x_train, x_test, y_train, y_test = split_data(capped_data[cols], "TARGET_deathRate")
    # Train the model
    lr = lr_model(x_train, y_train)
    summary = lr.summary()
    print(summary)
    
    # import numpy as np

    # # Handle NaNs and infinite values in x_train and y_train
    # x_train = x_train.replace([np.inf, -np.inf], np.nan).dropna()
    # y_train = y_train.loc[x_train.index]  # Ensure target aligns with cleaned features

    

    # Identify significant variables
    # significant_vars = identify_significant_vars(lr)
    # print("Number of Significant Variables:", len(significant_vars))

    # # Train the model with significant variables
    # significant_vars.remove("const")
    # lr = lr_model(x_train[significant_vars], y_train)
    # summary = lr.summary()
    # print(summary)

# print(capped_data.columns)
