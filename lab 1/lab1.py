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

























#4. «Карманные деньги». У студента есть n рублей (вводится с клавиатуры). 
#Кусок пиццы стоит 80 рублей, хлеб – 45 рублей, лапша быстрого приготовления – 15 рублей, молоко – 85 рублей, шоколадный батончик – 55 рублей, чипсы – 67 рублей,
#шаурма – 190 рублей. Вывести на экран продукты, которые он может купить 
#(пицца и хлеб, пицца и лапша, пицца+хлеб+молоко, пицца+пицца+молоко и т.д. ) и сколько денег у него останется при каждом варианте покупки. 
def calculate_products(money):
    products = {
        'пицца': 80,
        'хлеб': 45,
        'лапша': 15,
        'молоко': 85,
        'шоколадный батончик': 55,
        'чипсы': 67,
        'шаурма': 190
    }
    combinations = []
    for i in range(1, len(products) + 1):
        for combo in combinations_generator(products, i):
            total_cost = sum(combo.values())
            if total_cost <= money:
                remaining_money = money - total_cost
                if remaining_money >= 0:
                    combinations.append((combo, remaining_money))
    return combinations

def combinations_generator(products, length):
    if length == 1:
        for product, price in products.items():
            yield product
    else:
        for product, price in products.items():
            remaining_products = dict(products)
            del remaining_products[product]
            
            for combo in combinations_generator(remaining_products, length - 1):
                combo[product] = price
                yield combo

money = int(input("money = "))
combinations = calculate_products(money)
print("Возможные комбинации продуктов и остаток денег:")
for combo, remaining_money in combinations:
    print(combo, "Остаток:", remaining_money)
# for combo in combinations:
#     total_cost = sum(combo.values())
#     remaining_money = money - total_cost
#     print(combo, f"/n Остаток:", remaining_money)

 
