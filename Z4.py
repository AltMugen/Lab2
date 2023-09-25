def demonstrate():
    try:
        print("Внутри блока try")
        x = 1 / 0
    except ZeroDivisionError:
        print("Обработка исключения")
    finally:
        print("Блок finally")
def z4():
    demonstrate()
