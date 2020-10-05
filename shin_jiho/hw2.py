value = input()

print('-'*50)
print('(',value,'단',')')
for i in range(1,10):
	print(int(value)*i)
# 구구단을 출력해야 하며 함수 형태로 작성되야 하는 것이 과제였음(-2)
    
num = input()

def even(num):
	remainder = int(num) % 2
	if remainder == 0:
		return print('even')
	else:
		return print('odd')

even(num)

import numpy as np

data_size = np.random.randint(10)
num_list = np.random.randint(data_size,size=data_size)

print(num_list)

def average(num_list):
	list_length = len(num_list)
	sum = 0
	for i in range(list_length):
		sum += num_list[i]
	average_result = sum/list_length
	return print(average_result)

average(num_list)