# Вариант 15. Дано трехзначное число. Вывести вначале его последнюю цифру
# (единицы), а затем — его среднюю цифру (десятки)


try:
    num = int(input("Введите трехзначное число: "))

    if num < 100 or num > 999:
        print("Число должно быть трехзначным")
    # Проверяем, что число является трехзначным
    else:
        last = num % 10
        middle = (num // 10) % 10

        print("Последняя цифра:", last)
        print("Средняя цифра:", middle)
        print('Программа успешно завершена!')
except:
    print("Неверный тип данных")
