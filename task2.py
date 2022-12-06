# напишите программу, которая найдет произведение
# пар чисел списка. первый и последний, второй и предпоследний
# [2,3,4,5,6] -> [12,15,16]

list = [2,3,4,5,6]
print(list)

import math
size = math.ceil(len(list)/2)
print(size)
list1 = []
for i in range (size):
    list1.append(list[i]*list[len(list)-1-i])
print(list1)






