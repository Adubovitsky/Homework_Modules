
import os
import shutil
import sys
import json
from victory import game_victorina
from Bank_account import bank_account
import Functions

while True:
    print('Выберите пункт меню:\n 1-Создать новую папку \n 2-Удалить файл/папку \n 3-Копировать файл/папку'
          '\n 4-Просмотр содержимого рабочей директории \n 5-Посмотреть только папки \n 6-Посмотреть только файлы '
          '\n 7- Эаписать перечень файлов и папок в файл listdir.txt'
          '\n 8-Просмотр информации об операционнной системе \n 9-Создатель программы \n 10-Играть в Викторину '
          '\n 11-Мой банковский счет \n 12-Смена рабочей директории \n 13-Выход \n')
    choice = int(input())
    if choice==1: #Создать новую папку
       folder_name = input('Введите название новой папки ')
       os.mkdir(folder_name)
    elif choice==2: #Удалить файл/папку
        name_del = input('Введите название файла/папки для удаления ')
        if os.path.isfile(name_del)==True:
            print(os.path.isfile(name_del))
            os.remove(name_del)
        else:
            shutil.rmtree(name_del)
    elif choice == 3: #Копировать файл/папку
        copy_source = input("Введите название файла/папки для копирования ")
        copy_result = input("Введите название копии ")
        if os.path.isfile(copy_source):
            shutil.copy(copy_source,copy_result)
        else:
            shutil.copytree(copy_source,copy_result)
    elif choice == 4: #Просмотр содержимого рабочей директории
        #path = input('Введите путь и название папки для просмотра ')
        print(os.listdir())
    elif choice == 5: #Посмотреть только папки
        path = os.getcwd()
        print (Functions.make_folderlist(path))
    elif choice == 6: #Посмотреть только файлы
        path = os.getcwd()
        print (Functions.make_filelist(path))
    elif choice == 7: #Эаписать перечень файлов и папок в файл listdir.txt
        path = os.getcwd()
        file_list = str(Functions.make_filelist(path))
        signs = ['[', ']', '"', "'"]
        file_list_final = Functions.remove_symbols(file_list,signs)
        folder_list = json.dumps(Functions.make_folderlist(path))# Насколько я понял, преобразование в строку можно сделать
                                                            #как с помощью функции str, так и помощью json.dumps
        folder_list_final = Functions.remove_symbols(folder_list,signs)
        with open("listdir.txt", "w") as f:
            f.write("files: ")
            f.write(file_list_final)
            f.write("\n")
        with open("listdir.txt", "a") as f:
            f.write("dirs: ")
            f.write(folder_list_final)
    elif choice == 8: #Просмотр информации об операционнной системе
        print(sys.platform)
    elif choice == 9: #Создатель программы
        print(sys.copyright)
    elif choice == 10: # Играть в Викторину
        print('Игра Викторина!')
        game_victorina()
    elif choice == 11: # Мой банковский счет
        bank_account()
    elif choice == 12: # Смена рабочей директории
        new_path = input("Введите путь к желаемой директории ")
        os.chdir(new_path)
        print(os.getcwd())
    elif choice == 13: #
        break
    else:
        print("Неверный ввод данных")

