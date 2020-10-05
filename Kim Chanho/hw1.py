import numpy as np
n = 9
x = np.linspace(1,n,n)

for i in range(len(x)):
    print(i+1,'단')
    for j in range(len(x)):
        print(i+1,'*',j+1,'=',(i+1)*(j+1))
    print('\n')