def mul2(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]

mul2(4)
# 구구단을 출력해야함(-2)

def avg(a):
    i= 0
    s = 0
    for i in range(len(a)):
        s = s + a[i]
    avg= s/len(a)
    return avg

def odd(a):
    x = "odd"
    y = "even"
    if(a % 2 == 1):
        return x
    else:
        return y