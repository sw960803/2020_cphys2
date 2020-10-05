num = input()
from math import *
for x in range(1,10):
            print('{} * {} = {}'. format(int(num), x, int(num) * x))

x = 22
if (x%2) == 0:
    print ("Even")
else:
    print ("odd")

num_list = [5,1,7,3,4]

def average(num_list):
    list_length = len(num_list)
    sum = 0
    for i in range(list_length):
        sum += num_list[i]
        average_result = sum/list_length
    return print(average_result)
    
average(num_list)