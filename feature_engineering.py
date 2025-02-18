import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def bin_to_num(data):
    
    binnedinc = []
    for i in data["binnedInc"]:
        i = i.strip("()[]")  # Remove parentheses and brackets
        
        i = i.split(",")

        i = tuple(i)

        i = tuple(map(float, i))

        i = list(i)

        binnedinc.append(i)  # Convert tuple to list
    
    data["binnedInc"] = binnedinc
    # Extract lower bound, upper bound, and calculate median
    data["lower_bound"] = [i[0] for i in data["binnedInc"]]
    data["upper_bound"] = [i[1] for i in data["binnedInc"]]
    data["median"] = (data["lower_bound"] + data["upper_bound"]) / 2
    
    data.drop("binnedInc", axis=1, inplace = True)
    return data


def cat_to_col(data):

    data['county'] = [i.split(",")[0] for i in data['Geography']]
    data['state'] = [i.split(",")[1].strip() for i in data['Geography']]

    data.drop("Geography", axis = 1, inplace = True)
    return data


from sklearn.preprocessing import OneHotEncoder

def one_hot_encoding(X):
    # Select categorical columns
    categorical_columns = X.select_dtypes(include=["object"]).columns
    print("Categorical Columns:", categorical_columns)
    
    # Initialize one-hot encoder
    one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    
    # Fit and transform categorical columns
    one_hot_encoded = one_hot_encoder.fit_transform(X[categorical_columns])
    
    # Create a DataFrame with one-hot encoded columns
    encoded_columns = one_hot_encoder.get_feature_names_out(categorical_columns)
    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoded_columns, index=X.index)
    
    # Drop original categorical columns and concatenate the new one-hot encoded columns
    X = X.drop(categorical_columns, axis=1)
    X = pd.concat([X, one_hot_df], axis=1)
    
    return X




























