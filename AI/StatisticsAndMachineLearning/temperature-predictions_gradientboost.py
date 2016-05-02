##########################
# use Gradient Boost Regression
# score: 87.75/100
##########################

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

month_dict = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12}


if __name__ == "__main__":

    N = int(input())
    _ = input()

    max_train_X = []
    max_train_y = []
    min_train_X = []
    min_train_y = []
    max_test_X = []
    min_test_X = []

    # load data
    data = [input().strip().split() for i in range(N)]

    # assign to training data and test data
    for yyyy, month, tmax, tmin in data:

        if tmax.startswith("Missing"):
            max_test_X.append([int(yyyy), month_dict[month], float(tmin)])
        elif tmin.startswith("Missing"):
            min_test_X.append([int(yyyy), month_dict[month], float(tmax)])
        else:
            max_train_X.append([int(yyyy), month_dict[month], float(tmin)])
            max_train_y.append(float(tmax))
            min_train_X.append([int(yyyy), month_dict[month], float(tmax)])
            min_train_y.append(float(tmin))



    # training
    gbr_max = GradientBoostingRegressor()
    gbr_max.fit(max_train_X, max_train_y)

    gbr_min = GradientBoostingRegressor()
    gbr_min.fit(min_train_X, min_train_y)

    # predict
    #print(max_train_X)
    #print(max_test_X)
    index_max = 0
    index_min = 0
    for yyyy, month, tmax, tmin in data:
        if tmax.startswith("Missing"):
            y = gbr_max.predict([max_test_X[index_max]])
            print("%.1f"%y)
            index_max += 1
        elif tmin.startswith("Missing"):
            y = gbr_min.predict([min_test_X[index_min]])
            print("%.1f"%y)
            index_min += 1
        else:
            pass