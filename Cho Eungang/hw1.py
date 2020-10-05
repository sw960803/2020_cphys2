def dan(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
def gugudan(a):
    f=1
    x=dan(f)
    for f in range(1,a):
        f=f+1
        x=x+dan(f)
    return x
print(gugudan(9))
# 구구단을 출력해야 함(-2)