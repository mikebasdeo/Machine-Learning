# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("Data.csv")

# Distinguish between matrix of features and dependent variable vector

# Matrix of features, all rows, columns except last one.
x = dataset.iloc[:, :-1].values

# Dependent variable vector
y = dataset.iloc[:,3].values


# Spyder > 3.2 has an error re:displaying object arrays, so this will help with that.
display_x = pd.DataFrame(x)
display_y = pd.DataFrame(y)



# Take care of missing data by taking the mean of the data available
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(x[:, 1:3])

x[:,1:3] = imputer.transform(x[:,1:3])

# Encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_x = LabelEncoder()
x[:, 0] = label_encoder_x.fit_transform(x[:, 0])

# Dummy encoding for MOF
one_hot_encoder = OneHotEncoder(categorical_features=[0])
x = one_hot_encoder.fit_transform(x).toarray()

# Dummy encoding for DVV
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)


# Split data into training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
# fit to the training, data, not to the test data.
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)


















