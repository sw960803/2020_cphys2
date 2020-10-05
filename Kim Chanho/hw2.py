import numpy as np
def gugudan(n):
    x = [1,2,3,4,5,6,7,8,9]
    for i in range(len(x)):
        print(n,'*', int(x[i]),'=',n*int(x[i]))
        
def even(n):
    if n%2 == 0:
        print('even')
    else:
        print('odd')

def average(a):
    total = 0 
    for i in range(len(a)):
        total += a[i]
    ave = total/len(a)
    return ave