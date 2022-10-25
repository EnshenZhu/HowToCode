import numpy as np
import pandas as pd
import matplotlib

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

rawData = {"X":
               [337, 324, 316, 322, 314, 330, 321, 308, 302, 323, 325, 327, 328, 307, 311, 314, 317, 319,
                318,
                303],
           "y":
               [0.92, 0.76, 0.72, 0.8, 0.65, 0.9, 0.75, 0.68, 0.5, 0.45, 0.52, 0.84, 0.78, 0.62, 0.61, 0.54,
                0.66,
                0.65, 0.63, 0.62]}

pd_data = pd.DataFrame(data=rawData)

X_train = np.array(pd_data.iloc[:, 0]).reshape(1, -1)
print(X_train.shape)
y_train = pd_data.iloc[:, 1]
print(y_train.shape)

lg_reg_model = LogisticRegression(random_state=0).fit(X_train, y_train)

# y_predict = [lg_reg_model.predict(item) for item in X_train]
# print(y_predict)
