#1
import math
array = []
for _ in range(10):
    num = int(input())
    array.append(num)
print("Ответ: ")
sum = 0
for i in range(10):
    if array[i] % math.sqrt(array[i]) == 0:
        sum+=array[i]
print(sum)