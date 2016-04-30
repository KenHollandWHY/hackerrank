from scipy.stats import binom
n = 4
p = 4/5
rv = binom(n, p)

# more than 2 hits => P(X>2) = P(X=3) + P(X=4)
P0 = rv.pmf(3) + rv.pmf(4)
print('%.3f'%P0)

# at least 3 misses => P(X<=1) = P(X=0) + P(X=1)
P1 = rv.pmf(0) + rv.pmf(1)
print('%.3f'%P1)
