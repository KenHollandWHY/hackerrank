from __future__ import division

def std_deviation(array):
    l = len(array)
    mean = sum(array)/l
    s = pow(sum(map(lambda x: (x-mean)**2, array))/l, 1/2)
    return s

ar0 = [1,2,3]
d = 0.01
x = 2

val0 = std_deviation(ar0)
#print val0
while True:
    ar1 = ar0[:]
    ar1.append(x)
    val1 = std_deviation(ar1)

    if((val1 - val0) >= 0):
        x -= d
        break;
    x += d

print "%.2f"%x