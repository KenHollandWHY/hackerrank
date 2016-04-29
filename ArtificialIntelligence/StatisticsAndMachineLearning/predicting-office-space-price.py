from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

F,N = map(int, input().strip().split())

X_train = []
y_train = []

# load training data
for n in range(N):
    x = list(map(float, input().strip().split()))
    X_train.append(x[0:F])
    y_train.append(x[-1])

# load test data
X_test = []
T = int(input())
for j in range(T):
    x = list(map(float, input().strip().split()))
    X_test.append(x)

#print(X_test)

# Create linear regression object
model = Pipeline([
    ('poly', PolynomialFeatures(degree=3)),
    ('linear', LinearRegression(fit_intercept=False))])


# Train the model using the training sets
model.fit(X_train, y_train)

# The mean square error
y_predict = model.predict(X_test)

# print the results
for x in y_predict:
    print("%.2f"%x)
