def mul1(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]
# 구구단을 출력해야함(-2)

def solution(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'

a = [65,84,45,548,52,999,111,252]
total=0
for score in a:
    total += score
average = total/len(a)
print(average)
# 평균을 계산하는 '함수'를 작성하는 것이 과제임(-1)