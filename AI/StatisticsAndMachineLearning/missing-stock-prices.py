##########################
# use interpld version
# score: 56.23
##########################

from datetime import datetime
from scipy.interpolate import interp1d

if __name__ == "__main__":

    N = int(input())

    train_X = []
    train_y = []
    test_X = []

    # load data
    data = [input().strip().split() for i in range(N)]

    # assign to training data and test data
    for day, time, value in data:
        _temp = "%s %s"%(day, time)
        date_object = datetime.strptime(_temp, '%m/%d/%Y %H:%M:%S')
        t = int(date_object.strftime('%s'))

        if value.startswith("Missing"):
            test_X.append(t)
        else:
            train_X.append(t)
            train_y.append(float(value))


    # training
    f = interp1d(train_X, train_y, bounds_error=False, fill_value="extrapolate")

    # predict
    test_y = f(test_X)
    for y in test_y:
        print("%.2f"%y)
