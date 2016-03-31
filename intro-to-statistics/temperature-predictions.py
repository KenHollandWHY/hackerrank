'''
#ATTENTION!! I only got 22.60/30.00 points with this script.
'''

import numpy as np
from scipy.interpolate import interp1d

if __name__ == "__main__":
    #load input sample data
    N = int(raw_input())
    _ = raw_input()

    max_min_data = [[], []]
    missing_data = []
    x_range = [[], []]
    for i in range(N):
        yyyy, month, tmax, tmin = raw_input().strip().split()
        if not tmax.startswith("Missing"):
            max_min_data[0].append(float(tmax))
            x_range[0].append(i)
        else:
            missing_data.append([i,0])
        if not tmin.startswith("Missing"):
            max_min_data[1].append(float(tmin))
            x_range[1].append(i)
        else:
            missing_data.append([i,1])


    # prediction of max temperatur
    # for each max and min
    f = []
    for j in range(2):
        x = x_range[j]
        y = max_min_data[j]
        f.append(interp1d(x, y, bounds_error=False, fill_value="extrapolate"))
    #print x_range[1]

    # predict
    for l in missing_data:
        j = l[1]
        x = l[0]
        #print(j,x)
        print "%.1f"%f[j](x)
