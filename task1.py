# напишите программу, которая найдет сумму элементов списка,
# стоящих на нечтной позиции
# [2,3,5,9,3] -> 12

list = [2,3,5,9,3]
print(list)
sum = 0
for i in range (len(list)):
    if i%2 !=0:
        sum = sum + list[i]
print(sum)