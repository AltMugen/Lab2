from Z1 import *
from Z2 import *
from Z3 import *
from Z4 import *
v = 0
while v != 5:
    print("1. Задание 1\n2. Задание 2\n3. Задание 3\n4. Задание 4\n5. Выход\n")
    v = int(input("Выберите пункт меню\n"))
    if v == 1:
        z1()
    elif v == 2:
        z2()
    elif v == 3:
        z3()
    elif v == 4:
        z4()