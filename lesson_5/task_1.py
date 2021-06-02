from collections import namedtuple

number_enterprises = int(input("Введите кол-во предприятий: "))

Enterprises = namedtuple('Enterprises', ['name', 'cash'])
list_of_enterprises = []
sum_cash = 0
for i in range(number_enterprises):
    name = input("Введите название: ")
    cash = int(input("Введите прибыль за год: "))
    list_of_enterprises.append(Enterprises(name, cash))
    sum_cash += cash

avg = sum_cash / number_enterprises

for enterprise in list_of_enterprises:
    if enterprise.cash > avg:
        print(f'У {enterprise.name} прибыль больше среднего')





