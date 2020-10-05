def gugudan(a):
    print("구구단")
    print("[", a, "단", "]")
    for x in range(1, 10):
            print(f'{a}x{x}={a*x}',end="\t")
    return

def distinction(x):
    if x <= 0:
        print("not positive integer")
    elif x%2 == 1:
        print("odd")
    elif x%2 == 0:
        print("even")
    else:
        print("not natural number")
    return
# 홀짝은 정수 영역에서 정의되는 것이긴 하나 감점요소는 물론 아님
    
def average(list):
    print("평균값")
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x/len(list)