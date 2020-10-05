def MulTable(n):
    result = []
    for i in range(1,10):
        result.append(n*i)
    return result
for i in range(1,10):
    print(MulTable(i))
# 구구단을 출력해야함(-2)

def is_odd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1
 
def is_odd_even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def ListMean(n):
    if isinstance(n, list):
        sum = 0
        length = len(n)
        for i in range(length):
            if isinstance(n[i], int)==False:
                return "Invalid Element"
            else:
                sum += n[i]
        return sum / length
    else:
        return "Invalid Element"