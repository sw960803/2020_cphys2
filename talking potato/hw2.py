def mul(a):
    for j in range(9):
            print(a*(j+1))
# 구구단을 출력해야함(-2)
            
def check(a):
    if a%2==1:
        print ("odd")
    
    else:
        print ("even")
        
def average(list):
    d = 0
    for i in list:
        d = d + i
    return d / len(list)