salary = 5000    # Ежемесячная зарплата
spend = 6000     # Траты за первый месяц
months = 10      # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен (Исправил коэффициент, чтобы лишних строк не писать)

money_capital = 0     # Cумма, которую нужно взять из подушки в первый месяц
current_spend = spend # Текущие расходы

for month in range(months):
    shortage = current_spend - salary  # Считаем нехватку в текущем месяце
    money_capital += shortage          # Увеличиваем на нехватку подушку безопасности
    current_spend *= increase          # Увеличиваем траты на следующий месяц

money_capital = round(money_capital)   # Округляем до целого

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
