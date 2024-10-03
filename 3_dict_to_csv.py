"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dict_list = [
        {'name': 'Rajesh', 'age': 29, 'job': 'Scammer'},
        {'name': 'Charles', 'age': 55, 'job': 'Bum'},
        {'name': 'James', 'age': 98, 'job': 'Retired'},
        {'name': 'Larry', 'age': 23, 'job': 'Unemployed'}

    ]
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in dict_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
