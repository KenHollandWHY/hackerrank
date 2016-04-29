from sklearn import linear_model

#load input sample data
F, N = map(int, input().strip().split())

X_train = []
y_train = []

for i in range(N):
    x = list(map(float, input().strip().split()))
    X_train.append(x[0:F])
    y_train.append(x[-1])

#print(X_train)
#print(y_train)

X_test = []
T = int(input())
for j in range(T):
    x = list(map(float, input().strip().split()))
    X_test.append(x)

#print(X_test)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# The mean square error
y_predict = regr.predict(X_test)

# print the results
for x in y_predict:
    print("%.2f"%x)
