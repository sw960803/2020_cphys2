def multi(x):
    multi_=[]
    print(str(x)+' times \n')
    for idx in range(1,10,1):
        multi_.append(idx*x)
        print(str(x)+' x '+str(idx)+' = '+str(idx*x),'\n')
    return multi_
print(multi(8))

def evenorodd(y):
    try :
        if y-int(y) !=0 :
            print('Please check whether the number is integer or not.')
        elif y%2 ==1:
            print(str(y)+' is an odd.')
        else:
            print(str(y)+' is an even')
    except:
        print('Please input number.')

def avg(a):
    try:
        if type(a) == int or type(a) == float:
            return a
        else:
            val = 0
            for idx in a:
                val += idx
            return val/len(a)
    except:
        return print("Please check your data type! it must be list that is consisted with number!")