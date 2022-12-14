import numpy as np
import time
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), range(5)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=int(time.time()))

print(X_train, X_test, y_train, y_test)