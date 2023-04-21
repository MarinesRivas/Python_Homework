
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


import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the LASSO regression model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(lasso.coef_, index=X.columns)
print('Selected features:\n', coef[coef != 0])


import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the Ridge regression model
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(ridge.coef_, index=X.columns)
print('Selected features:\n', coef)