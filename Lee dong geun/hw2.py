input1 = input("몇단:")
i=0
while True:
    i += 1
    if i > 9: break
    print(int(input1)*i)
# 구구단을 출력하는 것이 과제(-2)
    
def 홀짝판별(number):
    if number%2 == 1:
        print("홀수")
    else:
        print("짝수")

홀짝판별(4)

def 평균(*a):
    result = 0
    for i in a:
        result += i
    return result / len(a)



평균(1,2,3,4,5)