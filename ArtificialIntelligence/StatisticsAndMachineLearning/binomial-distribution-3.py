from scipy.stats import binom

n = 10
p = 0.12

rv = binom(n, p)
# no more than 2 rejects => P(X<=2)
P = rv.pmf(0) + rv.pmf(1) + rv.pmf(2)
print('%.3f'%P)

# at least 2 rejects => P(X>=2) = 1 - P(X<=1)
P = 1 - (rv.pmf(0) + rv.pmf(1))
print('%.3f'%P)
