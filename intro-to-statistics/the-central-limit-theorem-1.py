#!/usr/bin/python
from __future__ import division
import scipy.stats

max_val = 9800
n = 49
mu = 205
sigma = 15

# [Method 1] Use the Central Limit Theorem
# z = (max_val - n*mu)/(pow(n, 1/2)*sigma)
# print('%.4f'%scipy.stats.norm.cdf(z, loc=0, scale=1))

# [Method 2] Use this fact: sum(Xi) ~ N(n*mu, pow(n, 1/2)*sigma)
print('%.4f'%scipy.stats.norm.cdf(max_val, loc=n*mu, scale=pow(n, 1/2)*sigma))
