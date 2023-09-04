#2
# import math
# x = int(input("Введите x: "))
# q = int(input("Введите v: "))
# b= int(input("Введите первый элемент геом. прогрессии b: "))
# for _ in range(10):
#     if(x==b*q):
#         print("Ответ: является")
n = input().split() #f s n
print(((int(n[2]) - int(n[0])) % int(n[1])) == 0)
