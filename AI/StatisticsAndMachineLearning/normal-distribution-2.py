#!/usr/bin/python
import scipy.stats

normal = scipy.stats.norm(loc=20, scale=2)

# P(X<19.5)
print('%.3f'%normal.cdf(19.5))

# P(20 < X < 22)
print('%.3f'%(normal.cdf(22)-normal.cdf(20)))
