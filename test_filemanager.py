import os
import shutil
from victory import correct_answer

def test_os_mkdir():
    new_dir = "New"
    os.mkdir(new_dir)
    assert (os.path.exists(new_dir))==True
    shutil.rmtree(new_dir)
    assert(os.path.exists(new_dir))==False

def test_shutil_copy():
    copy_source = "main.py"
    copy_file = "main_copy.py"
    shutil.copy(copy_source, copy_file)
    assert (os.path.exists(copy_file))==True
    os.remove(copy_file)
    assert (os.path.exists(copy_file)) == False

def test_correctanswer():
    Birthdays = {"Александр Сергеевич Пушкин": "26.05.1799",  "Михаил Юрьевич Лермонтов":"15.10.1814" }
    assert correct_answer(Birthdays,"Александр Сергеевич Пушкин") == ("двадцать шестое", "мая", "1799")
