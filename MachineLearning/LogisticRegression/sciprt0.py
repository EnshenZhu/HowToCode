import math

import numpy as np
import pandas as pd
import matplotlib

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

rawData = {"X":
               [301,
                310,
                324,
                336,
                321,
                315,
                304,
                297,
                290,
                303
                ],
           "y":
               [0.67,
                0.72,
                0.89,
                0.95,
                0.79,
                0.39,
                0.38,
                0.34,
                0.47,
                0.56
                ]}

pd_data = pd.DataFrame(data=rawData)

X_train = np.array(pd_data.iloc[:, 0]).reshape(-1, 1)
print(X_train.shape)
y_train = np.round(np.array(pd_data.iloc[:, 1]).reshape(-1, ))
print(y_train.shape)

lg_reg_model = LogisticRegression(random_state=0).fit(X_train, y_train)

y_predict = [lg_reg_model.predict((item[0].reshape(1, -1)))[0] for item in X_train]
print(y_predict)
