'''
# first: check training data
import matplotlib.pyplot as plt
X_train = []
y_train = []
with open('trainingdata.txt') as f:
    for x in f.readlines():
        charged, lasted = map(float, x.strip().split(','))
        X_train.append(charged)
        y_train.append(lasted)

plt.plot(X_train, y_train, 'bo')
plt.show()
'''
# second: ftom the graph we've got this:
# y = 2*x if x < 4, y = 8 if x >= 4

x = float(input().strip())
if(x < 4):
    y = 2*x
else:
    y = 8
print("%.2f"%y)