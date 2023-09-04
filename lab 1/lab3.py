import random
from faker import Faker

fake = Faker("ru_RU")

length = int(random.random() * 10 + 3)
grup1 = []
for _ in range(length):
    grup1.append(fake.name())

length = int(random.random() * 10 + 3)
grup2 = []
for _ in range(length):
    grup2.append(fake.name())

# Обмен элементами
for _ in range(3):
    i1 = int(random.random() * len(grup1))
    i2 = int(random.random() * len(grup2))
    temp = grup1[i1]
    grup1[i1] = grup2[i2]
    grup2[i2] = temp

grup1.pop(len(grup1)-1)
grup2.pop(len(grup2)-1)
grup1.sort()
grup2.sort()
print(grup1)
print(grup2)














































# from faker import Faker
# fake = Faker("ru_RU")

# length = int(random.random() * 10)
# grup1 = []*length
# for _ in range(len(grup1)):
# 	grup1.append(fake.name)


# length = int(random.random() * 10)
# grup2 = []*length
# for _ in range(len(grup2)):
# 	grup2.append(fake.name)

# # Обмен элементами
# for _ in range(3):
# 	i1 = int(random.random() * 10)
# 	i2 = int(random.random() * 10)
#     temp = grup1[i1]
#     grup1[i1] = grup2[i2]
#     grup2[i2] = temp

# grup1.pop(len(grup1)-1)
# grup2.pop(len(grup2)-1)
# print(grup1.sort())
# print(grup2.sort())

