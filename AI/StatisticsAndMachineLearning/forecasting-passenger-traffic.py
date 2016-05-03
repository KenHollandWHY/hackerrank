import numpy as np
from sklearn import linear_model

#load input sample data
N = int(input().strip())

y_train_all = [[] for m in range(12)]
regr = [None for m in range(12)]

for i in range(N):
    month = i%12
    y_train_all[month].append(int(input().strip().split()[1]))

for month in range(12):
    y_train = y_train_all[month]
    X_train = range(len(y_train))

    # Create linear regression object
    regr[month] = linear_model.LinearRegression()

    #print(np.array(X_train).reshape(-1, 1))
    # Train the model using the training sets
    regr[month].fit(np.array(X_train).reshape(-1, 1), np.array(y_train).reshape(-1, 1))

# The mean square error
for m in range(N, N+12):
    month = m%12
    x = len(y_train_all[month])

    #print(x)
    X_test = [x]
    y_predict = regr[month].predict(np.array(X_test).reshape(-1, 1))
    print("%d"%y_predict[0][0])
