import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def z1():
    while True:
        try:
            a = int(input("Введите число 1\n"))
            b = int(input("Введите число 2\n"))
            print(lcm(a, b))
            break
        except ValueError:
            print("Введено некорректное значение. Пожалуйста, введите число.")
