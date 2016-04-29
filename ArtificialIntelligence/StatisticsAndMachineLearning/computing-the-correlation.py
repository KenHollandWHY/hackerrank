def multiple(list_x, list_y):
    return [x*y for x,y in zip(list_x, list_y)]

def pearson_coefficient(x, y):
    n = len(x)
    X = ((n*sum(multiple(x,x)) - (sum(x))**2))**(1/2)
    Y = ((n*sum(multiple(y,y)) - (sum(y))**2))**(1/2)
    r_xy = (n*sum(multiple(x, y)) - sum(x)*sum(y))/(X*Y)
    return r_xy

N = int(input().strip())
mathematics = []
physics = []
chemistry = []

for n in range(N):
    m,p,c = [int(x) for x in input().strip().split()]
    mathematics.append(m)
    physics.append(p)
    chemistry.append(c)


mp = pearson_coefficient(mathematics, physics)
print('%.2f'%mp)
pc = pearson_coefficient(physics, chemistry)
print('%.2f'%pc)
cm = pearson_coefficient(chemistry, mathematics)
print('%.2f'%cm)
