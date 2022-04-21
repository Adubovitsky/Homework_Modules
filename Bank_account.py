"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import pickle
import Functions

def bank_account():
    FILE_ACCOUNT = "account_balance.txt"
    if os.path.exists(FILE_ACCOUNT):
        f=open(FILE_ACCOUNT,"r")
        account_saldo = int(f.read())  # Остаток на счете
        f.close()
    else:
        account_saldo = 0

    shopping_report = {}  # Словарь для накопления информации о покупках
    if os.path.exists("shopping_data.txt"):
         with open("shopping_data.txt","rb") as g:
           shopping_report= pickle.load(g)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню ')

        if choice == '1':
            deposit_amount_str = input("Введите сумму пополнения счета ")
            deposit_amount = int(deposit_amount_str)
            account_saldo += deposit_amount
            Functions.write_to_file(FILE_ACCOUNT,account_saldo)
        elif choice == '2':
            purchase_amount = int(input("Введите сумму покупки "))
            if purchase_amount <= account_saldo:
                purchase_name = input("Введите название покупки ")
                account_saldo -= purchase_amount
                shopping_report[purchase_name] = purchase_amount
                Functions.write_to_file(FILE_ACCOUNT, account_saldo)
            else:
                print("Недостаточно средств на счете")
            pass
        elif choice == '3':
            print(shopping_report)
            pass
        elif choice == '4':
            with open("shopping_data.txt","wb") as f1:
                pickle.dump(shopping_report,f1,)
            break
        else:
            print('Неверный пункт меню')



