# Найдите выручку компании в зависимости от месяца Для этого напишите функцию calc_income_by_month(),
# которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - это выручка.
# Используйте аннотирование типов.

from typing import List, Dict


def calc_income_by_month(dates: List[str], incomes: List[int]) -> Dict[int, int]:
    incomebymonth = {}  # Создаем словарь для хранения выручки по месяцам

    dates = [date.split("-") for date in dates]  # Разбиваем даты на год, месяц и день

    dates = [
        [int(date) for date in datelist] for datelist in dates
    ]  # Преобразуем списки строк в списки целых чисел

    for i in range(len(incomes)):  # Считываем выручку по месяцам
        month = dates[i][1]  # Получаем месяц из даты

        if month in incomebymonth:  # Если месяц уже есть в словаре, добавляем выручку
            incomebymonth[month] += incomes[i]
        else:  # Если месяца нет в словаре, создаем его и присваиваем выручку
            incomebymonth[month] = incomes[i]

    return incomebymonth


dates = ["2021-11-01"]
incomes = [100]

incomebymonth = calc_income_by_month(dates, incomes)
print(calc_income_by_month(dates=["2021-11-01"], incomes=[100]))
