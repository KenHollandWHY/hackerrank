#!/usr/bin/python
from __future__ import division
import scipy.stats

max_val = 250
n = 100
mu = 2.4
sigma = 2.0

# sum(Xi) ~ N(n*mu, pow(n, 1/2)*sigma)
print('%.4f'%scipy.stats.norm.cdf(max_val, loc=n*mu, scale=pow(n, 1/2)*sigma))
