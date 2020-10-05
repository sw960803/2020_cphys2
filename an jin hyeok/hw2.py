num = input("숫자를 입력하세요: " )
a=int(num)
for i in range (1,10):
    print(a,'*',i,'=',a*i)
# 구구단을 출력하는 '함수'를 작성하는 것이 과제(-1)
    
b=int(input("정수: "))
if (b%2==1):
    print("홀수입니다.")
else:
    print("짝수입니다.")
# '함수'를 작성했어야 함(-1)
    
c=list(map(int,input().split()))
sum = 0
for i in range(len(c)):
    sum=sum+c[i]
average=sum/len(c)
print(average)
# '함수'를 작성했어야 함(-1)