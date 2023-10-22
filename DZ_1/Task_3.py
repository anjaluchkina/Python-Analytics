# Даны два списка: дата покупки dates, суммы покупок по датам income.
# Найти итоговую сумму всех покупок в ноябре и сохранить ее в переменную x.
# Используйте list comprehensions.

dates = ["2021-11-01"]
income = [100]


dates = [date.split("-") for date in dates]  # Разбиваем даты на год, месяц и день


dates = [
    [int(date) for date in date_list] for date_list in dates
]  # Преобразуем списки строк в списки целых чисел


november_purchases = [
    income[i] for i in range(len(income)) if dates[i][1] == 11
]  # Отбираем только те покупки, которые совершены в ноябре


x = sum(november_purchases)  # Суммируем все покупки

print(x)
