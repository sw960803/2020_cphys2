def gugudan(x):
        for i in range(1,10):
            print(x,"*",i,"=",x*i)

def scan(x):
    if x%2 == 0:
        print("odd number")
    else :
        if x%2 == 1:
            print("even number")
        else :
            print("정수가 아닙니다")

def average(list):
    num = 0
    for i in range(len(list)):
        num = num + list[i]
    return (num)/len(list)


print("평균값 : {}".format(average(list)));