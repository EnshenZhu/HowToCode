from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)

print(type(X))
print(type(y))

print(X.shape)
print(y.shape)

print(y)

# clf = LogisticRegression(random_state=0).fit(X, y)
# clf.predict(X[:2, :])
# clf.predict_proba(X[:2, :])
# clf.score(X, y)

print(round(0.45))
