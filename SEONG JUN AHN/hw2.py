def gugudan(a):
    X1=[]
    x1=1
    for i in range(1,10):
        x1=a*i
        X1.append(x1)
    return X1
# 구구단을 출력하는 것이 과제(-2)

def holjjak(b):
    if b%2==0:
        print('even')
    else:
        print('odd')

def mean(c):
    x3=0
    for i in range(0,len(c),1):
        x3+=c[i]
    return x3/len(c)