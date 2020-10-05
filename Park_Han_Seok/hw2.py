def multip(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
# 구구단을 출력해야 함(-2)
    
def numchecker(a):
    if a%2==0:
        return print('even')
    else:
        return print('odd')
    
def average(a):
    b=0
    for i in range(len(a)):
        b=b+a[i]
    return b/len(a)