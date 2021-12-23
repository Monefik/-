import random
a = random.randint(0,20)
print(a)
while True:
    b = int(input("Ввведите число: "))
    if a == b:
        print("Вы угадали")
        break
    else:
        print("Вы не угадали")
