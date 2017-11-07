# import python datamining libs

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Loading dataset

dataset = pd.read_csv('input_data.csv')
print(len(dataset))
print(dataset.columns.values)

# Spliting dataset
def split_data(dataset):
    square_feet_values = []
    price_values = []
    for square_feet, price in zip(dataset['square_feet'], dataset['price']):
        square_feet_values.append([square_feet])
        price_values.append(price)
    return square_feet_values, price_values


train_x, train_y = split_data(dataset)
print(train_x)
print(train_y)

# Building the model
regr = linear_model.LinearRegression()
regr.fit(train_x, train_y)

# Fiting the model

plt.scatter(train_x, train_y, color = 'blue')
plt.plot(train_x, regr.predict(train_x), color = 'Red', linewidth = 4)
plt.show()

# Predicting the price for 700 square feet

print(regr.predict(700))
