dan = 1

while dan :
    dan = int(input('몇단을 출력할까요?(종료: 0) : '))
    if dan == 0 :
        break
    else:
        for i in range (1, 10) :
            print('{} * {} = {}'.format(dan,i,dan*i))
# 함수를 작성하는 것이 과제였음(-1)
            

n=int(input("숫자 입력: "))
 
if n%2 == 1:
    print("홀수")
else:
    print("짝수")
# 함수를 작성하는 것이 과제였음(-1)
    
score = {"a": 92,
         "b": 83,
         "c": 55,
         "d": 76
         }

total = 0

for value in score.values():
    total += value

print('평균은 : %.1f 입니다.' %(total / len(score)))
# 잘 했지만 딕셔너리 자료형이 아니라 리스트 자료형을 받는 '함수'를 작성하는 것이 과제였음(-1)