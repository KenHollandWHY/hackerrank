#P for price index
#S for the commodity stock.

P_mu = 100
P_std = 8
S_mu = 103
S_std = 4

# The R^2 correlation coefficient between the two series is 0.4
R_squared = 0.4

# want the slope of the regression line of P on S
# assume that r > 0 # how can we determine if r > 0 or r < 0 ?
r = pow(R_squared, 0.5)
b_ps = r * P_std/S_std
print ("%.2f"%b_ps)