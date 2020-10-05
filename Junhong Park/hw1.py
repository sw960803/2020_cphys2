print('구구단!\t1단 ~ 9단!\n\n')

for A in range(1, 10):
    print("{0}단 : ".format(A), end="")
    for B in range(1, 10):
        print(A*B, end=" ")
    print('')
# 구구단을 출력해야 함(-2)