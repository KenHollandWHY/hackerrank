#!/usr/bin/python
import scipy.stats

normal = scipy.stats.norm(loc=30, scale=4)

# P(X<40)
print('%.3f'%normal.cdf(40))

# P(X>21)
print('%.3f'%(1-normal.cdf(21)))

# P(30 < X < 35)
print('%.3f'%(normal.cdf(35)-normal.cdf(30)))
