from scipy import stats

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
#print(slope, intercept, r_value, p_value, std_err)

test = 80
val = slope*test + intercept
print '%.1f'%val