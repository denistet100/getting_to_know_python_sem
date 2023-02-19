# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

while True:

    three_dig_num = int(input("Введите целое трёхзначное число:"))
    num_sum = three_dig_num // 100 + three_dig_num // 10 % 10 + three_dig_num % 10
    print(num_sum)

    cont = str(input("Введите n, если хотите остановить программу, если продолжить, то любую клавишу:"))
    if cont.lower() == "n":
        break
    else:
        continue
