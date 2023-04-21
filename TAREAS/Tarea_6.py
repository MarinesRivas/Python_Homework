
#MARIA RIVAS RECENDEZ

#TAREA 6

#SELECCION DE CARACTERISTICAS

import pandas as pd
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform forward feature selection
n_features = 5  # number of features to select
estimator = LinearRegression()
selected_features = set()

for i in range(n_features):
    best_score = 0
    best_feature = None
    
    for feature in X.columns:
        if feature not in selected_features:
            selected_features.add(feature)
            X_selected = X[list(selected_features)]
            scores, _ = f_regression(X_selected, y)
            score = scores.mean()
            
            if score > best_score:
                best_score = score
                best_feature = feature
                
            selected_features.remove(feature)
            
    selected_features.add(best_feature)

print('Selected features:', list(selected_features))