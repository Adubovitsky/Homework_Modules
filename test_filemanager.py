import os
import pickle
import shutil
from victory import correct_answer
import Functions

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

def test_writetofile():
    testfile = "tf.txt"
    Functions.write_to_file(testfile,500)
    with open(testfile,"r") as f:
        assert f.read()=="500"
    os.remove(testfile)

def test_pickle():
    shopping_report ={"food": 100, "cloth": 300, "travel": 250}
    testfile = "testfile.txt"
    with open(testfile,"wb") as f:
        pickle.dump(shopping_report,f)
    with open(testfile, "rb") as f:
        assert pickle.load(f) == shopping_report
    os.remove(testfile)

def test_removesymbols():
    text = "Hello?? <world%^. It's@@ me"
    symbols = ["?","!","%","@","<","^"]
    assert Functions.remove_symbols(text,symbols) == "Hello world. It's me"