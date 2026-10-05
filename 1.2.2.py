p=int(input("Цена одной тетради (руб): "))
c=int(input("Количество тетрадей: "))
s=int(input("Переданная сумма (руб): "))
co=p*c
sd=s-co
print(f"Стоимость: {co}")
print(f"Сдача: {sd}")