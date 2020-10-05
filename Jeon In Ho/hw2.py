def mu(a):
    x= [1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
# 구구단을 출력해야함.(-2)
    
def f(q):
    if q%2 == 0 :
        return "even"
    else :
        return "odd"

def Average(list):
    Q = 0
    for i in range(len(list)):
        Q += list[i]
    return Q / len(list)
L = [i**3 for i in range(0,10)]
L, Average(L)
