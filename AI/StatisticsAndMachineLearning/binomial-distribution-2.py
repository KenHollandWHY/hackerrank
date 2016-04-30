from scipy.stats import binom

n = 6
p = 1.09/(1.09 + 1) # The probability of getting a boy

# at least 3 boys => P(X>=3) = P(X=3) + P(X=4) + P(X=5) + P(X=6)
rv = binom(n, p)
P = rv.pmf(3) + rv.pmf(4) + rv.pmf(5) + rv.pmf(6)
print('%.3f'%P)
