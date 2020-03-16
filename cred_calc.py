######
######
# расчет переплаты процентов за кредит

def credit():
    cred = float(input("Введите сумму стоимости автомобиля: "))
    self_sum = float(input("Введите сумму первого взноса: "))
    sm = cred - self_sum
    st = input("Введите процент годовой ставки: ")
    st = st.replace(",", ".")
    st_percent = float(st) / 100
    year = float(input("Введите срок кредита (в годах): "))
    sum_pog = float(input("Введите сумму остаточного платежа: "))
    sum_main = 0
    if sum_pog == '':
        sum_pog = sum_main
    st_cred = (year * st_percent * sm + sm - sum_pog) // (year * 12)
    print(f"Проценты переплаты за {int(year)} года/лет: "
          + (str(float(st_percent * year * (cred - sum_pog))) + (str(" рублей"))))
    print(f"Ежемесяцный платеж: {st_cred}" + " рублей")
    print(f"Остаточный платеж: {sum_pog}")


ans = ['да', 'yes', 'y']

while True:
    credit()
    ex = input("Хотите повторить оперцию ?: ")
    if ex not in ans:
        break
