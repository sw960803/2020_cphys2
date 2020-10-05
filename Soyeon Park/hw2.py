def times_tables(a):
    n=[1,2,3,4,5,6,7,8,9]
    return [x*a for x in n]
# 구구단을 출력해야함(-2)
    
def checkeven(a):
    if a%2 == 0:
        answer='even'
    else :
        answer='odd'
    return answer

import numpy as np
a=np.array([22,37,48,20,99,97])
b=np.mean(a)
print (b)
# 깔끔한 코드지만 과제는 '리스트'를 입력받는 '함수'를 만들어서 문제를 해결하는 것이었음(-2)