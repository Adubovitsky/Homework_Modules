# фунцкия для тестирования встроенной функции filter
import os
import pickle

def check_numbers(x): #Функция проверяет является ли аргумент больше нуля или нет
    if x >0:
        return True
    else:
        return False

def write_to_file(file,data):# Функция преобразует данные в формат строки и записывает в файл
    f=open(file,"w")
    f.write(str(data))
    f.close()

def make_filelist(path): #Функция формирует список файлов, находящихся в указанной директории
    all_object_list=os.listdir(path)
    file_list = []
    for i in all_object_list:
        if os.path.isfile(i)==True:
            file_list.append(i)
    return file_list

def make_folderlist(path): #Функция формирует список папок, находящихся в указанной директории
    all_object_list=os.listdir(path)
    folder_list = []
    for i in all_object_list:
        if os.path.isdir(i)==True:
            folder_list.append(i)
    return folder_list

def remove_symbols(string, symbols): #Функция удаляет некоторые символы строки
    for i in string:
        if i in symbols:
            string = string.replace(i,"")
    return string
