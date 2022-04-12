
import os
import shutil
import sys
from victory import game_victorina
import Bank_account

while True:
    print('Выберите пункт меню:\n 1-Создать новую папку \n 2-Удалить файл/папку \n 3-Копировать файл/папку'
          '\n 4-Просмотр содержимого рабочей директории \n 5-Посмотреть только папки \n 6-Посмотреть только файлы'
          '\n 7-Просмотр информации об операционнной системе \n 8-Создатель программы \n 9-Играть в Викторину '
          '\n 10-Мой банковский счет \n 11-Смена рабочей директории \n 12-Выход \n')
    choice = int(input())
    if choice==1:
       folder_name = input('Введите название новой папки ')
       os.mkdir(folder_name)
    elif choice==2:
        name_del = input('Введите название файла/папки для удаления ')
        if os.path.isfile(name_del)==True:
            print(os.path.isfile(name_del))
            os.remove(name_del)
        else:
            shutil.rmtree(name_del)
    elif choice == 3:
        copy_source = input("Введите название файла/папки для копирования ")
        copy_result = input("Введите название копии ")
        if os.path.isfile(copy_source):
            shutil.copy(copy_source,copy_result)
        else:
            shutil.copytree(copy_source,copy_result)
    elif choice == 4:
        #path = input('Введите путь и название папки для просмотра ')
        print(os.listdir())
    elif choice == 5:
        folder_list=[]
        for i in os.listdir():
            if os.path.isfile(i)==False:
                folder_list.append(i)
        print(folder_list)
    elif choice == 6:
        file_list=[]
        for i in os.listdir():
            if os.path.isfile(i)==True:
                file_list.append(i)
        print(file_list)
    elif choice == 7:
        print(sys.platform)
    elif choice == 8:
        print(sys.copyright)
    elif choice == 9:
        print('Игра Викторина!')
        game_victorina()
    elif choice == 10:
        Bank_account.bank_account()
    elif choice == 11:
        new_path = input("Введите путь к желаемой директории ")
        os.chdir(new_path)
        print(os.getcwd())
    elif choice == 12:
        break
    else:
        print("Неверный ввод данных")

