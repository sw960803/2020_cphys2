import numpy as np
def googoodan(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
# 구구단이 출력되야함(-2)
    
x=int(input("정수 x="))

if(x%2==1):
    print("홀수입니다.")
else:
    print("짝수입니다.")
# 함수를 작성해야함(-1)
    
list1 = list(map(int, input().split())) #원하는 리스트를 입력하시오.
sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]

def average(list1):
    return sum/len(list1)
average(list1)
# 리스트 요소들의 합을 구하는 과정은 평균을 구하는 과정의 일부이기에
# average 함수에 그 과정이 포함되어 있어야 한다고 생각하지만 감점은 하지 않겠음