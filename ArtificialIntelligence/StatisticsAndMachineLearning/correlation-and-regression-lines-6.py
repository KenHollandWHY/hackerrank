from scipy.stats import pearsonr

physics_scores = [15,12,8,8,7,7,7,6 ,5,3]
history_scores = [10,25,17,11,13,17,20,13,9,15]

coef, p_value = pearsonr(physics_scores, history_scores)
print('%.3f'%coef)