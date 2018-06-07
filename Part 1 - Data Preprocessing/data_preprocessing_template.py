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


# Spyder > 3.2 has a problem displaying x, so this will help with that.
display_x = pd.DataFrame(x)
display_y = pd.DataFrame(y)

# Take care of missing data by taking the mean of the data available
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(x[:, 1:3])

x[:,1:3] = imputer.transform(x[:,1:3])
