def mul1(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
# 구구단을 출력해야함(-2)
    
def solution(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
A = [42, 59, 40, 20, 5, 29]
total=0
for score in A:
    total += score
average = total/len(A)
print(average)
# 평균을 계산하는 '함수'를 작성하는 것이 과제임(-1)