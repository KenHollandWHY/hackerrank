#!/usr/bin/python
import scipy.stats

normal = scipy.stats.norm(loc=70, scale=10)

# P(X>80)
P0 = 1 - normal.cdf(80)
print('%.2f'%(100*P0))

# P(X>=60)
P1 = normal.cdf(60)
P2 = 1 - P1
print('%.2f'%(100*P2))

# P(60 < X)
print('%.2f'%(100*P1))
