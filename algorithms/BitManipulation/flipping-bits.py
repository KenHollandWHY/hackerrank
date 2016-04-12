N = int(raw_input())
x = pow(2,32) - 1
for i in range(N):
    n = int(raw_input())
    print(x^n)