#!/usr/bin/python
from __future__ import division
import scipy.stats

popularity = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
price = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

# Pearson coefficient
pc = scipy.stats.pearsonr(popularity, price)
print('%.3f'%pc[0])

# Spearman Rank coefficien
#print scipy.stats.rankdata(popularity)
#print scipy.stats.rankdata(price)
sc = scipy.stats.spearmanr(popularity, price)
print('%.1f'%sc.correlation)