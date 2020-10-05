def gugudan(n):
    t=0
    print("%d단" % n)
    while (t<=8):
        t = t+1
        print("%d x %d =%d" %(n,t,n*t))
        
def odd(n):
    if n % 2==0:
        print('짝수')
    else:
        print('홀수')

a=[1,2,3,4,5,6,72,34,56,78]
i=0
s=0
while i < len(a):
    s += a[i]
    i += 1
print(s / len(a))
# 함수를 작성했어야 함(-1)