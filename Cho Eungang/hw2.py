def dan(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
dan(3)
# 구구단을 출력해야 함(-2)
    
def hol(a):
    b=a%2
    if b==1:
        x='홀수'
    elif b==0:
        x='짝수'
    return x

def av(a):
    b=len(a)
    f=0
    x=a[f]
    for i in range(1,b):
        f=f+1
        x=x+a[f]
    return x/b